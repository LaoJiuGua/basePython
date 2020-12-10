import keyword
# print(keyword.kwlist)

def one():
    new1 = input("请输入第一个数字：")
    new2 = input("请输入第二个数字：")
    return int(new1)+int(new2)
# print(one())

def tow():
    user = "root"
    password = "123456"
    while True:
        print("+++++++++++++++++++++++++++++++++++++++")
        print("+             欢迎进入到身份认证系统V1.0")
        print("+1.登录")
        print("+2.退出")
        print("+3.认证")
        print("+4.修改密码")
        print("+++++++++++++++++++++++++++++++++++++++")

        new = int(input("请输入编号选择功能："))

        if new == 1:
            my_user = input("请输入用户名：")
            my_password = input("请输入密码：")
            if my_user == user and my_password == password:
                print("登录成功")
            else:
                print("账号和或密码错误")
        elif new == 2:
            print('退出成功')
            return 
        elif new == 3:
            my_authName = input("请输入名字：")
            my_authId = input("请输入身份证ID：")
            print("用户{0},您已经认证成功".format(user))
        elif new == 4:
            old_password = input("请输入旧密码：")
            if old_password == password:
                password = input("请输入新密码：")
                print("修改成功")
            else:
                print("旧密码不正确")

# tow()

def three():
    name = input("请输入名字：")
    QQ = input("请输入QQ：")
    ID = input("请输入手机号：")
    addr = input("请输入地址：")
    print("""
    ====================================
    姓名:{0}
    Q Q:{1}
    手机号:{2}
    公司地址:{3}
    ====================================
    """.format(name,QQ,ID,addr))   
    
three()     

