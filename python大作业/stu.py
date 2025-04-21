import pymysql
import login1
from 用户.学生 import student
from 用户.教师 import teacher
#连接数据库
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

def chakan_gr():#查看个人信息（手动）
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    c=input('请输入学生学号：')
    sql = "select * from `stu` where `学号`='{}'".format(c)  # SQL语句
    cur.execute(sql)  # 执行SQL语句
    data = cur.fetchall()  # 通过fetchall方法获得数据
    for i in data[0]:  # 打印输出数据
        print(i)
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
def chakan():#查看全部
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    sql = "select * from `stu` "  # SQL语句
    cur.execute(sql)  # 执行SQL语句
    data = cur.fetchall()  # 通过fetchall方法获得数据
    for i in data:  # 打印输出数据
        print(i)
    cur.close()  # 关闭游标
    conn.close()  # 关闭连接
def chakan_self():#检查自我信息（自动）
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    sql = "select * from `stu` where `学号`='{}'".format(login1.log_xinxi['id'])  # SQL语句
    cur.execute(sql)  # 执行SQL语句
    data = cur.fetchall()  # 通过fetchall方法获得数据
    for i in data:  # 打印输出数据
        print(i)
    cur.close()  # 关闭游标
    conn.close()  # 关闭连
def zengjia():#增加
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    # 学号  姓名  性别  联系电话bigint  年龄bigint
    xh=input('请输入学号：')
    name=input('请输入姓名：')
    sex=input('请输入性别：')
    tel=input('请输入联系电话：')
    age=input('请输入qq：')
    cl=input('请输入班级：')
    ban=input('输入班主任：')
    sql = "INSERT INTO stu VALUES ('{}','{}','{}',{},{},'{}','{}')".format(xh,name,sex,int(tel),int(age),cl,ban)
    # ===================================================
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
        print('成功!')
    except:
        conn.rollback()  # 如果发生错误则回滚
        print('添加错误！')
    conn.close()  # 关闭数据库连接
def shanchu():#删除
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    xh=int(input('请输入删除者学号：'))
    sql = 'DELETE FROM stu WHERE `学号` = "{}"'.format(xh)
    # ===================================================
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
    except:
        conn.rollback()  # 如果发生错误则回滚
    conn.close()  # 关闭数据库连接
def xiugai():#手动修改
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    #=================
    #关闭
    xh=int(input('请输入修改者学号：'))
    xzxg=input('请输入修改选项：姓名  性别  联系电话  qq  班级\n')
    xgnr=input('请输入修改内容：')
    sql="UPDATE stu SET `{}` ={} WHERE `学号` = '{}'".format(xzxg,xgnr,xh)
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
        print('修改成功！')
    except:
        conn.rollback()  # 如果发生错误则回滚
        print('修改失败！')
    conn.close()  # 关闭数据库连接
def class_in():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    #=================
    #关闭
    sql="SELECT * FROM stu WHERE `学号` NOT LIKE '__________'"
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
        data = cur.fetchall()  # 通过fetchall方法获得数据
        if len(data)==0:
            print('暂无')
        else:
            for i in data:  # 打印输出前2条数据
                print(i)
    except:
        conn.rollback()  # 如果发生错误则回滚
        print('检查失败！')
    conn.close()  # 关闭数据库连接
#成绩查看
def student_cjck():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    sql = f"SELECT stu.`学号`,stu.`姓名`,grade.`课程名称`,grade.`分数` from stu JOIN grade ON stu.`学号`=grade.`学号` WHERE  stu.`学号`='{student.student_xx['学号']}'"
    cur.execute(sql)
    shuju = cur.fetchall()  # 对应的班级科目数据(('学号','姓名','课程名称','分数'))
    print("课程           分数")
    for i in shuju:
        print(f'{i[2]:10}  {i[3]}')

