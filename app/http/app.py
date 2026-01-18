"""

@Time :  
@Author : 4ever
@File : .py

"""
from injector import Injector
from internal.router import Router
from internal.server import Http
from config import Config
import dotenv
dotenv.load_dotenv()
injector = Injector()
conf = Config()
app = Http(__name__, config = conf,router=injector.get(Router))
if(__name__ == "__main__"):
    app.run(debug=True)