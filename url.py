# coding=utf-8
__author__ = 'KiddoMa'

#定义URL的映射

import sys
from handler.servers.serversHandler import *
from handler.index.indexHandler import *

reload(sys)

url = [
    (r'/', index),
    (r'/selectServers',selectServers),
    (r'/configServers',configServers),
    (r'/servers',servers),
]