"""

@Time :  
@Author : 4ever
@File : .py

"""
from pkg.sqlalchemy import SQLAlchemy
from injector import Module, Binder
from internal.extension.database_extension import db

class DatabaseModule(Module):
    def configure(self, binder: Binder):
        # 将db实体映射到SQLAlchemy
        binder.bind(SQLAlchemy, to=db)
