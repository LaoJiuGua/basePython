from enum import Flag
import re,os

filename = "F:/python/coding/basePython/studentSystem/file/student.txt"

def insert():
    """
        录入和保存学生信息
    """
    
    stdentList = []         # 临时保存学生的列表
    mark = True             # 是否继续田间
    while mark:
        id = input("请输入ID（如 1001）:")
        if not id:          # ID为空跳出循环
            break
        name = input("请输入名字:")
        if not name:        # 名字为空跳出循环
            break
        try:
            english = int(input("请输入英语成绩:"))
            python = int(input("请输入Python成绩:"))
            c = int(input("请输入C语言成绩:"))
        except :
            print("输入无效,不是整形数值.....请重新录入信息")
            continue
        # 将学生的信息保存到字典
        stdent = {'id':id,'name':name,'english':english,'python':python,'c':c,}
        stdentList.append(stdent)   # 将字典添加到列表内
        inputMark = input('是否继续添加？（y/n）:')
        if inputMark.lower() == 'y':
            continue
        else:
            break
    sava(stdentList)
    print('学生信息录入完毕！')

def sava(student):
    """
        保存文件
    """
    try:
        students_txt = open(filename,"a",encoding='gbk')
    except Exception as e:
        students_txt = open(filename,"w",encoding='gbk')
    for info in student:
        students_txt.write(str(info)+'\n')
    students_txt.close()

def show():
    """ 查找学生信息 """
    student_new = []
    if os.path.exists(filename):            # 判断文件是否存在
        with open(filename,'r') as rfile:   # 打开文件
            student_old = rfile.readlines()
        for list in student_old:
            student_new.append(eval(list))
        if student_new:
            show_student(student_new)
    else:
        print('暂未保存数据信息...')

def show_student(studentList):
    """将保存在列表中的学生信息显示出来"""

    if not studentList:     # 判断列表是否为空
        print("... 无数据信息！ ...")
        return 
    # 美化输出标题
    format_title = "{0:^4}|{1:^5}|{2:^6}|{3:^2}|{4:^2}|{5}"         
    print(format_title.format('ID','名字','英语成绩','Python成绩','C语言成绩','总成绩'))
    # 美化输出数据
    format_data = "{0}|{1:^5}|{2:^10}|{3:^10}|{4:^9}|{5:^2}"
    for info in studentList:
        print(
            format_data.format(info.get('id'),
                               info.get('name'),
                               str(info.get('english')),
                               str(info.get('python')),
                               str(info.get('c')),
                               str(info.get('english') + info.get('python') + 
                               info.get('c'))
        ))

def delete():
    """
        根据学生ID删除已存在的学生
    """

    mark = True  # 标记循环
    while mark:
        studentID = input("请输入要删除的学生ID:")
        if studentID is not "":                 # 判断输入的ID不为空
            if os.path.exists(filename):        # 判断文件是否存在
                with open(filename,"r",encoding="gbk") as rfile:    # 打开文件
                    student_old = rfile.readlines()                 # 读取全部内容
                    print(student_old)
            else:
                student_old = []  
            ifdel = False       # 标记是否删除
            if student_old:     # 如果存在学生信息
                with open(filename,'w',encoding="gbk") as wfile:    # 以写的形式打开文件
                    d ={}       # 定义空字典
                    for list in student_old:
                        d = dict(eval(list))    # 字符串转字典
                        print(d)
                        if d['id'] != studentID:
                            wfile.write(str(d)+"\n")    # 将一条学生信息写入文件
                        else:
                            ifdel = True        # 标记已经删除
                    if ifdel:
                        print('ID为 %s 的学生信息已经被删除...' % studentID)
                    else:
                            print('没有找到ID为 %s 的学生信息...' % studentID)
            else:
                print('无学生信息...')
                break       # 跳出循环
            show()
        inputMark = input("是否继续删除? （y/n）:")
        if inputMark.lower() == "y":
            continue    # 继续删除
        else:
            break       # 退出删除学生信息功能

def search():
    """
        查找学生信息
    """
    mark  = True
    student_li = []     # 保存查询学生信息的列表
    while mark:
        id = ''             # 初始化id为空
        name = ''           # 初始化name为空
        if os.path.exists(filename):            # 判断文件是否存在
            mode = input("按ID查询输入1,按名字查询输入2:")
            if mode == "1":                     # 按照id查询
                id = input("请输入查询学生的ID:")
            elif mode == "2":                   # 按照name查询
                name = input("请输入查询学生的名字:")
            else:
                print("输入有误,请重新输入!")
                continue
            with open(filename,"r",encoding="gbk") as f:        # 打开文件
                students = f.readlines()                        # 列表形式读取文件
                for student in students:                        # 循环文件列表
                    d = dict(eval(student))                     # 字符串转字典
                    if id is not "":
                        if d['id'] == id:                       # 判断循环的单个字典id是否等于输入的id
                            student_li.append(d)                # 查询到的信息保存到列表内
                    if name is not "":
                        if d['name'] == name:                   # 判断循环的单个字典name是否等于输入的name
                            student_li.append(d)                # 查询到的信息保存到列表内
            show_student(student_li)                            # 将查询到的美化输出
            student_li.clear()                                  # 清空列表
            # 判断是否继续查询
            inputMark = input("是否继续查询(y/n):")
            if inputMark.lower() == "y":
                continue
            elif inputMark.lower() == "n":
                break
        else:
            print("未找到学生信息...")
            return

