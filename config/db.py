from sqlalchemy import create_engine, MetaData, engine

DB_CONNECTION = "postgresql"
DB_HOST = "ec2-54-158-247-97.compute-1.amazonaws.com"
DB_NAME = "d6gnk3ar4pba3p"
DB_PORT = "5432"
DB_USER = "mkiatgybkpqblr"
DB_PASSWORD = "64cb184329cfe6ce7f6c9df6b19a5667e3955fa73dfa4ae181bd0c0d328ee838"

engine = create_engine(
    f"{DB_CONNECTION}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

meta = MetaData()

conn = engine.connect()
