'''
    类的定义
'''
class  Car:
    def __init__(self,wheelNum,color):
        self.wheelNum = wheelNum
        self.color = color

    # 方法
    def getCarInfo(self):
        print("车轮子个数:%d，颜色%s"%(self.wheelNum,self.color))
    # 移动
    def move(self):
        print('车子正在移动....')
    # 鸣笛
    def toot(self):
        print('车子在鸣笛..嘟嘟。。')

BMW = Car(4,"黑色")
# BMW.color = "红色"
BMW.move()
BMW.toot()
BMW.getCarInfo()
print(BMW.color)