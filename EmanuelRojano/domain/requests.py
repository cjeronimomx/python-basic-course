import requests
import os
import datetime
from config import logs

log = logs.config_loggin()

def get_headers():
    return {'Content-Type': os.getenv("JSON_HEADER"), 'Accept': os.getenv("JSON_HEADER"), 'Authorization': f'Bearer {os.getenv("TOKEN")}'}

def check_status(id_bulk):
    log.debug(f"Check status bulk migration: {datetime.datetime.now()} ")
    status = None

    resp = requests.get(os.getenv("URL_TENANT")+'/v0/ns/'+os.getenv("NAMESPACE")+'/domains/'+os.getenv("DOMAIN")+'/massive-documents/bulks/'+id_bulk, headers=get_headers())
    if resp.status_code == 200:
        log.debug(f"Code 200: {datetime.datetime.now()} ")
        log.info(f"JSON RESPONSE: {resp.json()}")
        field = resp.json()['data']
        log.info(f"Id : {field['id']}")
        log.info(f"Estatus : {field['status']}")
        log.info(f"Total : {field['totalTasks']}")
        log.info(f"Completed : {field['completedTasks']}")
        log.info(f"Failed : {field['failedTasks']}")
        log.info(f"Pending : {field['pendingTasks']}")
        status = field['status']
    else:
        log.error(resp.text)
    return status


def create_bulk():
    log.debug(f"Create new bulk: {datetime.datetime.now()} ")
    id_bulk=None
    log.debug(f"Data: {get_data_bulk()}")
    resp = requests.post(os.getenv("URL_TENANT") + '/v0/ns/' + os.getenv("NAMESPACE") + '/domains/' + os.getenv("DOMAIN") + f'/massive-documents/bulks:createBinaryMigration'
                         , json=get_data_bulk()
                        , headers=get_headers())
    if resp.status_code == 201:
        log.debug(f"Code 201: {datetime.datetime.now()} ")
        log.info(f"JSON RESPONSE: {resp.json()}")
        field = resp.json()['data']
        log.info(f"Id : {field['id']}")
        log.info(f"Estatus : {field['status']}")
        log.info(f"Total : {field['totalTasks']}")
        log.info(f"Completed : {field['completedTasks']}")
        log.info(f"Failed : {field['failedTasks']}")
        id_bulk = field['id']
    else:
        log.error(resp.text)
    return id_bulk

def get_data_bulk():
    return {"maxBinaries": int(os.getenv("MAX_BINARIES")), "sourceStorage": os.getenv("SOURCE_STORAGE"), "sourceContainer": os.getenv("SOURCE_CONTAINER"), "destinationStorage": os.getenv("DESTINATION_STORAGE")}