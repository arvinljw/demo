import json
import os


def http_response(self, msg, code, data=None, ):
    self.write(json.dumps({"data": data, "msg": msg, "code": code}))


def save_files(file_metas, in_rel_path, type='image'):
    file_name_list = []
    for meta in file_metas:
        file_name = meta['filename']
        file_path = os.path.join(in_rel_path, file_name)
        file_name_list.append(file_name)
        # save image as binary
        with open(file_path, 'wb') as up:
            up.write(meta['body'])
    return file_name_list
