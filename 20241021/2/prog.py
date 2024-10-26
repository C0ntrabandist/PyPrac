from math import*
f=c=0
d={}
while (s:=input()):
    if 'quit' in s:
        print(eval(s[4:]).format(f+1, c+1))
        break
    elif s.startswith(':'):
        parts=s[1:].split()
        d[parts[0]]=eval(f"lambda {','.join(parts[1:-1])}: {parts[-1]}")
        f+=1
    else:
        cmd=s.split()
        print(d[cmd[0]](*map(eval, cmd[1:])))
    c+=1
