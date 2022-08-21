def f(i,j):
    if i==1 or j==1:
        return 1
    if not ls[i][j]:
        ls[i][j]=f(i-1,j)+f(i,j-1)
    return ls[i][j]
m,n=eval(input()),eval(input())
ls=[[0 for i in range(n+1)] for j in range(m+1)]
print(f(m,n))