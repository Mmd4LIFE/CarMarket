"""
    created at nov 18/2020 by Mmd4LIFE
    - data context for authentication
"""

from peewee import (
    Model, CharField, DateTimeField,
    SqliteDatabase
)


class AppContext:
    data_context = SqliteDatabase("./assets/auth.db")

    def __init__(self):
        self.data_context.connect(reuse_if_open="True")
        self.data_context.create_tables([User, Car])


class BaseModel(Model):
    class Meta:
        database = AppContext.data_context


class User(BaseModel):
    username = CharField(unique=True, max_length=100)
    password = CharField(max_length=100)
    created_time = DateTimeField()

class Car(BaseModel):
    name = CharField(max_length=40)
    model = CharField(max_length=40)
    color = CharField(max_length=20)
    car_number = CharField(max_length=20, unique=True)
    created_time = DateTimeField()
