import logging

from .qualified_name_client.generated.swagger.models.azure_datalake_gen2_resource_set_py3 import AzureDatalakeGen2ResourceSet
from .qualified_name_client.generated.swagger.models.azure_cosmosdb_container_py3 import AzureCosmosdbContainer
from urllib.parse import urlparse

def buildDatasetQNRequest(dataset):

    datasetType = dataset['type']

    if datasetType == 'azure_datalake_gen2_resource_set':
        azure_resource = dataset['azure_resource']
        url = urlparse(azure_resource)

        azure_storage_uri = '%s://%s' %(url.scheme, url.hostname)
        (_, filesystem_name, resource_set_path) = url.path.split('/', 2)

        result = AzureDatalakeGen2ResourceSet(**{
                'azure_storage_uri' : azure_storage_uri,
                'filesystem_name' : filesystem_name,
                'resource_set_path' : resource_set_path
            })
    elif datasetType == 'azure_cosmosdb_container':

        azure_resource = dataset['azure_resource']
        url = urlparse(azure_resource)

        cosmosdb_uri = '%s://%s' %(url.scheme, url.hostname)
        (_, database, container) = url.path.split('/', 2)

        result = AzureCosmosdbContainer(**{
                'cosmosdb_uri' : cosmosdb_uri,
                'cosmosdb_database' : database,
                'container_name' : container
            })
    else:
        logging.error('Unknown lineage dataset type "%s"' % datasetType)
        return None

    return result
