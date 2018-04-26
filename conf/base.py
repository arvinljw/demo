from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:123456@localhost:3306/demo?charset=utf8', encoding="utf8", echo=False)
BaseDB = declarative_base()

HOST_NAME = 'http://139.199.117.22'
SERVER_PORT = 8000

SERVER_HEADER = '%s:%s' % (HOST_NAME, SERVER_PORT)

ERROR_CODE = {
    "200": "ok",
    # Users error code
    "1001": "入参非法",
    "1002": "用户已注册",
    "1003": "用户尚未注册，请先注册",
    "2001": "上传图片不能为空",
}
