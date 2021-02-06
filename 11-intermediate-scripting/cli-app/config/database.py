from pymongo import MongoClient
import os


def connect():
    db_url = f"mongodb+srv://" \
             f"{os.getenv('MONGODB_USER')}:" \
             f"{os.getenv('MONGODB_PW')}@" \
             f"{os.getenv('MONGODB_HOST')}/" \
             f"retryWrites=true&w=majority"
    return MongoClient(db_url)

    """
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DB_NAME][COLLECTION_NAME]
    projects = collection.find()
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects
    """