#数据一次性输入
def stu_add():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    xh=['1904160221','2006380216','2006440242','2031010346','2031020241','2205231051','2205231053','2205231054','2205231055','2205231056','2205231057','2205231058','2205231059','2205231060','2205231062','2205231063','2205231064','2205231065','2205231066','2205231067','2205231068','2205231069','2205231070','2205231071','2205231072','2205231075','2205231076','2205231077','2205231078','2205231079','2205231080','2205231081','2205231082','2205231083','2205231084','2205231085','2205231088','2205231089','2205231090','2205231091','2205231092','2205231093','2205231095','2205231096','2205231097','2205231098','2031020242','1431070138','2202051063','2205341010','2205341013','2205211015','2205211046','2207141048','2019240136']
    name=['谢毅博','杜伟艺','林振汉','杨忠豪','李龙杰','欧炜','郭林同','林惠珍','魏杰','吴洪伟','李玮钊','张泽晨','张吉壕','王海鑫','李金煌','蔡泽杰','施文集','洪旭鹏','陈耿伟','赖晓玲','黄振炳','雷康乘','郑凯','郑佳馨','陈嘉良','杨袁','叶爱阳','吴晨晖','李泽城','曾堡鑫','詹万生','詹震威','陈晓阳','吴清霞','赵子涵','杨佳琪','张博','龚浩','金旭升','周承湛','苏世龙','马红芳','商智勇','阮婷辉','徐琳琳','李洋','汤岳虎','李成鑫','彭美','谢进','王天傲','黄琦鸿','张鑫志','王冲冲','黄伟涛']
    sex=['男','男','男','男','男','男','男','女','男','男','男','男','男','男','男','男','男','男','男','女','男','男','男','女','男','女','男','男','男','男','男','男','男','女','男','女','男','男','男','男','男','女','男','女','女','男','男','男','女','男','男','男','男','男','男']
    tel=[15985939088,18750170930,15059570715,15059177905,15960727149,17750351762,15715083121,13123051008,15759087998,17739523672,18859756212,15375735528,13559531957,18876517847,18859919417,15059581896,13178088065,15159818782,18760475909,18859095615,17338837535,17268627380,13559906041,15892145206,15060093708,17305083915,17744062750,13055402360,13959891856,19105052963,13163952010,13110822735,17689923850,15059262196,18409606009,13895304393,18995203121,18195297884,13369564062,18095578469,15709551161,13037951213,18786240889,13978761012,15278318971,18835211404,17759363931,18627792375,15259438203,15160773111,13665992846,15305031882,19139191768,18285266072,17750670209]
    qq=[531794250,1538277370,1414906460,841845776,2446556002,2403542164,2934639390,1137698042,1480686816,2663586550,1913307208,3241119453,1007628799,2629723398,3559784829,3395804459,812885461,1839694450,2025813616,3298213187,1719162258,3349569533,1544759897,295048441,2650128843,3253488535,2561198361,690897622,1419664478,1260094313,2871652844,1194567347,1099828271,2150999203,2222123876,2364647298,1585863602,2394268285,2844250183,2727055831,2846915377,1782868505,3271703579,2638911232,2153612229,1946284120,1279483669,291674807,3366988764,365145360,2031680589,1829693309,1814190631,3132436591,447073139]
    cl='软件3班'
    cur = conn.cursor()  # 生成游标对象
    i=0
    while True:
        if i+1<len(xh):
            sql = "INSERT INTO stu VALUES ('{}','{}','{}',{},{},'{}')".format(xh[i], name[i], sex[i], tel[i], qq[i],cl)
            i += 1
            try:
                cur.execute(sql)  # 执行插入的sql语句
                conn.commit()  # 提交到数据库执行
            except:
                conn.rollback()  # 如果发生错误则回滚
        else:
            break
    conn.close()  # 关闭数据库连接
#批量数据一次性删除
def delclear():
    conn = pymysql.connect(host='127.0.0.1'  # 连接名称，默认127.0.0.1
                           , user='root'  # 用户名
                           , passwd='DHLX9035'  # 密码
                           , port=3306  # 端口，默认为3306
                           , db='text'  # 数据库名称
                           , charset='utf8'  # 字符编码
                           )
    cur = conn.cursor()  # 生成游标对象
    #=====================================
    #关闭
    sql='TRUNCATE TABLE stu;'
    try:
        cur.execute(sql)  # 执行插入的sql语句
        conn.commit()  # 提交到数据库执行
    except:
        conn.rollback()  # 如果发生错误则回滚
    conn.close()  # 关闭数据库连接
def xg_qq():
    a=['联系电话','qq','姓名']
    xg_xiang=input('请选择修改项：联系电话  qq  姓名')
    xg_mean=input('请输入修改内容：')
    if xg_xiang in a and xg_mean!='':
        add={'修改人学号':student.student_xx['学号'],'修改项':xg_xiang,'修改内容':xg_mean,'班主任':student.student_xx['班主任']}
        teacher.stu_xg_qq.append(add)
        print('已向班主任发送个人信息修改请求！')
def a():
    return

def stu_gl():
    print('————————学生管理————————')
    while True:
        xz = {
            '1': chakan,
            '2': zengjia,
            '3': shanchu,
            '4': xiugai,
            '5': class_in,
        }
        choose = input('\n请选择相应操作：\n1、查看所有学生信息\n2、增加学生\n3、删除学生\n4、修改学生信息\n5、查看学号有出错之人\n6、退出\n')
        xz.get(choose, a)()
        if choose =='6':
            break