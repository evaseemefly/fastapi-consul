# -*- coding: utf-8 -*-
from consul_client import ConsulClient
import requests


# 请求rest api 实例
class HttpClient:
    # 指定consul 服务的主机，端口，以及所要请求的应用名
    def __init__(self, consulhost, consulport, appname):
        self.consulhost = consulhost
        self.consulport = consulport
        self.appname = appname
        self.consulclient = ConsulClient(host=self.consulhost, port=self.consulport)

    def request(self):
        sss = self.consulclient.get_service(self.appname)
        if sss != None:
            host, port = sss
            # TODO:[*] 23-11-02
            # requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=8500): Max retries exceeded with url: /v1/catalog/service/student (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x00000202BED0CBC8>: Failed to establish a new connection: [WinError 10061] 由于目标计算机积极拒绝，无法连接。'))
            scrapyMessage = requests.get("http://" + host + ":" + str(port) + "/" + self.appname)
            print("返回：", scrapyMessage)
            return scrapyMessage
        else:
            print("随机选取节点为空")
            return "没有可用的服务节点"
