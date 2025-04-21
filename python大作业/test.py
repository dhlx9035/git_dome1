if __name__ == '__main__':
    xz=int(input('选着'))
    data=(('aa','11,2,5,447'),())
    data1=('aa','11,2,5,447')
    a=data[xz-1]
    b=a.replace('a','A')
    c=a.replace("1",'2')
    print(b,'\n',c)