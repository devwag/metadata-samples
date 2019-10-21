import datetime
import logging
import os

import azure.functions as func

from .lineageEventProcessor import LineageEventProcessor

def main(timer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if timer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

    LineageEventProcessor(os.environ).scanEvents()
