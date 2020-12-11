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
    print(1)
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

def menu():
    """
       输入菜单 
    """
    print("""
    =========== 功能菜单 ===========

    1 录入学生信息
    2 查找学生信息
    3 删除学生信息
    4 修改学生信息
    5 排序
    6 统计学生总人数
    7 显示所有学的信息
    0 退出系统
    =========== 感谢使用 ===========
    说明:通过数字选择菜单
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
            elif int(option_str) == 1 :  
                insert()
            elif int(option_str) == 2 :
                show()
            elif int(option_str) == 3 :
                delete()
            elif int(option_str) == 4 :
                pass
            elif int(option_str) == 5 :
                pass
            elif int(option_str) == 6 :
                pass
            elif int(option_str) == 7 :
                pass

main()