import os
import uuid
from dataclasses import dataclass

from injector import inject
from openai import OpenAI
from flask import request, jsonify
from internal.schema.app_schema import CompletionReq
from pkg.response import Response, HttpCode, success_json, validation_error_json, success_message
from internal.service.AppService import AppService
@inject
@dataclass
class AppHandler:
    app_Service : AppService
    def create_app(self):
        # 调用服务创建app
        app = self.app_Service.create_app()
        return success_message(f"应用已经创建成功，id为{app.id}")

    def get_app(self,id:uuid.UUID):
        # 调用服务创建app
        app = self.app_Service.get_app(id)
        return success_message(f"获取应用成功，应用名为{app.name}")

    def completion(self):
        req = CompletionReq()
        if not req.validate():
            return validation_error_json(req.errors)
        query = request.json.get('query')
        client = OpenAI(
            base_url=os.getenv("OPEN_API_BASE"),
        )
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                    "role":"system",
                    "content":"你是一个OpenAi开发的聊天机器人，请根据我的问题来回答"
                },
                {
                    "role":"user",
                    "content":query
                }
            ]
        )
        # response = client.responses.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role":"system","content":"你是OpenAi旗下的智能机器人，请根据用户提出的问题作出回答"},
        #         {"role":"user","content":query}
        #     ]
        # )
        content = completion.choices[0].message.content
        resp = Response(code = HttpCode.SUCCESS,message = "",data = {"content":content})
        '''Flask API的返回格式：字典、字符串、序列化后的字典'''
        '''没法直接返回resp'''
        return success_json({"content":content})
    def ping(self):
        return {"ping":"pong"}