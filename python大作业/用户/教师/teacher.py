import grade
import lesson
import room
import stu
import tea
stu_xg_qq=[]#修改人学号  修改项  修改内容  班主任
teacher_xx={}#教师信息（中转站） 教师编号  姓名  教学科目  教学班级  班级——教师联系
teacher_xinxi=[]#教师所有信息 包含中转站信息，为成绩的相关方法做判断  [{ 教师编号  姓名  教学科目  教学班级  班级——教师联系},{}]
teacher_qq=[]#教师请求   修改项，修改内容，修改人（教师编号）
def a():
    return
def teacher_xt():
    print('————————黎明教师：{}，欢迎进入————————'.format(teacher_xx['姓名']))
    print('以下是您的基本信息：\n教师编号：{0}\n姓名：{1}\n教学科目：{2}\n教学班级：{3}\n联系电话：{4}\n班级——教师联系：{5}'.format(teacher_xx['教师编号'],teacher_xx['姓名'],teacher_xx['教学科目'],teacher_xx['教学班级'],teacher_xx['联系电话'],teacher_xx['班级——教师联系']))
    while True:
        xz = {
            '1': teacher_room,
            '2': teacher_lesson,
            '3': teacher_stu_gl,
            '5': teacher_grade_gl,#成绩管理
        }
        choose = input('\n您可以进行相应操作：\n1、进入个人空间\n2、课表操作\n3、学生管理\n4、查询空闲教室\n5、成绩管理\n6、退出\n')
        xz.get(choose, a)()
        if choose=='4':
            room.room_spare()
            room.room_deal1()
        if choose =='6':
            break
#教师课程操作
def teacher_lesson():
    print('\n进入  -教师——课表-  操作...')
    while True:
        xz = {
            '1': lesson.kbck_admin,
            '2': lesson.kb_add,
            '3': lesson.kb_del,
        }
        choose = input('\n您可以进行相应操作：\n1、课表查询\n2、增加课程\n3、删除课程（单位时间课程）\n6、退出\n')
        xz.get(choose, a)()
        if choose =='6':
            break
#教师个人空间
def teacher_room():
    print('----  {}  -----个人中心'.format(teacher_xx['姓名']))
    while True:
        xz = {
            '1': tea.chakan_self,
            '2': tea.xg_qq,
        }
        choose = input('\n您可以进行相应操作：\n1、查看自我信息\n2、修改自我数据\n6、退出\n')
        xz.get(choose, a)()
        if choose =='6':
            break
#学生管理
def teacher_stu_gl():
    print('{}教师，你可以对{}中的学生进行操作'.format(teacher_xx['姓名'],teacher_xx['教学班级']))
    while True:
        xz = {
            '1': stu.chakan,#有时间改为查询关于学生的所有数据
            '2': stu.chakan_gr,#有时间改为查询关于学生的所有数据
            '3': stu.stu_gl,#√学生信息管理
            '4': tea.stu_qq_deal,#√
        }
        choose = input('\n您可以进行相应操作：\n1、学生信息查询(全部)\n2、学生信息查询（个人）\n3、学生信息增删改查\n4、学生信息修改请求处理\n6、退出\n')
        xz.get(choose,a)()
        if choose =='6':
            break
#成绩管理
def teacher_grade_gl():
    while True:
        xz = {
            '1': tea.teacher_grade_qbck,#成绩查询（全部<班主任班级的所有科目，非班主任的班级教学科目>）       关于班主任班级和非班主任班级可通过查看的班级分辨
            '2': tea.teacher_grade_gtck,#成绩个体查询（班主任班级的某一个人的所有科目成绩，非班主任班级的教学科目成绩）
            '3': tea.teacher_gradefuyu,#成绩赋予（教学科目成绩赋予）
            '4': tea.teacher_grade_xg,#成绩单一修改
            '5': tea.teacher_pj_jg_yx,#平均分，及格率，优秀率查看（班主任班级所有科目，非班主任班级教学科目）
        }
        choose = input('\n您可以进行相应操作：\n1、成绩查询(全部<一次查一个班级>)\n2、成绩个体查询\n3、成绩赋予\n4、成绩修改\n5、平均分，及格率，优秀率查看\n6、退出\n')
        xz.get(choose,a)()
        if choose =='6':
            break