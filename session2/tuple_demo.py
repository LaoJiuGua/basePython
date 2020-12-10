'''
    接收用户输入的月日，判断用户的星座
    ("水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","摩羯座")
    ((1,20),(2,18),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
'''
# zodiac = ("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
# zodiac_days = ((1,20),(2,18),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
# print(int(zodiac_days[0][0])-1)

# month = int(input("请输入您的出生月份:"))
# day = int(input("请输入您的出生日:"))


# index = 0
# for 循环
# for zodiac_day in zodiac_days:
#     if ((month,day)) > zodiac_days[-1]:
#         index = 0
#     elif((month,day)) > zodiac_day:
#         index =+ 1

# while 循环
# while  (month,day) > zodiac_days[index] :
#     if (month,day) > zodiac_days[-1]:
#         break
#     index += 1

# print(zodiac[index])


'''
    接收用户输入的年月日，判断用户的生肖和星座
    鼠牛虎兔龙蛇马羊猴鸡狗猪
    ("水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","摩羯座")
    ((1,20),(2,18),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
'''

chinese_str = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
zodiac = ("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
zodiac_days = ((1,20),(2,18),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
# while True:
    # year = int(input("请输入您的出生年份:"))
    # month = int(input("请输入您的出生月份:"))
    # day = int(input("请输入您的出生日:"))

    # zodiac_nuw = year % 12

    # # while 循环
    # index = 0
    # while  (month,day) > zodiac_days[index] :
    #     if (month,day) > zodiac_days[-1]:
    #         break
    #     index += 1
    # print("您的生肖是{},您的星座是{}".format(chinese_str[zodiac_nuw],zodiac[index]))

while True:
    year = int(input("请输入您的出生年份:"))
    month = int(input("请输入您的出生月份:"))
    day = int(input("请输入您的出生日:"))

    zodiac_nuw = year % 12

    # while 循环
    index = 0
    while  (month,day) > zodiac_days[index] :
        if (month,day) > zodiac_days[-1]:
            break
        index += 1
    print("您的生肖是{},您的星座是{}".format(chinese_str[zodiac_nuw],zodiac[index]))

    new = int(input("请输入命令【0】退出/【1】继续"))
    if new == 0:
        print("退出成功！")
        break
    continue