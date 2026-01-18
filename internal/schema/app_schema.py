"""

@Time :  
@Author : 4ever
@File : .py

"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
class CompletionReq(FlaskForm):
    '''基础聊天接口请求验证'''
    query = StringField('query',
                        validators=[DataRequired(message='用户的输入是必填项'),
                                    Length(max=2000, message='Query too long')])
    submit = SubmitField('Submit')