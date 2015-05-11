# coding=utf-8
__author__ = 'KiddoMa'

import tornado

class index(tornado.web.RequestHandler):
    #定义首页的处理跳转到index.html页面
    def get(self):
        self.render("index.html")


