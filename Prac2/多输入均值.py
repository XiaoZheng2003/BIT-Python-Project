nl=list(map(eval,input().split()))
ans=0
for num in nl:
    ans+=num
print("{:.1f}".format(ans/len(nl)))