"""

@Time :  
@Author : 4ever
@File : .py

"""
import os
from typing import Any
from .default_config import DEFAULT_CONFIG

# -> Any意思是返回啥类型都行
def _get_env(key: str) -> Any:
    # 获取环境变量，如果不存在则返回默认值
    return os.getenv(key,DEFAULT_CONFIG.get(key))
# 获取布尔类型的环境变量
def _get_bool_env(key: str) -> bool:
    value:str = _get_env(key)
    return value.lower() == "true" if value is not None else False
class Config:
    def __init__(self):
        '''关闭WTF的CSRF保护'''
        self.WTF_CSRF_ENABLED = False

        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_ECHO = _get_bool_env("SQLALCHEMY_ECHO")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": _get_env("SQLALCHEMY_POOL_SIZE"),
            "pool_recycle": _get_env("SQLALCHEMY_POOL_RECYCLE"),
        }
