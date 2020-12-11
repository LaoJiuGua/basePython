"""
    读取name.txt文件中的名字 转换成列表
"""



f = open('./session4/file/name.txt','r+')
resp = f.read()
names = resp.split("|")
for name in names:
    print(name)


"""
    读取weapon.txt中的武器
"""
f1 = open('./session4/file/weapon.txt','r+',encoding="utf-8")
resp = f1.readlines()
print([i.strip() for i in resp if i.strip() != ""])
for i in resp:
    print(i.strip())
# names = resp.split("|")
# for name in names:
#     print(name)



"""
    读取sanguo.txt中的武器
"""
# f2 = open('./session4/file/sanguo.txt','r+',encoding="gb18030")
# resp = f1.read()
# print(resp)

f3 = open('./session4/file/sanguo_utf8.txt','r+',encoding="utf8")
resp = f3.read()
print(resp)
