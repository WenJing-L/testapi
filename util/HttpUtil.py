import requests, json
from common.commonData import CommonData


# 打开代理  键值对
class HttpUtil():  # 封装了对应的get方法和post方法   请求与发送的公共类

    def __init__(self):
        self.http = requests.session()  # 创建一个会话
        self.headers = {'Content-Type': 'application/json; charset=utf-8'}

    # get方法
    def get(self, path):
        host = CommonData.host + path
        self.headers['token'] = CommonData.token
        resp = self.http.get(url=host, headers=self.headers)
        try:
            assert resp.status_code == 200
        except:
            print(resp.json()['ok'])
        self.printresp(resp)
        resp_json = resp.text
        resp_dict = json.loads(resp_json)  # 装化成python格式
        return resp_dict

    # post方法
    def post(self, path, data):
        # proxies = CommonData.proxies  # 获取全局变量proxies代理
        host = CommonData.host + path  # 获取全局变量host路径
        self.headers['token'] = CommonData.token
        data_json = json.dump(data)  # 将python 格式转为json双引号格式
        resp = requests.post(url=host,
                              data=data_json,
                              headers=self.headers)
        assert resp.status_code == 200
        resp_json = resp.text
        print(resp_json)
        resp_dict = json.loads(resp_json)  # 装化成python格式
        return resp_dict

    def printresp(self,resp):
        print('\n\n---------HTTP response *begin-------')
        print(resp.status_code)
        print(resp.json()['ok'])
        for k,v in resp.headers.items():
            print(f'{k}:{v}')
        print(resp.content.decode('UTF-8'))   # 输出返回实体
        print('\n\n---------HTTP response *end-------')
