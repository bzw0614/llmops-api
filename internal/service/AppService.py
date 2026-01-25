"""

@Time :  
@Author : 4ever
@File : .py

"""
import uuid

from pkg.sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from injector import inject
from internal.model import App
@inject
@dataclass
class AppService:
    db: SQLAlchemy
    def create_app(self) -> App:
        # 里面是yeild之前的代码
        with self.db.auto_commit():
            # 1.创建实体类
            # 2.将实体类添加到session
            # 3.将session提交给对话
            # 可以写在参数里，也可以在外面
            app = App(account_id =uuid.uuid4(),description = "智能聊天机器人",name = "魏传琪",icon = "")
            # app.name = "魏传琪"
            # app.description = "智能聊天机器人"
            # app.account_id =uuid.uuid4()
            self.db.session.add(app)
            # self.db.session.commit()
        return app

    def get_app(self,id:uuid.UUID) -> App:
        # 查询操作不需要commit
        return self.db.session.query(App).get(id)