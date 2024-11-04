from db.datasources.mongo_datasource import MongoDataSource
from core.settings import ProjectSettings


def get_mongo_ds():
    project_settings = ProjectSettings()
    mongo_data_source = MongoDataSource(host=project_settings.MongoDBHost, 
                    port=project_settings.MongoDBPort, 
                    username=project_settings.MongoDBUser, 
                    password=project_settings.MongoDBPassword,
                    database=project_settings.MongoDBName)
    try:
        yield mongo_data_source
    finally:
        mongo_data_source.close()
