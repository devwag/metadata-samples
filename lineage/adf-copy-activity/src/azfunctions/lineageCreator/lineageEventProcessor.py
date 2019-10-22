import logging

from .qualified_name_client.generated.swagger.qualified_name_client import QualifiedNameClient
from .json_generator_client.generated.swagger.json_generator_client import JsonGeneratorClient
from .restFactory import RestFactory
from .sqlWrapper import SqlWrapper
from .qnRequestBuilder import buildDatasetQNRequest
from .qualified_name_client.generated.swagger.models.adf_copy_activity_py3 import AdfCopyActivity

class LineageEventProcessor:
    def __init__(self, config):
        self.config = config
        self.restFactory = RestFactory(self.config)
        self.sql = SqlWrapper(config)

    def scanEvents(self):
        datasets = self.sql.getModifiedDatasets()

        lineageRequests = self._buildLineageRequests(datasets)

        self._reportLineage(lineageRequests)

        ##self._deleteRequests(lineageRequests) keep the records while debuging

    def _buildLineageRequests(self, datasets):
        lineageRequests = {}

        qnClient = self.restFactory.getQnClient()

        for dataset in datasets:
            requestId = dataset["request_id"]

            if requestId not in lineageRequests:
                lineageRequests[requestId] = { 
                    'datafactory_name' : dataset['datafactory_name'],
                    'pipeline_name' : dataset['pipeline_name'],
                    'activity_name' : dataset['activity_name'],
                    'sources' : [], 
                    'destinations' : [], 
                    'valid': False 
                }

            if dataset['direction'].lower() == "source":
                lineageRequests[requestId]['sources'] += [dataset]
            else:
                lineageRequests[requestId]['destinations'] += [dataset]

            try:
                dsInfo = buildDatasetQNRequest(dataset)

                if dsInfo is not None:
                    qn = qnClient.get_qualified_name(
                        type_name=dataset['type'], 
                        body=dsInfo, 
                        code=self.config['qualifiedNameServiceKey'])
                    
                    dataset["qualified_name"] = qn.qualified_name

                    if qn.is_exists:
                        dataset["guid"] = qn.guid
                        lineageRequests[requestId]['valid'] = True
                    else:
                        logging.error('Type "%s" does not exist in the Qualified Service' % dataset['type'])

            except Exception as e:
                logging.error('Error processing request %s: %s' % (requestId, e))

        for lineageRequest in lineageRequests.values():
            #if not lineageRequest['valid']: continue todo: enable when types are available

            activityInfo = AdfCopyActivity(**{
                'datafactory_name' : lineageRequest['datafactory_name'],
                'pipeline_name' : lineageRequest['pipeline_name'],
                'activity_name' : lineageRequest['activity_name']
            })

            qn = qnClient.get_qualified_name(
                type_name='adf_copy_activity', 
                body=activityInfo, 
                code=self.config['qualifiedNameServiceKey'])

            lineageRequest['qualified_name'] = qn.qualified_name
            if qn.is_exists:
                lineageRequest['guid'] = qn.guid
            else:
                lineageRequest['valid'] = False
                logging.error('Type "adf_copy_activity" does not exist in the Qualified Service')

        return lineageRequests

    def _reportLineage(self, lineageRequests):
        client = self.restFactory.getJsonGeneratorClient()
        logging.info('%d lineage requests processed', len(lineageRequests))

    def _deleteRequests(self, lineageRequests):
        ids = [id for id in lineageRequests.keys()]
        self.sql.deleteRequests(ids)
