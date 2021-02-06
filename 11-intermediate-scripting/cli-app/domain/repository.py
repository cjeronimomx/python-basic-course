import os
from datetime import datetime


def create_metric(db_client, metric_data, metric_type: str):
    metric_data["key"] = datetime.now()
    db = db_client.metrics
    collection = db[metric_type]
    collection.insert_one(metric_data)
    return metric_data["key"]


def read_metric(db_client, key, metric_type: str):
    db = db_client.metrics
    collection = db[metric_type]
    metric_data = collection.find_one({'key': key})
    return metric_data
