import time
import pymysql

import login1
import stu
from 用户.教师 import teacher
from 用户.管理员 import admin
#连接数据库
conn = pymysql.connect(host='127.0.0.1'  # 连接名称，默认127.0.0.1
                       , user='root'  # 用户名
                       , passwd='DHLX9035'  # 密码
                       , port=3306  # 端口，默认为3306
                       , db='text'  # 数据库名称
                       , charset='utf8'  # 字符编码
                       )
#查看所有教师数据
def tea_xinxi0():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    sql = "select * from `teacher` "  # SQL语句
    cur.execute(sql)  # 执行SQL语句
    data = cur.fetchall()  # 通过fetchall方法获得数据
    for i in data:  # 打印输出数据
        print(i)
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
#查看个体教师数据
def tea_xinxi1():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    while True:
        c = input('请输入教师编号：')
        sql = "select * from `teacher` where `教师编号`='{}' ".format(c)  # SQL语句
        cur.execute(sql)
        data = cur.fetchall()
        if len(data) < 1:
            x = input('教师编号错误！\n请选择是否从新输入（y or n）')
            if x == 'n':
                return
            elif x == 'y':
                continue
        else:
            break
    for i in data:  # 打印输出数据
        print(i)
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
#增加教师
def teacher_add():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    bh=input('输入教师编号：')
    name=input('输入教师名：')
    les=input('输入教师科目：')
    bj=input('输入教学班级：')
    mun=input('输入联系电话：')
    lx=input('教师班级联系：')
    sql = "INSERT INTO teacher VALUES ('{}','{}','{}','{}','{}','{}')".format(bh,name,les,bj,mun,lx)
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
        print('成功!')
    except:
        conn.rollback()  # 如果发生错误则回滚
        print('添加错误！')
    conn.close()  # 关闭数据库连接
#删除教师
def teacher_del():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    xh = input('请输入删除者教师编号：')
    # km = input('请输入教学课程：')
    sql = 'DELETE FROM teacher WHERE `教师编号` = "{}"'.format(xh)
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
    except:
        conn.rollback()  # 如果发生错误则回滚
    conn.close()  # 关闭数据库连接
#手动修改
def xiugai():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    # =================
    # 关闭
    xh = int(input('请输入修改者学号：'))
    xzxg = input('请输入修改选项：姓名  性别  联系电话  qq  班级\n')
    xgnr = input('请输入修改内容：')
    sql = "UPDATE stu SET `{}` ={} WHERE `学号` = '{}'".format(xzxg, xgnr, xh)
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
        print('修改成功！')
    except:
        conn.rollback()  # 如果发生错误则回滚
        print('修改失败！')
    conn.close()  # 关闭数据库连接
#修改教师数据
def tea_xg():
    cur = conn.cursor()  # 生成游标对象
    xh=input('请输入编号：')
    xzxg=input('请输入修改选项：教师名   教学科目    教学班级\n')
    xgnr=input('请输入修改内容：')
    sql="UPDATE teacher SET `{}` ='{}' WHERE `教师编号` = '{}'".format(xzxg,xgnr,xh)
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
        print('修改成功！')
    except:
        conn.rollback()  # 如果发生错误则回滚
        print('修改失败！')
    conn.close()  # 关闭数据库连接
#检查自我信息
def chakan_self():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    sql = "select * from `teacher` where `教师编号`='{}' and `教师名`='{}' ".format(teacher.teacher_xx['教师编号'],teacher.teacher_xx['姓名'])  # SQL语句
    cur.execute(sql)  # 执行SQL语句
    data = cur.fetchall()  # 通过fetchall方法获得数据
    for i in data:  # 打印输出数据
        print(i)
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
#教师请求数据修改
def xg_qq():
    xg_xiang=input('请选择修改项：  姓名  教学科目  教学班级')
    xg_mean=input('请输入修改内容：')
    if xg_xiang!='' and xg_mean!='':
        add={'教师编号':teacher.teacher_xx['教师编号'],'修改项':xg_xiang,'修改内容':xg_mean}
        admin.tea_xg_qq.append(add)
        print('已向管理员发送个人信息修改请求！')
