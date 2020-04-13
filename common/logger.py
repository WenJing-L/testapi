import logging,time,os

class Logger():
    def __init__(self,logname):
        self.log=logging.getLogger(logname)
        self.log.setLevel(logging.INFO)
        tm =time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

        path=os.path.abspath(os.path.dirname('.'))+'//logs//'+tm+'.log'    #当前目录的上一级目录
        file=logging.FileHandler(path)
        file.setLevel(logging.INFO)

        controltext=logging.StreamHandler()
        controltext.setLevel(logging.INFO)

        formatter =logging.Formatter('%(asctime)s-%(name)s-%(levername)s-%(message)s')
        file.setFormatter(formatter)
        controltext.setFormatter(formatter)

        self.log.addHandler(file)
        self.log.addHandler(controltext)
    def getlog(self):
        return self.log