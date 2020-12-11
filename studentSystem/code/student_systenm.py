


import re


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
    说明:通过数字或↑↓方向键选择菜单
    """)


def main():
    """ 
        主函数入口
    """
    ctrl = True  # 标记是否退出系统
    while (ctrl):
        menu()
        option = input("请选择:")
        option_str = re.sub("\D","",option)
        if option_str in ['0','1','2','3','4','5','6','7',]:
            if int(option_str) == 0 :
                print("您已退出学生信息管理系统")
                break
            elif int(option_str) == 1 :
                pass
            elif int(option_str) == 2 :
                pass
            elif int(option_str) == 3 :
                pass
            elif int(option_str) == 4 :
                pass
            elif int(option_str) == 5 :
                pass
            elif int(option_str) == 6 :
                pass
            elif int(option_str) == 7 :
                pass

main()