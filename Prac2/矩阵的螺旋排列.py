def SpiralOrder(matrix):
    ans=[]
    try:
        while True:
            ans+=matrix.pop(0)
            for line in matrix:
                ans.append(line.pop())
            ans+=matrix.pop()[::-1]
            for line in matrix[::-1]:
                ans.append(line.pop(0))
    except:
        return ans
matrix=eval(input())
res=SpiralOrder(matrix)
print(res)