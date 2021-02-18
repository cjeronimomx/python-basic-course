import os
from config import logs

log = logs.config_loggin()


def read_last_bulk():
    # r=read, w=write, a=append
    try:
        with open(os.getenv("BULKS_FILE"), "r") as file:
            return file.readlines()[-1]
    except FileNotFoundError as ex:
        log.error(ex.strerror)


def writte_bulk_id(id):
    with open(os.getenv("BULKS_FILE"), "a") as file:
        file.write('\n'+id)

