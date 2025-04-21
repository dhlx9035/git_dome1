import pymysql
from 用户.学生 import student
from 用户.教师 import teacher
from 用户.管理员 import admin
log_xinxi={}

def log():#登录
    find=0
    while True:
        conn = pymysql.connect(host='127.0.0.1'  # 连接名称，默认127.0.0.1
                               , user='root'  # 用户名
                               , passwd='DHLX9035'  # 密码
                               , port=3306  # 端口，默认为3306
                               , db='text'  # 数据库名称
                               , charset='utf8'  # 字符编码
                               )
        cur = conn.cursor()  # 生成游标对象
        id = input('请输入ID：')
        password = input('请输入密码：')
        sql = "select * from `user` where id='{}' and password='{}' ".format(id, password)  # SQL语句
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
    if find==1:
        exit()
    elif data[0][0]=='学生':
        student.student_xt()
        log_xinxi['id']=id
        log_xinxi['password']=password
    elif data[0][0]=='教师':
        log_xinxi['id']=id
        log_xinxi['password']=password
        teacher.teacher_xt()
    elif data[0][0]=='管理员':
        log_xinxi['id']=id
        log_xinxi['password']=password
        admin.admin_xt()

#教师对应的数据
def tea_xinxi():
    return
