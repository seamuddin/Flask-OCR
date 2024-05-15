import os
from datetime import timedelta
from sqlalchemy.engine import URL


def create_db_uri(db_type, username, password, host, port, database):
    return URL.create(str(db_type), username=username, password=password, host=host, port=port, database=database)


db1_uri = create_db_uri('mysql+pymysql','system', 'qweseam1','103.175.242.10', '3306', 'voter')

SQLALCHEMY_DATABASE_URI = db1_uri

SQLALCHEMY_BINDS = {
    "db1": db1_uri,
    # "db2": db2_uri,
}

# Other configurations
SQLALCHEMY_ENGINE_OPTIONS = {
    'pool_recycle': 3600,
    'pool_timeout': 300,
    'pool_pre_ping': True,
}


API_TITLE = os.getenv("API_TITLE")
API_VERSION = os.getenv("API_VERSION")
SECRET_KEY = os.getenv("SECRET_KEY")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
BIDA_APPLICATION_URL = os.getenv('BIDA_APPLICATION_URL')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)
