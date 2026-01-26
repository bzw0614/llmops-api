"""

@Time :  
@Author : 4ever
@File : .py

"""
from pkg.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from injector import Module, Binder
from internal.extension.database_extension import db
from internal.extension.migrate_extension import migrate
class DatabaseModule(Module):
    def configure(self, binder: Binder):
        # 将db实体映射到SQLAlchemy
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)
