# chinese_strs = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
# chinese_str_li = [0,0,0,0,0,0,0,0,0,0,0,0]
zodiacs = ("摩羯座","水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座")
zodiac_days = ((1,20),(2,18),(3,21),(4,20),(5,21),(6,22),(7,23),(8,23),(9,23),(10,24),(11,23),(12,22))


# num = lambda arg1,arg2:arg1+arg2
# print(num(3,2))

month = int(input("请输入您的出生月份:"))
day = int(input("请输入您的出生日:"))

result = filter(lambda x:x<(month,day),zodiac_days)
resp = zodiacs[len(list(result))]
print(resp)