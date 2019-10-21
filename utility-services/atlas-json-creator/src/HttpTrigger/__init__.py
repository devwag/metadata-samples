import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Atlas Json Creator function processed a request.')

    return func.HttpResponse("Atlas Json Creator function is up and running.")

