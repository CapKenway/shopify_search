import sqlalchemy as sql
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
import configparser
import os
from datetime import datetime as dt

base = declarative_base()

class Products(base):
    __tablename__="products"
    id = sql.Column(sql.Integer, primary_key=True)
    title = sql.Column(sql.String)
    price = sql.Column(sql.String)
    slug = sql.Column(sql.String)
    store = sql.Column(sql.String)

    def __repr__(self) -> str:
        return f"Product: {self.title} at {self.store}"

class Stores(base):
    __tablename__="stores"
    id = sql.Column(sql.Integer, primary_key=True)
    store = sql.Column(sql.String)

    def __repr__(self) -> str:
        return f"ID: {self.id} of {self.store}"

if __name__ == "__main__":
    def str_to_bool(input:str)->bool:
        if input=='true':
            return True
        elif input=='false':
            return False
        else:
            return False
    config = configparser.ConfigParser()
    config.read('./config.ini')
    # db_address = "sqlite://database.db"
    db_address = config['SQL']['address']

    if str_to_bool(config['SQL']['sqlite']):
        db_abspath = os.path.abspath(f'./{db_address}')
        # print(f"sqlite:///{db_abspath}")
        engine = sql.create_engine(f"sqlite:///{db_abspath}",echo=True)
    else:
        engine = sql.create_engine(db_address,echo=True)
    # engine = sql.create_engine(db_address, echo=True)
    conn = engine.connect()
    session = Session(engine)
    meta = sql.MetaData(engine)
    base = declarative_base()

    prod_table = sql.Table(
        "products",
        meta,
        sql.Column('id',sql.Integer, primary_key=True),
        sql.Column('title',sql.String),
        sql.Column('price',sql.String),
        sql.Column('slug',sql.String),
        sql.Column('store',sql.String)
        )
    store_table = sql.Table(
        "stores",
        meta,
        sql.Column('id',sql.Integer, primary_key=True),
        sql.Column('store',sql.String),
        )
    # session = Session(engine)
    meta.create_all()
    print(meta.bind)
    session.commit()