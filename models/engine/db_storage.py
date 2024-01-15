#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine, MetaData
from models.base_model import Base


class DBStorage:
    """This class defines the DBStorage engine"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage engine"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(user, password, host, database), pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session"""
        from models import classes
        results = {}

        if cls:
            objects = self.__session.query(classes[cls]).all
        else:
            objects = []
            for key, value in classes.items():
                objects.extend(self.__session.query(value).all())

        for obj in objects:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            results[key] = obj

        return results
