import  pytest,requests
from common.commonData import CommonData
from util.HttpUtil import HttpUtil
http=HttpUtil()


@pytest.fixture(scope='session',autouse=True)  #session适用于每一次会话，autouse自动

def login():
    pay_load = {"loginId":"20171405139","password":"123456","orgId":10}
    path =CommonData.host+'api/auth/login'
    resp=http.http.post(path,pay_load)
    http.printresp(resp)
    CommonData.token=resp.json()['data']['auth_token']
    print('登陆成功')


