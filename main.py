# Author:arvinljw

import tornado.ioloop
import tornado.web
import tornado.options
import os
from common.url_router import include, url_wrapper
from models import init_db
from sqlalchemy.orm import scoped_session, sessionmaker
from conf.base import BaseDB, engine, HOST_NAME, SERVER_PORT


class Application(tornado.web.Application):
    def __init__(self):
        init_db()
        handlers = url_wrapper([
            (r"/api/v1/users/", include('views.users.users_urls')),
            (r"/api/v1/upload/", include('views.upload.upload_urls')),
        ])
        # 定义 Tornado 服务器的配置项，如 static/templates 目录位置，debug 级别等
        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates")
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = scoped_session(sessionmaker(bind=engine, autocommit=False,
                                              autoflush=True, expire_on_commit=False))


if __name__ == '__main__':
    print("Tornado server is %s ready for service\r" % HOST_NAME)
    tornado.options.parse_command_line()
    Application().listen(SERVER_PORT, xheaders=True)
    tornado.ioloop.IOLoop.instance().start()
