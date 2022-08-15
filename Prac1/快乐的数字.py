def nextNum(n:int):
    t=0
    while n:
        t+=(n%10)**2
        n//=10
    return t
def check(n:int):
    for i in range(1000):
        if n==1:
            return True
        n=nextNum(n)
    return False
print(check(eval(input())))