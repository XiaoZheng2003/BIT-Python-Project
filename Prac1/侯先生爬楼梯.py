def solve(n:int):
    if n<3:
        return n
    return solve(n-2)+solve(n-1)
print(solve(eval(input())))