#!/usr/bin/env python
# # -*- coding: utf-8 -*-

from infrastructure.db import DbManager


class RepositoryBase(object):
    def __init__(self, class_name):
        self.__db = DbManager.DB
        self.__session = DbManager.DB.session
        self.__class = class_name

    @property
    def db(self):
        return self.__db

    @property
    def session(self):
        return self.__session

    def save(self, entity, commit=True):
        self.session.add(entity)
        if commit:
            self.session.commit()

    def commit(self):
        self.session.commit()

    def get_all(self):
        return DbManager.DB.session.query(self.__class).all()

    def get_by_id(self, _id):
        return DbManager.DB.session.query(self.__class).get(_id)
