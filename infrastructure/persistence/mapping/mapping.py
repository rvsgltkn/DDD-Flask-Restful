#!/usr/bin/env python
# # -*- coding: utf-8 -*-

from sqlalchemy import Table, MetaData, Column, String
from sqlalchemy.orm import mapper
from domain.student.model.student import Student

custom_metadata = MetaData()

student_mapping = Table('student', custom_metadata,
                        Column('id', String(36), primary_key=True),
                        Column('name', String(50)),
                        Column('surname', String(50)),
                        Column('tel', String(50)),
                        )

mapper(Student, student_mapping)
