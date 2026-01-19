"""

@Time :  
@Author : 4ever
@File : .py

"""
from .http_code import HttpCode
from dataclasses import field,dataclass
from typing import Any
from flask import jsonify
@dataclass
class Response:
    '''基础HTTP响应格式'''
    code : HttpCode = HttpCode.SUCCESS
    message : str =  ""
    data : Any=field(default_factory=dict)

def json(data:Response=None):
    return jsonify(data),200

def success_json(data:Any=None):
    return jsonify(Response(code=HttpCode.SUCCESS,message="",data=data))

def fail_json(data:Any=None):
    return jsonify(Response(code=HttpCode.FAIL,message="",data=data))

def validation_error_json(errors:dict=None):
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors.get(first_key)[0]
    else:
        msg = ""
    return jsonify(Response(code=HttpCode.VALIDATION_ERROR,message=msg,data=errors))

def message(code:HttpCode=None,msg:str=""):
    return json(Response(code=code,message=msg,data={}))

def success_message(msg:str=""):
    return message(code=HttpCode.SUCCESS,message=msg)

def fail_message(msg:str=""):
    return message(code=HttpCode.FAIL,message=msg)

def not_found_message(msg:str=""):
    return message(code=HttpCode.NOT_FOUND,message=msg)

def unauthorized_message(msg:str=""):
    return message(code=HttpCode.UNAUTHORIZED,message=msg)

def forbidden_message(msg:str=""):
    return message(code=HttpCode.FORBIDDEN,message=msg)