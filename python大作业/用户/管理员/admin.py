import lesson
import stu
import tea
import room
import grade
tea_xg_qq=[]#教师编号  修改项  修改内容
admin_xx={}#管理员信息（中转站）  id  password
def a():
    return
def admin_xt():
    print('————————管理员：您好！————————')
    print('以下是您的基本信息：\n管理员编号：{0}\n管理员密码：{1}'.format(admin_xx['id'],admin_xx['password']))
    while True:
        xz = {
            '1': admin_les_gl,#课程管理
            '2': admin_tea_gl,#教师管理
            '3': admin_stu_gl,#学生管理
            '4': admin_room_gl,#教室管理
            '5': admin_grade_gl,#成绩管理
        }
        choose = input('\n您可以进行相应操作：\n1、课表操作\n2、教师管理\n3、学生管理\n4、教室管理\n5、成绩管理\n6、退出\n')
        xz.get(choose, a)()
        if choose =='6':
            break
#管理员----学生管理
def admin_stu_gl():
    print('亲爱的管理员，你可以对学生信息进行操作：')
    while True:
        xz = {
            '1': stu.chakan,#有时间改为查询关于学生的所有数据
            '2': stu.chakan_gr,#有时间改为查询关于学生的所有数据
            '3': stu.stu_gl,#√
        }
        choose = input('\n1、学生信息查询(全部)\n2、学生信息查询（个人）\n3、学生信息增删改查\n6、退出\n')
        xz.get(choose,a)()
        if choose =='6':
            break
#管理员----教师管理
def admin_tea_gl():#√
    while True:
        xz = {
            '1': tea.tea_xinxi0,#教师信息查询(全部)
            '2': tea.tea_xinxi1,#教师信息查询（个人）
            '3': tea.tea_qq_deal,#教师请求处理
            '4': tea.teacher_add,#增加教师
            '5': tea.teacher_del,#删除教师
        }
        choose = input('\n1、教师信息查询(全部)\n2、教师信息查询（个人）\n3、教师请求处理\n4、增加教师\n5、删除教师\n6、返回\n')
        xz.get(choose,a)()
        if choose =='6':
            break
#管理员----课程管理
def admin_les_gl():
    while True:
        xz = {
            '1': lesson.admin_kb_xinxi,#课程信息查询(全部)
            '2': lesson.kbck_admin,#课程信息查询（个人）
            '3': '',#科目查看
            '4': '',#科目增加
            '5': '',#科目删除
            '7': lesson.kb_add,#课程增加
            '8': lesson.kb_del,#课程删除
        }
        choose = input('\n1、课表信息查询(全部)\n2、课表信息查询（个体）\n3、课程查看\n4、课程增加\n5、课程删除\n6、返回\n7、课表增加\n8、课表删除\n')
        xz.get(choose,a)()
        if choose =='6':
            break
#管理员----教室管理
def admin_room_gl():
    while True:
        choose = input('\n1、空闲教室查询\n2、教室信息查询\n6、返回\n')
        if choose=='1':
            room.room_spare()
            room.room_deal1()
        if choose=='2':
            room.room_spare()
            room.room_deal2()
        elif choose =='6':
            break
#管理员----成绩管理
def admin_grade_gl():
    while True:
        xz = {
            '1': grade.admin_qb_chaxun,#成绩查询(全部)
            '2': grade.admin_gt_chaxun,#成绩查询（个人）（学号）
            '3': grade.grade_pj,#平均分，及格率，优秀率查看（1、各班级，单科目<针对的是各个班级排名>）
        }
        choose = input('1、成绩查询(全部)\n2、成绩查询（个体）\n3、平均分，及格率，优秀率查看\n6、返回\n')
        xz.get(choose,a)()
        if choose =='6':
            break