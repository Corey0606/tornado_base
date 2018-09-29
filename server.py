#!/usr/bin/env python
# _*_coding:utf-8_*_
import tornado.ioloop
import tornado.web
import config
import Applications




if __name__ == '__main__':
    app = Applications.App()
    app.listen(config.options['port'])
    tornado.ioloop.IOLoop.current().start()