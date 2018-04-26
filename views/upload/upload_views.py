import tornado.web
import os
from conf.log import init_log
from views import BaseRequestHandler

# 从commons中导入http_response及save_files方法
from common.commons import (
    http_response,
    save_files
)

# 从配置文件中导入错误码
from conf.base import (
    ERROR_CODE,
    SERVER_HEADER
)

# Configure logging
logger = init_log("log/upload/upload.log", "Upload")


class UploadFileHandle(BaseRequestHandler):
    """handle /upload/file request, upload image and save it to static/image/
    :param image: upload image
    """

    def post(self):
        try:
            # 获取入参
            image_metas = self.request.files['image']
        except:
            # 获取入参失败时，抛出错误码及错误信息
            logger.info("UploadFileHandle: request argument incorrect")
            http_response(self, ERROR_CODE['1001'], 1001)
            return

        if image_metas:
            # 获取当前的路径
            pwd = os.getcwd()
            save_image_path = os.path.join(pwd, "static/image/")
            logger.debug("UploadFileHandle: save image path: %s" % save_image_path)
            # 调用save_file方法将图片数据流保存在硬盘中
            file_name_list = save_files(image_metas, save_image_path)
            image_path_list = [SERVER_HEADER + "/static/image/" + i for i in file_name_list]
            ret_data = {"imageUrl": image_path_list}
            # 返回图片下载地址给客户端
            http_response(self, ERROR_CODE['200'], 200, ret_data)
        else:
            # 如果图片为空，返回图片为空错误信息
            logger.info("UploadFileHandle: image stream is empty")
            http_response(self, ERROR_CODE['2001'], 2001)
