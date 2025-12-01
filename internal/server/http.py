"""

@Time :  
@Author : 4ever
@File : .py

"""
from flask import Flask
from internal.router import Router

class Http(Flask):
    #第一个参数是 非命名参数 例如1234 第二个参数是命名参数例如a=1
    #命名参数要写在非命名参数之后
    def __init__(self, *args, router:Router ,**kwargs):
        super().__init__(*args, **kwargs)
        # 注册应用路由
        router.register_router(self)