#教师请求处理
def tea_qq_deal():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    i=0#序号
    for ele in admin.tea_xg_qq:
        i+=1
        print(i,'  教师编号：{}  请求将 {} 修改成 {} '.format(ele['教师编号'],ele['修改项'],ele['修改内容']))
    if i==0:
        print('没有请求！1秒后返回')
        time.sleep(1)
        return
    xz01=input('输入"all"全部同意\n输入数字单一同意\n输入"rej"全部拒绝\n放空将返回\n')
    if xz01=='':
        return
    elif xz01=='all':
        for ele in admin.tea_xg_qq:
            sql = "UPDATE teacher SET `{}` ='{}' WHERE `教师编号` = '{}'".format(ele['修改项'],ele['修改内容'],ele['教师编号'])
            try:
                cur.execute(sql)  # 执行插入的sql语句
                conn.commit()  # 提交到数据库执行
            except:
                conn.rollback()  # 如果发生错误则回滚
                print('修改失败！')
                print(ele)
        admin.tea_xg_qq.clear()
    elif xz01=='rej':#如果后面学生系统加入“教师消息”，可进行记录
        teacher.stu_xg_qq.clear()
        print('全部打回')
    elif int(xz01)<=i:
        sql="UPDATE teacher SET `{}` ={} WHERE `教师编号` = '{}'".format(admin.tea_xg_qq[i-1]['修改项'],admin.tea_xg_qq[i-1]['修改内容'],admin.tea_xg_qq[i-1]['教师编号'])
        try:
            cur.execute(sql)  # 执行插入的sql语句
            conn.commit()  # 提交到数据库执行
            print('修改成功！')
            del admin.tea_xg_qq[int(xz01)-1]
        except:
            conn.rollback()  # 如果发生错误则回滚
            print('修改失败！')
    conn.close()  # 关闭数据库连接
#学生请求处理
def stu_qq_deal():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    i=0#序号
    for ele in teacher.stu_xg_qq:
        if teacher.teacher_xx['姓名']==ele['班主任']:
            i+=1
            print(i,'  学号为 {} 的学生请求将 {} 修改成 {} '.format(ele['修改人学号'],ele['修改项'],ele['修改内容']))
    if i==0:
        print('没有请求！1秒后返回')
        time.sleep(1)
        return
    xz01=input('输入"all"全部同意\n输入数字单一同意\n输入"rej"全部拒绝\n放空将返回\n')
    if xz01=='':
        return
    elif xz01=='all':
        for ele in teacher.stu_xg_qq:
            sql = "UPDATE stu SET `{}` ='{}' WHERE `学号` = '{}'".format(ele['修改项'],ele['修改内容'],ele['修改人学号'])
            try:
                cur.execute(sql)  # 执行插入的sql语句
                conn.commit()  # 提交到数据库执行
            except:
                conn.rollback()  # 如果发生错误则回滚
                print('修改失败！')
                print(ele)
        teacher.stu_xg_qq.clear()
    elif xz01=='rej':#如果后面学生系统加入“教师消息”，可进行记录
        teacher.stu_xg_qq.clear()
        print('全部打回')
    elif int(xz01)<=i:
        sql="UPDATE stu SET `{}` ={} WHERE `学号` = '{}'".format(teacher.stu_xg_qq[i-1]['修改项'],teacher.stu_xg_qq[i-1]['修改内容'],teacher.stu_xg_qq[i-1]['修改人学号'])
        try:
            cur.execute(sql)  # 执行插入的sql语句
            conn.commit()  # 提交到数据库执行
            print('修改成功！')
            del teacher.stu_xg_qq[int(xz01)-1]
        except:
            conn.rollback()  # 如果发生错误则回滚
            print('修改失败！')
    conn.close()  # 关闭数据库连接
