from db.datasources.mongo_datasource import MongoDataSource
from core.settings import ProjectSettings


def get_mongo_ds():
    settings = ProjectSettings()
    mongo_data_source = MongoDataSource(host=settings.MongoDBHost, 
                    port=settings.MongoDBPort, 
                    username=settings.MongoDBUser, 
                    password=settings.MongoDBPassword)
    try:
        yield mongo_data_source
    finally:
        mongo_data_source.close()
