"""

@Time :  
@Author : 4ever
@File : .py

"""
from enum import Enum
class HttpCode(str,Enum):
    SUCCESS = "success", # 成功
    FAIL = "fail", # 失败
    NOT_FOUND = "not_found", # 未找到
    UNAUTHORIZED = "unauthorized", # 未授权
    FORBIDDEN = "forbidden", # 无权限
    VALIDATION_ERROR = "validation_error" # 数据验证错误