def total():
    if os.path.exists(filename):
        with open(filename,"r",encoding="gbk") as f:
            students = f.readlines()
        if students:
            print("一共有%d个学生" % len(students))
        else:
           print("还没有录入学生信息！")
    else:
        print("未查询到数据！") 

def modify():
    """
        修改学生信息
    """
    show()                          # 显示出学生信息
    if os.path.exists(filename):    # 判断文件是否存在
        with open(filename,"r",encoding='gbk') as f:
            student_olds = f.readlines()    # 按列表取出数据
    else:
        print('未找到数据...')
    id = input("请输入要修改学生的ID:")
    with open(filename,"w",encoding='gbk') as f:    # 按照写方式打开文件
        for student in student_olds:   
            d = dict(eval(student))         # 字符串转成字典
            if d['id'] == id:               
                print("找到学生请修改！")
                while True:
                    try:
                        # 在字典内按照键修改值
                        d['name'] = input("请输入要修改学生的名字:")
                        d['english'] = int(input("请输入要修改学生的英语成绩:"))
                        d['python'] = int(input("请输入要修改学生的Python成绩:"))
                        d['c'] = int(input("请输入要修改学生的C语言成绩:"))
                    except Exception:
                        print("输入有误,请从新输入！")
                    else:
                        break
                students_new = str(d)       # 把字典转成字符串
                f.write(students_new + '\n')      # 改过的新数据保存到文件内
            else:
                f.write(student)            # 未修改过的文件保存到文件内
        mark = input("是否继续修改？（y/n）")
        if mark.lower() == 'y':             # 判断是否继续
            modify()
        return

def sort():
    show()
    if os.path.exists(filename):
        with open(filename,"r",encoding="gbk") as f:
            students = f.readlines()
    else:
        print('无数据信息....')
    student_li = []
    for studen in students:
        d = dict(eval(studen))
        student_li.append(d)
    s = input('请选择(升序:1/降序:2): ')      # 选择升序或者降序
    if s == "1":
        is_reverse = False                  # 升序给is_reverse False值
    elif s == "2":
        is_reverse = True                   # 降序给is_reverse True值
    else:
        print("输入错误,请重新输入！")
        sort()
    so_new = input("请选择排序方式(english:1 / Python:2 / C语言:3 / 总成绩:4)：")   # 选择排序方式
    # 使用内置的排序方法，reverse是控制升序或者降序
    if so_new == "1":
        student_li.sort(key=lambda x:x["english"], reverse=is_reverse)    
    elif so_new == "2":
        student_li.sort(key=lambda x:x["python"], reverse=is_reverse)
    elif so_new == "3":
        student_li.sort(key=lambda x:x["c"], reverse=is_reverse)
    elif so_new == "4":
        student_li.sort(key=lambda x:x["english"] + x["python"] + x["c"] , reverse=is_reverse)
    else:
        print('输入错误,请重新输入...')
        sort()
    # 显示出排序的数据
    show_student(student_li)

def menu():
    """
       输入菜单 
    """
    print("""
    -----------------------------------------------------------
                                                             
              =========== 功能菜单 ===========                
                                                             
               1 录入学生信息                                  
               2 查找学生信息                                   
               3 删除学生信息
               4 修改学生信息
               5 排序
               6 统计学生总人数
               7 显示所有学生信息
               0 退出系统
               =========== 感谢使用 ===========
               说明:通过数字选择菜单
    
    ------------------------------------------------------------
    """)

def main():
    """ 
        主函数入口
    """
    while True:
        menu()
        option = input("请选择:")
        option_str = re.sub("\D","",option)
        if option_str in ['0','1','2','3','4','5','6','7',]:

            if int(option_str) == 0 :   # 退出学生系统
                print("您已退出学生信息管理系统")
                break
            elif int(option_str) == 1 :  # 录入学生信息
                insert()
            elif int(option_str) == 2 :   # 查找学生信息
                search()
            elif int(option_str) == 3 :    # 删除学生信息
                delete()
            elif int(option_str) == 4 :     # 修改学生信息
                modify()
            elif int(option_str) == 5 :     # 排序
                sort()
            elif int(option_str) == 6 :     # 统计人数
                total()
            elif int(option_str) == 7 :     # 显示所有学生信息
                show()

main()