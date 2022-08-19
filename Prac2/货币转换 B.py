s=input()
if s[0]=='$':
    print("￥{:.2f}".format(eval(s[1:])*6.78))
elif s[0]=='￥':
    print("${:.2f}".format(eval(s[1:])/6.78))
elif s[0:3]=='RMB':
    print("USD{:.2f}".format(eval(s[3:])/6.78))
else:
    print("RMB{:.2f}".format(eval(s[3:])*6.78))