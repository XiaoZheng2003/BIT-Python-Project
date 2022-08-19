try:
    d=eval(input())
    e={}
    for k in d:
        e[d[k]]=k
    print(e)
except:
    print("输入错误")