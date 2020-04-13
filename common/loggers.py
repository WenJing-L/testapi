import logging,time,os

class Logger():

    def __init__(self,logger):
        self.log=logging.getLogger(logger)
        self.log.setLevel(logging.INFO)

        tm=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        path=os.path.abspath(os.path.dirname('.'))+'//logs//'+tm+'.log'
        file=logging.FileHandler(path)
        file.setLevel(logging.INFO)

        control=logging.StreamHandler()
        control.setLevel(logging.INFO)

        formatter=logging.Formatter('%(asctime)s-%(name)s-%(Levelname)s-%(message)s')
        file.setFormatter(formatter)
        control.setFormatter(formatter)

        self.log.addHandler(file)
        self.log.addHandler(control)

    def getlog(self):
        return self.log