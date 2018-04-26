from __future__ import unicode_literals
from .upload_views import (
    UploadFileHandle
)

urls = [
    # 从 /upload/file 过来的请求，将调用 upload_views 里面的 UploadFileHandle 类
    (r'file', UploadFileHandle)
]
