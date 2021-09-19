from sqlalchemy import create_engine, MetaData, engine

DB_CONNECTION = "db_connection"
DB_HOST = "db_host"
DB_NAME = "db_name"
DB_PORT = "db_port"
DB_USER = "db_user"
DB_PASSWORD = "db_password"

engine = create_engine(
    f"{DB_CONNECTION}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

meta = MetaData()

conn = engine.connect()
