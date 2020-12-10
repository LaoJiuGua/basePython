'''
    接收用户的输入的年份,判断用户的生生肖
    鼠牛虎兔龙蛇马羊猴鸡狗猪
'''

chinese_str = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
str_to_int_year = int(input("请输入您的出生年份:"))

zodiac_nuw = str_to_int_year % 12
print("您的生肖是{}".format(chinese_str[zodiac_nuw]))


'''
    接收用户输入的年月日，判断用户的生肖和星座
'''