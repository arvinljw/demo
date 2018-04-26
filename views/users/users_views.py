import tornado.web
from tornado.escape import json_decode
from datetime import datetime
from conf.log import init_log
from views import BaseRequestHandler

# 从commons中导入http_response方法
from common.commons import (
    http_response,
)
# 从配置文件中导入错误码
from conf.base import (
    ERROR_CODE,
)

from models import (
    Users
)

# Configure logging
logger = init_log("log/users/users.log", "Users")


class RegisterHandle(BaseRequestHandler):
    """handle /users/register request
    :param phone: users sign up phone
    :param password: users sign up password
    :param code: users sign up code, must six digital code
    """

    def post(self):
        try:
            # 获取入参
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
            verify_code = args['code']
        except:
            # 获取入参失败时，抛出错误码及错误信息
            logger.info("RegisterHandle: request argument incorrect")
            http_response(self, ERROR_CODE['1001'], 1001)
            return

        ex_user = self.db.query(Users).filter_by(phone=phone).first()
        if ex_user:
            http_response(self, ERROR_CODE['1002'], 1002)
            self.db.close()
            return
        else:
            logger.debug("RegisterHandle: insert db, user: %s" % phone)
            create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            add_user = Users(phone, password, create_time)
            self.db.add(add_user)
            self.db.commit()
            self.db.close()
            # 处理成功后，返回成功码“200”及成功信息“ok”
            logger.debug("RegisterHandle: register successfully")
            http_response(self, ERROR_CODE['200'], 200)


class LoginHandle(BaseRequestHandler):
    """handle /users/login request
    :param phone: users sign up phone
    :param password: users sign up password
    """

    def get(self):
        try:
            # 获取入参
            phone = self.get_argument("phone")
            password = self.get_argument("password")
        except:
            # 获取入参失败时，抛出错误码及错误信息
            logger.info("LoginHandle: request argument incorrect")
            http_response(self, ERROR_CODE['1001'], 1001)
            return

            # 从数据库 Users 表查找入参中的 phone 是否存在
        ex_user = self.db.query(Users).filter_by(phone=phone).first()
        if ex_user:
            # 如果手机号已存在，返回首页 H5 页面 index.html
            logger.debug("LoginHandle: get user login: %s" % phone)
            self.render("index.html")
            self.db.close()
            return
        else:
            # 用户不存在，提示用户未注册
            http_response(self, ERROR_CODE['1003'], 1003)
            self.db.close()
            return
