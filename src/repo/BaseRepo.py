from marshmallow import Schema
from sqlalchemy.orm.decl_api import DeclarativeMeta

from connectors.sql import db_connector
from src.repo.BaseSession import BaseSession


class BaseRepo:
    BaseSession = BaseSession
    db_connector = db_connector

    def add(
        self, model: DeclarativeMeta, schema: Schema, data: dict, **kwargs
    ):
        new_data_dict = data.copy()
        final_data = None
        with self.BaseSession(self.db_connector) as Session:
            if kwargs:
                for key in kwargs:
                    new_data_dict[key] = kwargs[key]
            new_data = model(**new_data_dict)
            try:
                Session.add(new_data)
            except Exception as e:
                Session.rollback()
                raise e
            else:
                Session.commit()
                final_data = schema().dump(new_data)

        return final_data
