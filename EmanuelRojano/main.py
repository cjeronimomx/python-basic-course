"""
This APP manages the binary migration, from a source to the destinations
depends of the configuration on .env file (SOURCE_STORAGE, SOURCE_CONTAINER, DESTINATION_STORAGE)

This APP is triggered by a cron executor, and every execution gets the last bulk_id saved in bulks.txt file
The last bulk_id is checked for verify the status, depends on the last bulk id status, the APP
executes the service for create new bulk, the new bulk id generated is saved in bulks.txt

"""

import datetime

from dotenv import load_dotenv
from config import logs
from domain import requests, file_bulks

status_bulks = ("IN_PROGRESS", "PENDING", "NOT_EXECUTED", "NOT_PROCESS");


def create_bulk():
    """
    This function creates a new bulk and
    writes the id in the bulks.txt file
    """
    id_bulk = requests.create_bulk()
    if id_bulk is not None:
        file_bulks.writte_bulk_id(id_bulk)
    else:
        log.error("Error creating bulk...")


def verify_process(id_bulk):
    """
    This function verify the bulk_id status
    if the bulk has finished, creates new bulk
    """
    status = requests.check_status(id_bulk)
    log.info(f"Bulk in status {status}")
    if status is not None and status in status_bulks:
        log.info(f"Finished Process...")
    elif status is not None:
        log.info(f"Another bulk will be generated...")
        create_bulk()


if __name__ == "__main__":
    load_dotenv()
    log = logs.config_loggin()

    log.debug(f"App started at: {datetime.datetime.now()} ")

    id_bulk=file_bulks.read_last_bulk()
    log.debug(f"Last bulk_id: {id_bulk} ")

    """
    If the bulk.txt file is empty or
    not exists (first time), it creates new bulk 
    """
    if id_bulk is None:
        log.debug(f"First Bulk...")
        create_bulk()
    else:
        verify_process(id_bulk)

