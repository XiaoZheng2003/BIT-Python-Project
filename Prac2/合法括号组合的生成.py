def bracket(rst,l,r):
    if l==n and r==n:
        ls.append(rst)
    else:
        if l<n:
            bracket(rst+'(',l+1,r)
        if r<l:
            bracket(rst+')',l,r+1)
n=eval(input())
ls=[]
bracket('',0,0)
print(ls)