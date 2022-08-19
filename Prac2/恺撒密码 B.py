s=input()
for c in s:
    if c>='a' and c<='z':
        print(chr((ord(c)-ord('a')+3)%26+ord('a')),end='')
    elif c>='A' and c<='Z':
        print(chr((ord(c)+ord('A')+3)%26+ord('A')),end='')
    else:
        print(c,end='')