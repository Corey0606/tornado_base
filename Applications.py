#!/usr/bin/env python
# _*_coding:utf-8_*_
import tornado.web
import views.index
import config
# url


class App(tornado.web.Application):
    def __init__(self):
        handles = [
            ('/road',views.index.homedo,{'word1':'word1','word2':'word2'}),  # 后面字典为参数传进view 可以去除
            tornado.web.url(r'/reverse1',views.index.do_reverse1,name='reverse_fixed'),  # 反向解析以name准（不能用元组形式，只能url形式），改代码不变
            ('/test',views.index.do_reverse),
            (r'/nb/(\w+)/(\w+)/(\w+)',views.index.re_receive),  # 正则分组从url里传参数
            (r'/sb/(?P<p1>\w+)/(?P<p3>\w+)/(?P<p2>\w+)',views.index.re_receive2),  # 正则参数固定位置传入
            (r'/post1',views.index.post_test)


        ]
        '''
                   ('/data',views.index.homedo,{'word1':word1,'word2':word2})
                   '''
        super(App,self).__init__(handles, **config.settings)

