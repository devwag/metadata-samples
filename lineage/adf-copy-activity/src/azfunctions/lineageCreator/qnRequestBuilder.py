from .qualified_name_client.generated.swagger.models import Model0

def buildDatasetQNRequest(dataset):
    result = Model0(**{
            "cosmosdb_uri" : "http://somewhere/whatever/",
            "cosmosdb_database" : "db",
            "container_name" : "container"
        })

    return result
