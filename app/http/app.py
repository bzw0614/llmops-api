"""

@Time :  
@Author : 4ever
@File : .py

"""
from injector import Injector
from internal.router import Router
from internal.server import Http
from config import Config
from pkg.sqlalchemy import SQLAlchemy
import dotenv
from .module import DatabaseModule
from flask_migrate import Migrate
dotenv.load_dotenv()
injector = Injector([DatabaseModule])
conf = Config()
app = Http(__name__, db = injector.get(SQLAlchemy),migrate=injector.get(Migrate),config = conf,router=injector.get(Router))
if(__name__ == "__main__"):
    app.run(debug=True)