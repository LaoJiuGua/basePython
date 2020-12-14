'''
    id()
    __str__
'''

class Car:
    def __init__(self,name,color="red",wheelNum=4):
        self.__name = name
        self.__color = color
        self.__wheelNum = wheelNum

    def __move(self):
        print("%s颜色的汽车在行使————"%self.__color)
    
    def __str__(self):
        return "我是一辆%s汽车,颜色是%s,我有%d轮子"%(self.__name,self.__color,self.__wheelNum)
    
    def get_move(self):
        self.__move()
    
    def __del__(self):
        print("%s汽车爆炸了————"%self.__name)


BWM = Car(name='宝马',color="blue",wheelNum=4)
BWM.get_move()
print(BWM)

Audio = Car(name="奥迪")
print(Audio)
Audio.get_move()

del BWM