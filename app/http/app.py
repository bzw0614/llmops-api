"""

@Time :  
@Author : 4ever
@File : .py

"""
from injector import Injector
from internal.router import Router
from internal.server import Http
from config import Config
from internal.extension.database_extension import db
import dotenv
dotenv.load_dotenv()
injector = Injector()
conf = Config()
app = Http(__name__, db = db,config = conf,router=injector.get(Router))
if(__name__ == "__main__"):
    app.run(debug=True)