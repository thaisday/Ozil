# coding=utf-8
__author__ = 'KiddoMa'

import tornado
from dao import serversDao


class selectServers(tornado.web.RequestHandler):
    # 跳转到选择服务器的页面
    def get(self):
        self.render('selectServers.html')


class configServers(tornado.web.RequestHandler):
    # 跳转到配置服务器的页面
    def get(self):
        self.render('configServers.html')




class servers(tornado.web.RequestHandler):
    #获取servers的信息
    def get(self):
        try:
            serversList = serversDao.getServersList()
            self.write(serversList)
        except Exception as e:
            print e

    # 保存servers的信息
    def post(self):
        serversList = self.get_argument('data')
        serversDao.setServersList(serversList)
