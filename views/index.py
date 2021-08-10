#!/usr/bin/env python
# _*_coding:utf-8_*_
import tornado.web

class homedo(tornado.web.RequestHandler):


    def initialize(self,word1, word2):
        self.word1 = word1
        self.word2 = word2
        # print(self.word1)

    def get(self, *args, **kwargs):
        print(self.word1,self.word2)
        self.write('hello road')

class do_reverse(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        url = self.reverse_url('reverse_fixed')
        self.write("<a href='%s'>我们一起去反向解析</a>"%url)

class do_reverse1(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # url = self.reverse_url('reverse_fixed')
        self.write('hello11')

class re_receive(tornado.web.RequestHandler):
    def get(self,a,b,c, *args, **kwargs):   # 传入数据已接收，正则分组方法
        print(a+'-'+b+'-'+c)
        self.write('success')

class re_receive2(tornado.web.RequestHandler):
    def get(self,p1,p2,p3,*args, **kwargs):
        print(p1 + '-' + p2 + '-' + p3)
        self.write('success')

class post_test(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):  # self.get_query_argument()获取get请求
        self.render('postfile.html')
    def post(self, *args, **kwargs):
        name = self.get_body_argument('username')
        '''
        self.get_argument()兼容get post
        '''
        pwd = self.get_body_argument('passwd')   # 单个name值用，多个相同的name值则会取最后一个
        hobby = self.get_body_arguments('hobby')  # post请求的列表形式值（多个相同的name用）
        print(name,pwd,hobby)
        self.write('success post')