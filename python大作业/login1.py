import pymysql
import tea
from 用户.学生 import student
from 用户.教师 import teacher
from 用户.管理员 import admin
import stu
log_xinxi={}
conn = pymysql.connect(host='127.0.0.1'  # 连接名称，默认127.0.0.1
                       , user='root'  # 用户名
                       , passwd='DHLX9035'  # 密码
                       , port=3306  # 端口，默认为3306
                       , db='text'  # 数据库名称
                       , charset='utf8'  # 字符编码
                       )
def log():#登录
    find=0
    while True:
        xz=input('请选择身份：\n1、管理员\n2、教师\n3、学生\n')
        cur = conn.cursor()  # 生成游标对象
        if xz=='1':
            id = input('请输入ID：')
            # password = input('请输入密码：')
            sql = "select * from `user` where id='{}'".format(id)  # SQL语句
            # sql = "select * from `user` where id='{}' and password='{}' ".format(id, password)  # SQL语句
        elif xz=='2':
            id = input('请输入教师编号：')
            # password = input('请输入教师名：')
            sql = "select * from `teacher` where `教师编号`='{}'".format(id)  # SQL语句
            # sql = "select * from `teacher` where `教师编号`='{}' and `教师名`='{}' ".format(id, password)  # SQL语句
        elif xz=='3':
            id = input('请输入学号：')
            # password = input('请输入姓名：')
            sql = "select * from `stu` where `学号`='{}'".format(id)  # SQL语句
            # sql = "select * from `stu` where `学号`='{}' and `姓名`='{}' ".format(id, password)  # SQL语句
        else:
            print('没有该选项！')
        cur.execute(sql)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        if len(data) > 0:
            print('登录成功！')
            break
        else:
            a=input('登录失败！\n按任意非空键退出！')
            if len(a)>0:
                find=1
                break
            continue
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
    log_xinxi['id'] = id
    # log_xinxi['password'] = password
    new=list(data[0])
    if find==1:
        exit()
    if xz=='1':
        admin.admin_xx['id']=new[1]
        admin.admin_xx['password']=new[2]
        admin.admin_xt()
    elif xz=='2':
        teacher.teacher_xx['教师编号']=new[0]
        teacher.teacher_xx['姓名']=new[1]
        teacher.teacher_xx['教学科目']=new[2]
        teacher.teacher_xx['教学班级']=new[3]
        teacher.teacher_xx['联系电话']=new[4]
        teacher.teacher_xx['班级——教师联系']=new[5]
        tea.teacher_shuju_zzz()
        teacher.teacher_xt()
    elif xz=='3':
        #储存学生登录者信息，方便个体查询
        student.student_xx['学号'] = new[0]
        student.student_xx['姓名'] = new[1]
        student.student_xx['性别'] = new[2]
        student.student_xx['联系电话'] = new[3]
        student.student_xx['qq'] = new[4]
        student.student_xx['qq'] = new[5]
        student.student_xx['班级'] = new[6]
        student.student_xx['班主任'] = new[7]
        student.student_xt()

