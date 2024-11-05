from db.datasources.mongo_datasource import MongoDataSource
from core.settings import ProjectSettings


def get_mongo_ds():
    project_settings = ProjectSettings()
    mongo_data_source = MongoDataSource(connection_string=project_settings.MongoDBConnectionString,
                                        database=project_settings.MongoDBName)
    try:
        yield mongo_data_source
    finally:
        mongo_data_source.close()
