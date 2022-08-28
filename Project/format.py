f=[]
for i in range(11,23):
    f.append(open("result/year/20{}年天气情况.csv".format(i),encoding="gbk"))
for j in range(33):
    for i in range(12):
        ls=f[i].readline().replace('\n','').split(',')
        if j==0:
            continue
        fw=open("result/city/{}_{}.csv".format(ls[0],ls[1]),"a",encoding="gbk")
        if i==0:
            fw.write("年份,平均高温,平均低温,极端高温,极端低温\n")
        fw.write("20{},{},{},{},{}\n".format(i+11,ls[2],ls[3],ls[4],ls[5]))