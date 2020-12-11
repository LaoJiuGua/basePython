'''
    接收用户输入的年月日，判断用户的生肖和星座并统计人数
    鼠牛虎兔龙蛇马羊猴鸡狗猪
    ("水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","摩羯座")
    ((1,20),(2,18),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
'''
chinese_strs = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# chinese_str_li = [0,0,0,0,0,0,0,0,0,0,0,0]
zodiacs = ("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
zodiac_days = ((1,20),(2,18),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))



dict_chinese_strs = {chinese_str:0 for chinese_str in chinese_strs} 
dict_zodiacs = {zodiacs:0 for zodiacs in zodiacs} 
# dict_chinese_str = {k:chinese_str_li[i] for i,k in enumerate(chinese_str)}
# dict_zodiac = {k:chinese_str_li[i] for i,k in enumerate(zodiac)}


while True:
    year = int(input("请输入您的出生年份:"))
    month = int(input("请输入您的出生月份:"))
    day = int(input("请输入您的出生日:"))

    zodiac_nuw = year % 12
    print(zodiac_nuw)

    # while 循环
    index = 0
    while  (month,day) > zodiac_days[index] :
        if (month,day) > zodiac_days[-1]:
            break
        index += 1
    print("您的生肖是{},您的星座是{}".format(chinese_strs[zodiac_nuw],zodiacs[index]))
    dict_chinese_strs[chinese_strs[zodiac_nuw]] += 1
    dict_zodiacs[zodiacs[index]] += 1
    print(dict_chinese_strs)
    print(dict_zodiacs)

    new = int(input("请输入命令【0】退出/【1】继续"))
    if new == 0:
        print("""
        ================================
                非常感谢为您服务
        ================================
        """)
        break