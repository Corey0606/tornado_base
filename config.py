#!/usr/bin/env python
# _*_coding:utf-8_*_
# port
import os
BASE_DIR = os.path.dirname(__file__)
options = {
    'port': 4010
}
# settings
settings = {
    'staic_path':os.path.join(BASE_DIR,'static'),  # 没有上传文件的path
    'template_path':os.path.join( BASE_DIR,'templates'),
    # 'debug':True # 有错改正以后需重启，默认为False，一般不用他，用autoreload
    # 'autoreload': True   # 有错改正后自动重启
}