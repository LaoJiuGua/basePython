"""
    统计三国演义name.txt中哥哥英雄出现的次数，和weapon.txt中的武器出现次数
"""



f = open('./session4/file/name.txt','r+')
resp = f.read()
names = resp.split("|")

f1 = open('./session4/file/weapon.txt','r+',encoding="utf-8")
resp = f1.readlines()
weapons = [i.strip() for i in resp if i.strip() != ""]

f3 = open('./session4/file/sanguo_utf8.txt','r+',encoding="utf8")
context = f3.read()

times = []
for name in names:
    t = context.count(name)
    times.append(t)
print(list(zip(names,times)))

times1 = []

for weapon in weapons:
    t = context.count(weapon)
    times1.append(t)
print(list(zip(weapons,times1)))


#  使用pyecharts绘制柱状图

# 导入柱状图-Bar
from pyecharts.charts import Bar

bar = Bar()
bar1 = Bar()
# 添加柱状图的数据及配置项
bar.add_xaxis(names)
bar.add_yaxis("名字出现的次数",times)
bar1.add_xaxis(weapons)
bar1.add_yaxis("武器出现的次数",times1)

# 生成本地文件（默认为.html文件）
bar.render('anmes.html')
bar1.render('weapons.html')