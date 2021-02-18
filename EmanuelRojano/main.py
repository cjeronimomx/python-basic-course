import datetime

from dotenv import load_dotenv
from config import logs
from domain import requests, file_bulks

status_bulks = ("IN_PROGRESS", "PENDING", "NOT_EXECUTED", "NOT_PROCESS");

def create_bulk():
    id_bulk = requests.create_bulk()
    if id_bulk is not None:
        file_bulks.writte_bulk_id(id_bulk)
    else:
        log.error("Error creating bulk...")

def verify_process(id_bulk):
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

    if id_bulk is None:
        log.debug(f"First Bulk...")
        create_bulk()
    else:
        verify_process(id_bulk)

