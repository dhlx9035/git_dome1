import pymysql
import login1
import room
import stu
import lesson
# 学号  姓名  性别  联系电话  qq  班级  班主任
student_xx={}#学生信息（中转站）
# student_qq=[]#学生请求   修改项，修改内容，修改人（学号）
def a():
    return
def student_xt():
    print('————————黎明学子：{}，欢迎进入————————'.format(student_xx['姓名']))
    print('以下是您的基本信息：\n学号：{0}\n联系电话：{3}\nqq：{4}\n班级：{5}\n班主任：{6}'.format(student_xx['学号'],student_xx['姓名'],student_xx['性别'],student_xx['联系电话'],student_xx['qq'],student_xx['班级'],student_xx['班主任'],))
    while True:
        xz = {
            '1': stu.chakan_self,
            '2': lesson.kbck_student,
            '3': stu.xg_qq,
            '4': lesson.stu_kb_xinxi,
            '5': stu.student_cjck,
        }
        choose = input('\n请选择相应操作：\n1、查看自我信息\n2、查看课表\n3、修改自我数据\n4、查看学科科目信息\n5、查看成绩\n6、退出\n7、查找空闲教室')
        xz.get(choose, a)()
        if choose =='6':
            break
        elif choose=='7':
            room.room_spare()
            room.room_deal1()
