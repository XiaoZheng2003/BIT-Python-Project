def findPrime(n:int):
    s,flag='',2
    for i in range(3,n,2):
        if n%i==0:
            flag-=1
            s=str(i)+s
        if flag==0:
            break
    return s
def count(n:int,m:int):
    cnt,k,i=0,n,1
    while k:
        k=n//i
        h=k//10
        if m==0:
            if h:
                h-=1
            else:
                break
        cnt+=h*i
        cur=k%10
        if cur>m:
            cnt+=i
        elif cur==m:
            cnt+=n-k*i+1
        i*=10
    return cnt
s=findPrime(eval(input()))
print("WHUT"+s)
print(count(int(s),eval(input())))