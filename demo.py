import requests


# 模拟get请求
# response = requests.get('http://www.baidu.com')
# print(response.text)

# 模拟一个post的登录请求
# pay_load = {"loginId": "20171405139", "password": "123456", "orgId": 10}
# response = requests.post('http://acv3.learn.it101.live/api/auth/login', pay_load)
# data = response.json()
# print(data)
# assert data['ok'] == True

# 模拟一个get的请求，添加一个请求头
# headers = {'ac-token': 'sQ6H0O8ZFsYjWX9z-uwH7jcI0H3v0ihI'}
# response = requests.get('http://acv3.learn.it101.live/api/courses/v3/trends', headers=headers)
# data = response.json()
# print(data)
# assert data['ok'] == True

# 打印HTTP响应消息的函数
def printResponse(response):
    print('\n\n---------HTTP response *begin-------')
    print(response.status_code)  # 获取状态码

    # 获取所有响应头相关的所有信息 response.headers.items()
    for k, v in response.headers.items():  # 遍历输出键值对
        print(f'{k}:{v}')
    print(' ')

    print(response.content.decode('utf8'))   #获取响应实体，相当于上边的print(data)
    print('\n\n---------HTTP response *end-------')


# 使用session
session = requests.session()
# 登录
pay_load = {"loginId": "20171405139", "password": "123456", "orgId": 10}
response = session.post('http://acv3.learn.it101.live/api/auth/login', pay_load)
printResponse(response)
# 获取最近学习动态
response = session.get('http://acv3.learn.it101.live/api/courses/v3/trends')
printResponse(response)
# 获取课程列表
response = session.get('http://acv3.learn.it101.live/api/courses/v3/myCourses')
printResponse(response)
# 获取最近学习小节
response = session.get('http://acv3.learn.it101.live/api/learning/v3/194/recentLesson')
printResponse(response)
# 获取课程角色
response = session.get('http://acv3.learn.it101.live/api/courses/v3/194/courseRole/')
printResponse(response)
# 获取课程详情
response = session.get('http://acv3.learn.it101.live/api/courses/v3/194/detail')
printResponse(response)
# 获取菜单
response = session.get('http://acv3.learn.it101.live/api/courses/v3/194/modules/')
printResponse(response)
# 获取大纲
response = session.get('http://acv3.learn.it101.live/api/courses/v3/194/chapters')
printResponse(response)
# 获取章节
response = session.get('http://acv3.learn.it101.live/api/courses/v3/194/chapters')
printResponse(response)
# 获取小节详情
response = session.get('http://acv3.learn.it101.live/api/courses/v3/213/statistics/teacher/lesson')
printResponse(response)
# 记录时间
pay_load = {"courseId":"213","lessonId":"qi-dong-firefox-liu-lan-qi","duration":9801,"type":"lesson","beginAt":1586078230592,"url":"http://acv3.learn.it101.live/learning/213/qi-dong-firefox-liu-lan-qi/"}
response = session.post('http://acv3.learn.it101.live/api/record/recordStudyTime/', pay_load)
printResponse(response)
# 运行
pay_load = {"courseId":"213","lessonId":"di-yi-ge-cheng-xu","exerciseId":"5e6338098e1a9404f85e3b62","language":"python","code":"from selenium import webdriver\n\n# 请在Chrome方法中，传入驱动的字符串路径\ndriver = webdriver.Chrome(\"d:/webdrivers/chromedriver.exe\")\ndriver.get(\"https://www.python.org\")\nassert \"Python\" in driver.title","stdin":""}
response = session.post('http://acv3.learn.it101.live/api/learning/v3/run', pay_load)
printResponse(response)
# 提交答案
pay_load = {"courseId":"213","lessonId":"di-yi-ge-cheng-xu","exerciseType":"code","exerciseId":"5e6338098e1a9404f85e3b62","solution":"from selenium import webdriver\n\n# 请在Chrome方法中，传入驱动的字符串路径\ndriver = webdriver.Chrome(\"d:/webdrivers/chromedriver.exe\")\ndriver.get(\"https://www.python.org\")\nassert \"Python\" in driver.title"}
response = session.post('http://acv3.learn.it101.live/api/learning/v3/judge', pay_load)
printResponse(response)

# 退出登录
response = session.get('http://acv3.learn.it101.live/api/auth/logout')
printResponse(response)