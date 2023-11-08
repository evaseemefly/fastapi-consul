import logging
from typing import Optional

import consul
import requests

from config import Config
from consul_client import ConsulClient, ConsulExtractClient


def client_start():
    # client = HttpClient('127.5.9.79', '8500', 'student-service')  # 测试用
    # client.request()
    # consul_client = ConsulClient('127.5.9.79', '8500')
    # consul_client.getService('student-service')

    c = consul.Consul(host='128.5.9.79', port=8500)
    # agent是consul的核心，用来维护成员的重要信息
    agent = c.agent
    services = agent.services()
    # 根据注册的服务名称获取对应的服务信息
    service_name: str = 'student-service'
    target_serivce = services.get(service_name)
    # 从当前心跳检测通过的服务中心获取指定的服务节点集合
    _, nodes = c.health.service(service=service_name, passing=True)
    # 随便取出第一个 nodes -> node 获取地址与port
    random_node = nodes[0]
    random_service = random_node.get('Service')
    address = random_service['Address']
    port = random_service['Port']
    # 根据 address+port 获取服务url地址
    # eg: 127.0.0.1:8000
    url = f'http://{address}:{port}'
    full_url = f'{url}/health'

    client = requests.session()
    headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive',
               'buc-auth-token': 'default.buc-auth-token'}
    # 使用此种方式相当于是通过 consul 获取对应服务的实际url地址，并直接访问该地址，是否可以通过 ->consul 直接访问该服务，而不通过获取后的url而访问
    response = client.get(url=full_url, headers=headers)

    print(response.text)
    # target_serivce = json.loads(target_serivce_str)
    pass


if __name__ == '__main__':
    # server = HttpServer('127.0.0.1', 8000, '128.5.9.79', 8500, 'student-service')
    # server.startServer()
    client_start()
    # 尝试使用 ConsulExtractClient
    consul_extract = ConsulExtractClient('student-service')
    test_res = consul_extract.get('/school/', params={'school_id': 1})

    logging.warning(f'获取结果:"/health":{test_res}')
    pass
