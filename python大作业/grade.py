#对应成绩表
#学号  课程名称  分数  等级
import pymysql
from 用户.教师 import teacher
def unit():#模版
    conn = pymysql.connect(host='127.0.0.1'  # 连接名称，默认127.0.0.1
                           , user='root'  # 用户名
                           , passwd='DHLX9035'  # 密码
                           , port=3306  # 端口，默认为3306
                           , db='text'  # 数据库名称
                           , charset='utf8'  # 字符编码
                           )
    cur = conn.cursor()  # 生成游标对象
    #=================
    #关闭
    sql=''
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
    except:
        conn.rollback()  # 如果发生错误则回滚
    conn.close()  #
#空成绩一次性输入
def grade_shuju_add():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    sql = "select `学号` from `stu` "
    cur.execute(sql)
    bh = cur.fetchall()#学号
    sql = "select `课程` from `course` "
    cur.execute(sql)
    kc = cur.fetchall()#课程
    # for bh1 in bh:
    #     for kc1 in kc:
    #         sql="INSERT INTO grade VALUES ('{}','{}','')".format(bh1[0],kc1[0])
    #         cur.execute(sql)
    for kc1 in kc:
        for bh1 in bh:
            sql="INSERT INTO grade VALUES ('{}','{}','')".format(bh1[0],kc1[0])
            cur.execute(sql)
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
#成绩表数据清空
def grade_clear():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    sql='TRUNCATE TABLE grade;'
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
    except:
        conn.rollback()  # 如果发生错误则回滚
    conn.close()  # 关闭数据库连接
#管理员全部成绩查询
def admin_qb_chaxun():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    sql='select * from grade'
    cur.execute(sql)
    data=cur.fetchall()
    for ele in data:
        print(ele)
    cur.close()
    conn.close()
#管理员成绩个体查询
def admin_gt_chaxun():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    xh=input('请输入学号：')
    sql = f"SELECT stu.`学号`,stu.`姓名`,grade.`课程名称`,grade.`分数` from stu JOIN grade ON stu.`学号`=grade.`学号` WHERE  stu.`学号`='{xh}'"
    cur.execute(sql)
    shuju = cur.fetchall()  # 对应的班级科目数据(('学号','姓名','课程名称','分数'))
    for i in shuju:
        print(f'{i[0]}  {i[1]}  {i[2]}  {i[3]}')

#管理员平均分，及格率，优秀率查看（各个班级，所有科目）
def grade_pj():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    sql = f"SELECT stu.`班级`,grade.`课程名称`,COUNT(*) AS `学生人数`,AVG(grade.`分数`) AS `平均分`,COUNT(CASE WHEN grade.`分数` >= 60 THEN 1 END) AS `及格人数`,(COUNT(CASE WHEN grade.`分数` >= 60 THEN 1 END) / COUNT(*))*100 AS `及格率`,COUNT(CASE WHEN grade.`分数` >= 90 THEN 1 END) AS `优秀人数`,(COUNT(CASE WHEN grade.`分数` >= 90 THEN 1 END) /COUNT(*))*100 AS `优秀率` FROM stu JOIN grade ON stu.`学号`=grade.`学号` GROUP BY stu.`班级`,grade.`课程名称`"
    try:
        cur.execute(sql)
        data=cur.fetchall()
        for ele in data:
            print(f'班级：{ele[0]}  {ele[1]:10}  班级人数：{ele[2]}  平均分：{ele[3]}  及格人数：{ele[4]}  及格率：{ele[5]}  优秀人数：{ele[6]}  优秀率：{ele[7]}')#课程名称，学生人数，平均分，及格人数，及格率，优秀人数，优秀率
    except:
        conn.rollback()
    conn.close()
