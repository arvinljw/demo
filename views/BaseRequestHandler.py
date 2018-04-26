from tornado.web import RequestHandler
from sqlalchemy.orm import scoped_session


class BaseRequestHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    @property
    def db(self):
        db = self.application.db
        if isinstance(db, scoped_session):
            # 这里处理一下，方便在使用时知道是什么类型，有方法提示不那么容易写错
            return db
