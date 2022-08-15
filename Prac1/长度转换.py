s=input()
if s[-1]=='m':
    m=eval(s[:-1])
    print("{:.2f}ft".format(m*3.2808))
else:
    ft=eval(s[:-2])
    print("{:.2f}m".format(ft/3.2808))