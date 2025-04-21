import pymysql
from 用户.学生 import student
conn = pymysql.connect(host='127.0.0.1'  # 连接名称，默认127.0.0.1
                           , user='root'  # 用户名
                           , passwd='DHLX9035'  # 密码
                           , port=3306  # 端口，默认为3306
                           , db='text'  # 数据库名称
                           , charset='utf8'  # 字符编码
                           )
def kbck_admin():#课表查看(针对管理员)
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    a=input('查找班级：\n软件1,2,3班\n输入数字：')#指定班级
    if a!='':
        a1=input('请输入1-18周任一：')#指定周
        if a1!='':
            a2=input('请输入星期:')# 指定星期
            if a2!= '':
                a3=int(a2)-1
                i=['一','二','三','四','五','六','日']
                sql = "SELECT `课程名称`,`课程指定教学地点`,`星期`,`节`,`所属班级`,`对应教师` FROM `lesson`  WHERE `所属班级`='软件{}班' AND `周` LIKE '%{}%' AND `星期`='星期{}' ORDER BY `节`".format(int(a), int(a1),i[a3])  # 指定班级,周课程
            else:
                sql = "SELECT `课程名称`,`课程指定教学地点`,`星期`,`节`,`所属班级`,`对应教师` FROM `lesson`  WHERE `所属班级`='软件{}班' AND `周` LIKE '%{}%' ORDER BY `星期`".format(int(a),int(a1))  #指定班级,周课程
        else:
            sql="SELECT `课程名称`,`课程指定教学地点`,`星期`,`节`,`所属班级`,`对应教师` FROM `lesson`  WHERE `所属班级`='软件{}班' ORDER BY `星期`".format(int(a))  #指定班级,周课程
    else:
        sql = "SELECT `课程名称`,`课程指定教学地点`,`星期`,`节`,`所属班级`,`对应教师` FROM `lesson` ORDER BY `所属班级`,`课程名称`,`星期`"#所有课程
    # sql="SELECT `课程名称`,`课程指定教学地点`,`星期`,`节` FROM `lesson`  WHERE `所属班级`='软件3班' AND `星期`='星期一' AND `周` LIKE '%15%'  ORDER BY `节`
    try:
        cur.execute(sql)  # 执行插入的sql语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        # data为数组
        for i in data:  # 打印输出数据
            print('课程：{:<10}   地点：{:<10}   {:^5}   {:>10}节-----{}    {}教师任课'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
            # print(i)
    except:
        conn.rollback()  # 如果发生错误则回滚
        print('cuow')
    cur.close()  # 关闭游标
    conn.close()  # 关闭数据库连接
def kbck_student():#课表查看(针对学生)
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    #=================
    a=student.student_xx['班级']
    if a!='':
        a1=input('请输入1-18周任一：')#指定周
        if a1!='':
            a2=input('请输入星期:')# 指定星期
            if a2!= '':
                a3=int(a2)-1
                i=['一','二','三','四','五','六','日']
                sql = "SELECT `课程名称`,`课程指定教学地点`,`星期`,`节`,`所属班级`,`对应教师` FROM `lesson`  WHERE `所属班级`='{}' AND `周` LIKE '%{}%' AND `星期`='星期{}' ORDER BY `节`".format(a, int(a1),i[a3])  # 指定班级,周课程
            else:
                sql = "SELECT `课程名称`,`课程指定教学地点`,`星期`,`节`,`所属班级`,`对应教师` FROM `lesson`  WHERE `所属班级`='{}' AND `周` LIKE '%{}%' ORDER BY `星期`".format(a,int(a1))  #指定班级,周课程
        else:
            sql="SELECT `课程名称`,`课程指定教学地点`,`星期`,`节`,`所属班级`,`对应教师` FROM `lesson`  WHERE `所属班级`='{}' ORDER BY `星期`".format(a)  #指定班级,周课程
    else:
        sql = "SELECT `课程名称`,`课程指定教学地点`,`星期`,`节`,`所属班级`,`对应教师` FROM `lesson` ORDER BY `所属班级`,`课程名称`,`星期`"#所有课程
    # sql="SELECT `课程名称`,`课程指定教学地点`,`星期`,`节` FROM `lesson`  WHERE `所属班级`='软件3班' AND `星期`='星期一' AND `周` LIKE '%15%'  ORDER BY `节`
    try:
        cur.execute(sql)  # 执行插入的sql语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        # data为数组
        for i in data:  # 打印输出数据
            print('课程：{:<10}   地点：{:<10}   {:^5}   {:>10}节-----{}    {}教师任课'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
            # print(i)
    except:
        conn.rollback()  # 如果发生错误则回滚
        print('cuow')
    cur.close()  # 关闭游标
    conn.close()  # 关闭数据库连接
def stu_kb_xinxi():#学生查看课表信息(全部)
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    sql = "SELECT `课程名称`,`课程指定教学地点`,`周`,`星期`,`节`,`对应教师`,`课程分` FROM `lesson`  WHERE `所属班级`='{}' ORDER BY `星期`".format(student.student_xx['班级']) # 指定班级
    try:
        cur.execute(sql)  # 执行插入的sql语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for i in data:  # 打印输出数据
            print('课程：{:<10}   地点：{:<10}  {}教师任课  科目学分：{:^5}    {:^5}    {:>10}节  {:<10}周'.format(i[0],i[1],i[5],i[6],i[3],i[4],i[2]))
            # print(i)
    except:
        conn.rollback()  # 如果发生错误则回滚
        print('cuow')
    cur.close()  # 关闭游标
    conn.close()  # 关闭数据库连接
def admin_kb_xinxi():#管理员查看课表信息(全部)
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    sql = "SELECT `所属班级`,`课程名称`,`课程指定教学地点`,`周`,`星期`,`节`,`对应教师`,`课程分` FROM `lesson` ORDER BY `星期`"
    try:
        cur.execute(sql)  # 执行插入的sql语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        for i in data:  # 打印输出数据
            print('班级：{:<8}课程：{:<10}   地点：{:<10}  {}教师任课  科目学分：{:^5}   {:^5}{:>10}节  {:<10}周'.format(i[0],i[1],i[2],i[6],i[7],i[4],i[5],i[3]))
            # print(i)
    except:
        conn.rollback()  # 如果发生错误则回滚
        print('cuow')
    cur.close()  # 关闭游标
    conn.close()  # 关闭数据库连接
def kb_add():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur=conn.cursor()
    lesson_name=input('课程名称：')
    class_name=int(input('班级名称：\n   1  \n软件2班\n   3  \n输入数字：'))
    room=input('教室：')
    week=input('周：')
    ri=int(input('星期'))
    jie=input('节：')
    tea=input('任课教师：')
    cj=int(input('课程分：'))
    i = ['一', '二', '三', '四', '五', '六', '日']
    sql="INSERT INTO lesson VALUES ('{}','{}','0,{},19','星期{}','{}','软件{}班','{}',{})".format(lesson_name,room,week,i[ri-1],jie,class_name,tea,cj)
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
        print('成功!')
    except:
        conn.rollback()  # 如果发生错误则回滚
        print('添加错误！')
    conn.close()  # 关闭数据库连接
def kb_del():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    # a=input('指定班级：\n软件1,2,3班\n输入数字：')#指定班级
    a1 = input('请输入1-18周任一：')  # 指定周
    a2 = input('请输入星期:')  # 指定星期
    i = ['一', '二', '三', '四', '五', '六', '日']
    sql = "SELECT `课程名称`,`课程指定教学地点`,`星期`,`节`,`所属班级`,`对应教师`,`周` FROM `lesson`  WHERE `星期`='星期{}' AND `周` LIKE '%,{},%' ORDER BY `节`".format(i[int(a2)-1],a1) # 指定班级,周课程
    cur.execute(sql)  # 执行插入的sql语句
    data = cur.fetchall()  # 通过fetchall方法获得数据
    # data为数组
    k=0
    for i in data:  # 打印输出数据
        print('课程：{:<10}   地点：{:<10}   {:^5}   {:>10}节-----{}   {}'.format(i[0], i[1], i[2], i[3], i[4],i[5]))
        # print(i)
        k+=1
    # ===================================================
    xz=int(input('请输入你的选择（第几个）：'))
    if xz!='' and xz<=k:
        b=''
        for ele in data[xz-1][6]:
            b+=ele
        c=b.replace('{}'.format(a1),'')
        sql='update lesson set `周`="{}" where `课程名称`="{}"  and `星期`="{}" and `节`="{}"'.format(c,data[xz-1][0],data[xz-1][2],data[xz-1][3])
        try:
            cur.execute(sql)  # 执行插入的sql语句
            conn.commit()  # 提交到数据库执行
            print('删除成功！')
        except:
            conn.rollback()  # 如果发生错误则回滚
            print('出现错误，删除失败！！')
    else:
        print('删除失败！')
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
    except:
        conn.rollback()  # 如果发生错误则回滚
    conn.close()  # 关闭数据库连接
def kb_xiugai():
    return