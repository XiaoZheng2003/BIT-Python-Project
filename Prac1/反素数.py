def reverse(n:int):
    m=0
    while n:
        m=m*10+n%10
        n//=10
    return m
def isPrime(n:int):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def check(n:int):
    m=reverse(n)
    return m!=n and isPrime(n) and isPrime(m)
n=eval(input())
t=13
while n:
    if check(t):
        print(t,end=' ')
        n-=1
    t+=1