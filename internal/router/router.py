from flask import Flask,Blueprint
from internal.handler import AppHandler
from injector import inject
from dataclasses import dataclass
@inject
@dataclass
class Router:
    app_handler:AppHandler
    def __init__(self,app_handler:AppHandler):
        self.app_handler = app_handler
    def register_router(self,app:Flask):
        """注册路由"""
        #1.创建一个蓝图
        bp = Blueprint("llmops",__name__,url_prefix="",)

        #2.将url与对应的控制器方法做绑定

        #第一个请求参数是路径
        #第二个参数是methods=["GET","POST","DELETE"]get可以不写
        #第三个参数view_func是绑定的具体哪个函数 绑定的是函数，不是函数的执行结果 方法不要写括号
        bp.add_url_rule("/ping",view_func=self.app_handler.ping)
        bp.add_url_rule("/app/chat",methods = ["POST"],view_func=self.app_handler.completion)
        bp.add_url_rule("/app",methods = ["POST"],view_func=self.app_handler.create_app)
        bp.add_url_rule("/app/<id>", view_func=self.app_handler.get_app)

        #3.在应用上注册蓝图 (传入对应蓝图)
        app.register_blueprint(bp)