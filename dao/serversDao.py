# coding=utf-8
__author__ = 'KiddoMa'

import json

#获取选择服务器的列表
def getServersList():
    try:
        fp = open('./config/servers.json','r')
        s = json.load(fp)
        return s
    except Exception as e:
        print e
    finally:
        fp.close()

#保存选择服务器的结果
def setServersList(serversList):
    try:
        fp = open('./config/servers.json','w')
        fp.write(serversList)
    except Exception as e:
        print e


if __name__ == '__main__':
    serverList = getServersList()
    print serverList