import pymysql
import lesson
room_name=[]
room_kc=[]
#数据一次性输入
def room_shuru():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()
    name=['信电101','信电102','信电103','信电201','信电206','信电207','信电208','信电301','信电302','信电303','信电304','信电305','信电306','信电307','信电308','信电309','信电401','信电402','信电403','信电407','信电408','信电501','信电506','信电507','信电508','信电509','信电601','信电602','信电603','信电604','信电605','信电606','信电607']
    yt=['','服装鞋类制版实训室','服装鞋类制版实训室','','AI实训室','信息安全实训室','物联网工程实训室','','','','','','物联网技术实训室','无线传感器实训室','软件工程实训室','移动开发技术实训室','','','','北斗技术实训室','华为网院','','电力驱动实训室','电源实训室','模电实训室','单片机实训室','','','','','电子技能实训室','计算机组装实训室','综合布线实训室']
    rs=[100,55,55,100,60,60,50,100,55,55,55,55,50,50,50,45,100,55,55,54,54,100,50,40,48,45,55,55,55,55,45,50,50]
    i=0
    for ele in name:
        sql = "INSERT INTO room VALUES ('{}','{}',{})".format(ele, yt[i], rs[i])
        i += 1
        try:
            cur.execute(sql)
            conn.commit()
        except:
            conn.rollback()
    conn.close()  # 关闭数据库连接
#查看空闲教室
def room_spare():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    zhou = input('请输入1-18周任一：')  # 指定周
    if zhou != '':
        xingqi = input('请输入星期:')  # 指定星期
        if xingqi != '':
            xingqi01 = int(xingqi) - 1
            i = ['一', '二', '三', '四', '五', '六', '日']
            jie = input('请输入节：')  # 指定节
            if jie != '':
                sql = "SELECT `课程名称`,`课程指定教学地点`,`星期`,`节`,`所属班级`,`对应教师` FROM `lesson`  WHERE `周` LIKE '%,{},%' AND `星期`='星期{}' AND `节` LIKE '%{}%' ORDER BY `节`".format(int(zhou), i[xingqi01],jie)  # 指定星期，节,周课程
            else:
                print('具体节不能空！')
        else:
            print('星期不能空！')
    else:
        print('周不能空！')
    try:
        cur.execute(sql)
        data = cur.fetchall()
        # data为数组
        for i in data:
            room_kc.append(i)
            # print('课程：{:<10}   地点：{:<10}   {:^5}   {:>10}节-----{}    {}教师任课'.format(i[0],i[1],i[2],i[3],i[4],i[5]))
            # print(i)
        sel_room()
    except:
        conn.rollback()
        print('cuow')
    cur.close()
    conn.close()
def sel_room():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='DHLX9035', port=3306, db='text', charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    sql='SELECT * FROM room'
    cur.execute(sql)
    classroom = cur.fetchall()
    # print(room_kc)
    for ele in classroom:
        room_name.append(ele[0])
    # print(room_name)
    for ele in room_kc:
        if ele[1] in room_name:
            room_name.remove(ele[1])
#显示空闲教室
def room_deal1():
    print(room_name)
    room_name.clear()
    room_kc.clear()
#显示现阶段的教室情况
def room_deal2():
    for ele in room_kc:
        print('{:<8}{:<10}{:5}{:8}'.format(ele[1],ele[0],ele[5],ele[4]))
    room_name.clear()
    room_kc.clear()
if __name__ == '__main__':
    room_spare()
    room_deal2()