#数据储存（教学班级，教师班级联系）
def teacher_shuju_zzz():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    sql = "select * from `teacher` where `教师编号`='{}'".format(login1.log_xinxi['id'])
    cur.execute(sql)
    data = cur.fetchall()
    i=0
    k=len(data)
    if k==1:
        return
    if k>1:
        for ele in data:
            if ele[5] == '班主任':
                teacher.teacher_xx['教学科目'] = ele[2]
                teacher.teacher_xx['教学班级'] = ele[3]
                teacher.teacher_xx['联系电话'] = ele[4]
                teacher.teacher_xx['班级——教师联系'] = ele[5]
            add={}#放这里还是放上面效果基本一致
            add['教师编号'] = ele[0]
            add['姓名'] = ele[1]
            add['教学科目'] = ele[2]
            add['教学班级'] = ele[3]
            add['联系电话'] = ele[4]
            add['班级——教师联系'] = ele[5]
            teacher.teacher_xinxi.append(add)
    # print(teacher.teacher_xinxi)
#教师——成绩查看（全部）
def teacher_grade_qbck():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    banji=input('请输入班级名称：')
    # print(teacher.teacher_xinxi)
    for km in teacher.teacher_xinxi:
        if banji in km['教学班级']:
            if km['班级——教师联系']=='班主任':
                sql = f"SELECT stu.`学号`,stu.`姓名`,grade.`课程名称`,grade.`分数` from stu JOIN grade ON stu.`学号`=grade.`学号` WHERE  stu.`班级`='{banji}' ORDER BY grade.`课程名称`,stu.`学号` "
            elif km['班级——教师联系']=='普通教师':
                sql = f"SELECT stu.`学号`,stu.`姓名`,grade.`课程名称`,grade.`分数` from stu JOIN grade ON stu.`学号`=grade.`学号` WHERE  stu.`班级`='{banji}' and grade.`课程名称`='{km['教学科目']}' ORDER BY grade.`课程名称`,stu.`学号` "
            else:
                print('您没有教学科目在此班级！')
                return
    try:
        cur.execute(sql)
        data=cur.fetchall()
        for ele in data:
            print(f'{ele[2]:10}{ele[0]:^16}{ele[1]:<5}{ele[3]:>5}')#教学科目，学号，姓名，分数
    except:
        conn.rollback()
    conn.close()
#教师成绩个体查看
def teacher_grade_gtck():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    xh=input('请输入学号：')
    sql='SELECT `班级` from stu where `学号`="{}"'.format(xh)
    cur.execute(sql)
    banji=cur.fetchall()#查出学号所属班级   (('软件3班'))
    for km in teacher.teacher_xinxi:
        if banji[0][0] in km['教学班级']:
            sql = f"SELECT stu.`学号`,stu.`姓名`,grade.`课程名称`,grade.`分数` from stu JOIN grade ON stu.`学号`=grade.`学号` WHERE  stu.`学号`='{xh}'"
            cur.execute(sql)
            shuju = cur.fetchall()  # 对应的班级科目数据(('学号','姓名','课程名称','分数'))
            for i in shuju:
                print(f'{i[0]}  {i[1]}  {i[2]}  {i[3]}')
#成绩赋予
def teacher_gradefuyu():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    banji=input('请输入班级名称：')
    for km in teacher.teacher_xinxi:
        if banji in km['教学班级']:
            # sql=f"SELECT stu.`学号`,stu.`姓名`,grade.`课程名称`,grade.`分数` from stu JOIN grade ON stu.`学号`=grade.`学号` WHERE  stu.`班级`='{banji}' and grade.`课程名称`='{km['教学科目']}'  AND  ORDER BY grade.`课程名称`,stu.`学号`"
            sql=f"SELECT stu.`学号`,stu.`姓名`,grade.`课程名称`,grade.`分数` from stu JOIN grade ON stu.`学号`=grade.`学号` WHERE  stu.`班级`='{banji}' AND grade.`分数` IS NULL OR grade.`分数`=0 and grade.`课程名称`='{km['教学科目']}' ORDER BY stu.`学号`"
    try:
        cur.execute(sql)
        data=cur.fetchall()
        for ele in data:
            print(f'{ele[2]:10}{ele[0]:^16}{ele[1]:<5}{ele[3]:>5}')#教学科目，学号，姓名，分数
            xgnr = input('请输入该同学成绩：        输入0则退出成绩赋予\n')
            sql = f"UPDATE grade SET `分数` ={xgnr} WHERE `学号` = '{ele[0]}' and `课程名称`='{ele[2]}'"
            cur.execute(sql)
            if xgnr=='0':
                break
    except:
        conn.rollback()
    conn.close()
