from .json_generator_client.generated.swagger.json_generator_client import JsonGeneratorClient
from .qualified_name_client.generated.swagger.qualified_name_client import QualifiedNameClient
from .metadata_wrapper.generated.swagger.metadata_wrapper_client import MetadataWrapperClient

class RestFactory:
    def __init__(self, config):
        self.config = config

    def getQnClient(self):
        return QualifiedNameClient(self.config['qualifiedNameServiceUrl'])

    def getJsonGeneratorClient(self):
        return JsonGeneratorClient(self.config['jsonGeneratorServiceUrl'])

    def getMetadataClient(self):
        return MetadataWrapperClient(self.config['metadataWrapperServiceUrl'])
