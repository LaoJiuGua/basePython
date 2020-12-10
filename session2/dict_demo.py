'''
    接收用户输入的年月日，判断用户的生肖和星座并统计人数
    鼠牛虎兔龙蛇马羊猴鸡狗猪
    ("水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","摩羯座")
    ((1,20),(2,18),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))
'''
chinese_str = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
zodiac = ("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
zodiac_days = ((1,20),(2,18),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))

dict_sum = {
    "shengxiao":{
        "鼠":0,
        "牛":0,
        "虎":0,
        "兔":0,
        "龙":0,
        "蛇":0,
        "马":0,
        "羊":0,
        "猴":0,
        "鸡":0,
        "猪":0
    },
    "xingzuo":{
        "摩羯座":0,
        "水瓶座":0,
        "双鱼座":0,
        "白羊座":0,
        "金牛座":0,
        "双子座":0,
        "巨蟹座":0,
        "狮子座":0,
        "处女座":0,
        "天秤座":0,
        "天蝎座":0,
        "射手座":0
    }
    
    }
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
    dict_sum["shengxiao"][chinese_str[zodiac_nuw]] += 1
    dict_sum["xingzuo"][zodiac[index]] += 1
    

    new = int(input("请输入命令【0】退出/【1】继续"))
    if new == 0:
        print("""
        ================================
                非常感谢为您服务
        ================================
        """)
        for i,k in dict_sum["shengxiao"].items():
            print('属"{}"的有{}位'.format(i,k))
            print()
        print("========================")
        for i,k in dict_sum["xingzuo"].items():
            print('"{}"的有{}位'.format(i,k))
            print()
        print("========================")
        break
    continue