#成绩单一修改
def teacher_grade_xg():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    xh=input('请输入学号：')
    sql='SELECT `班级` from stu where `学号`="{}"'.format(xh)
    cur.execute(sql)
    banji=cur.fetchall()#查出学号所属班级   (('软件3班'))
    for km in teacher.teacher_xinxi:
        if banji[0][0] in km['教学班级']:
            kemu=km['教学科目']
    sql=f"SELECT stu.`学号`,stu.`姓名`,grade.`课程名称`,grade.`分数` from stu JOIN grade ON stu.`学号`=grade.`学号` WHERE  stu.`学号`='{xh}' AND grade.`课程名称`='{kemu}'"
    try:
        cur.execute(sql)
        old_shuju = cur.fetchall()  # 对应的班级科目数据(('学号','姓名','课程名称','分数'))
        for i in old_shuju:
            print(f'{i[0]}  {i[1]}  {i[2]}  {i[3]}')
        xz=input('是否修改？（按“ n ”退出）')
        if xz=='n':
            return
        xgnr=input('修改为：')
        sql=f"UPDATE grade SET `分数` ={xgnr} WHERE `学号` = '{xh}' and `课程名称`='{kemu}'"
        cur.execute(sql)
        conn.commit()
        print('修改成功！')
    except:
        conn.rollback()  # 如果发生错误则回滚
        print('错误！\n请检查所输入的学号是否属于所教班级的学生')
#班主任平均分，及格率，优秀率查看
def teacher_pj_jg_yx():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    banji=input('请输入班级名称：')
    for km in teacher.teacher_xinxi:
        if banji in km['教学班级']:
            if km['班级——教师联系']=='班主任':
                sql = f"SELECT grade.`课程名称`,COUNT(*) AS `学生人数`,AVG(grade.`分数`) AS `平均分`,COUNT(CASE WHEN grade.`分数` >= 60 THEN 1 END) AS `及格人数`,(COUNT(CASE WHEN grade.`分数` >= 60 THEN 1 END) / COUNT(*))*100 AS `及格率`,COUNT(CASE WHEN grade.`分数` >= 90 THEN 1 END) AS `优秀人数`,(COUNT(CASE WHEN grade.`分数` >= 90 THEN 1 END) /COUNT(*))*100 AS `优秀率` FROM stu JOIN grade ON stu.`学号`=grade.`学号` WHERE  stu.`班级`='{banji}' GROUP BY grade.`课程名称`"
            elif km['班级——教师联系']=='普通教师':
                sql = f"SELECT grade.`课程名称`,COUNT(*) AS `学生人数`,AVG(grade.`分数`) AS `平均分`,COUNT(CASE WHEN grade.`分数` >= 60 THEN 1 END) AS `及格人数`,(COUNT(CASE WHEN grade.`分数` >= 60 THEN 1 END) / COUNT(*))*100 AS `及格率`,COUNT(CASE WHEN grade.`分数` >= 90 THEN 1 END) AS `优秀人数`,(COUNT(CASE WHEN grade.`分数` >= 90 THEN 1 END) /COUNT(*))*100 AS `优秀率` FROM stu JOIN grade ON stu.`学号`=grade.`学号` WHERE  stu.`班级`='{banji}' AND grade.`课程名称`='{km['教学科目']}' GROUP BY grade.`课程名称`"
            else:
                print('您没有教学科目在此班级！')
                return
    try:
        cur.execute(sql)
        data=cur.fetchall()
        for ele in data:
            print(f'{ele[0]:10}  班级人数：{ele[1]}  平均分：{ele[2]}  及格人数：{ele[3]}  及格率：{ele[4]}  优秀人数：{ele[5]}  优秀率：{ele[6]}')#课程名称，学生人数，平均分，及格人数，及格率，优秀人数，优秀率
    except:
        conn.rollback()
    conn.close()