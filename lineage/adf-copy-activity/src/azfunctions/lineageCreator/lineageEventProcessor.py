import logging

from .qualified_name_client.generated.swagger.qualified_name_client import QualifiedNameClient
from .json_generator_client.generated.swagger.json_generator_client import JsonGeneratorClient
from .restFactory import RestFactory
from .sqlWrapper import SqlWrapper
from .qnRequestBuilder import buildDatasetQNRequest

class LineageEventProcessor:
    def __init__(self, config):
        self.config = config
        self.restFactory = RestFactory(self.config)
        self.sql = SqlWrapper(config)

    def scanEvents(self):
        datasets = self.sql.getModifiedDatasets()

        lineageRequests = self._buildLineageRequests(datasets)

        self._reportLineage(lineageRequests)

        self._deleteRequests(lineageRequests)

    def _buildLineageRequests(self, datasets):
        lineageRequests = {}

        qnClient = self.restFactory.getQnClient()

        for dataset in datasets:
            dsInfo = buildDatasetQNRequest(dataset)

            qn = qnClient.get_qualified_name(
                type_name=dataset['type'], 
                body=dsInfo, 
                code=self.config['qualifiedNameServiceKey'])
            
            requestId = dataset["request_id"]

            #todo: handle empty guids

            dataset["guid"] = qn.guid
            dataset["qualified_name"] = qn.qualified_name

            if requestId not in lineageRequests:
                lineageRequests[requestId] = { "sources" : [], "destinations" : [] }

            if dataset["direction"].lower() == "source":
                lineageRequests[requestId]["sources"] += [dataset]
            else:
                lineageRequests[requestId]["destinations"] += [dataset]

        return lineageRequests

    def _reportLineage(self, lineageRequests):
        pass

    def _deleteRequests(self, lineageRequests):
        ids = [id for id in lineageRequests.keys()]
        self.sql.deleteRequests(ids)
