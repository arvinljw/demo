import logging
from logging.handlers import TimedRotatingFileHandler


def init_log(logFilePath, name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = TimedRotatingFileHandler(logFilePath,
                                       when="D",
                                       interval=1,
                                       backupCount=30)
    formatter = logging.Formatter('%(asctime)s \
    %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', )
    handler.suffix = "%Y%m%d"
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
