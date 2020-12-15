'''
    类方法
    
'''

class  People:
    country = 'china'

    # 类方法  通过cls作为第一参数  代表这是一个类  通过cls去访问类属性
    @classmethod
    def getCountry(cls):
        return cls.country

    @classmethod
    def setCountry(cls,country):
        cls.country = country
        

P = People()
print(P.getCountry())
P.setCountry('japan')
print(P.getCountry())
