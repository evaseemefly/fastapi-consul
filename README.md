# fastapi-consul
fastapi引入consul实现服务注册与发现

本demo用来演示在 `fastapi` 中引入 `consul`实现服务注册与服务发现。

![001](/docs/imgs/001.png)

```py
|___consul_client.py
    |____ ConsulRegisterServer # consul 服务注册类 只用来向 consul 注册指定服务
    |____ConsulExtractClient   # consul 订阅类(客户端类),客户端通过 服务名称 获取指定服务的地址信息
    |____ ConsulClient         # consul 实现consul的服务注册，与服务发现
|__ server_service.py # fastapi的逻辑，向consul服务注册
|__ main_client.py  # 服务发现并调用的示例
|__ main_service.py # 启动fastapi服务
```

ConsulClient 参考自: [ConsulFlask](https://gitee.com/aichinai/consul_flask/blob/master/ConsulFlask/consulclient.py)

基于 fastapi 的服务注册与发现参考: [consul-fastapi-microservice]([pace-noge/consul-fastapi-microservice: Microservice using fastapi and consul (github.com)](https://github.com/pace-noge/consul-fastapi-microservice))



### fastapi基于consul实现服务注册与发现的原理:

1. fastapi服务端通过consul实现注册服务(详见: server_service.py)

   *在fastapi startup 事件触发时，向consul注册当前服务(server_name)*

2. fastapi客户端通过consul获取指定 service-name 获取对应的注册服务节点

3. client -> consul (service-name) ->service url

4. service url + uri -> full_url

5. get/post ful_url -> 对应的地址获取结果

### consul的服务订阅大体原理:

![consul服务订阅示意图](/docs/imgs/002.png)
