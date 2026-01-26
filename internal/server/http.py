"""

@Time :  
@Author : 4ever
@File : .py

"""
from flask import Flask,jsonify
from internal.exception import CustomException
from internal.model import App
from pkg.response import Response,HttpCode,json
from internal.router import Router
from config import Config
from pkg.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
class Http(Flask):
    #第一个参数是 非命名参数 例如1234 第二个参数是命名参数例如a=1
    #命名参数要写在非命名参数之后
    def __init__(self, *args, config:Config,db:SQLAlchemy,migrate:Migrate,router:Router ,**kwargs):
        super().__init__(*args, **kwargs)
        self.config.from_object(config)
        # 注册绑定错误异常处理
        self.register_error_handler(Exception, self._register_error_handler)

        # 初始化sql
        db.init_app(self)

        migrate.init_app(self,db,directory="internal/migrations")
        # 生成数据库表
        # 注册应用路由
        # 这样就不用写一大堆@app.route()
        router.register_router(self)


    def _register_error_handler(self,error:Exception):
        # 如果是我们的自定义异常
        if isinstance(error,CustomException):
            return json(Response(code = error.code,message=error.message,data=error.data if error.data is not None else {}))
        # 如果不是我们的自定义异常，有可能是数据库、程序抛出的，也可以提取信息，设置FAIL状态码
        return json(Response(code = HttpCode.FAIL,message=str(error),data={}))
