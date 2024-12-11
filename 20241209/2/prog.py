import math, sys

p, v, l = [], {}, {}
ops, cmp = {'add','sub','mul','div'}, {'ifeq','ifne','ifgt','ifge','iflt','ifle'}

for line in sys.stdin.readlines():
    s = line.strip().split()
    if not s: continue
    if s[0].endswith(':'):
        l[s[0][:-1]] = len(p)
        s = s[1:]
        if not s: continue
    if not s: continue
    cmd = s[0]
    if cmd == 'stop':
        p.append(['stop'])
    elif cmd == 'store':
        p.append(['store', s[1], s[2]])
    elif cmd in ops or cmd in cmp:
        p.append(s)
    elif cmd == 'out':
        p.append(['out', s[1]])

for ins in p:
    if ins[0] in cmp and ins[3] not in l:
        exit()

i = 0
while i < len(p):
    ins = p[i]
    op = ins[0]
    if op == 'stop':
        break
    elif op == 'store':
        try:
            v[ins[2]] = float(ins[1])
        except:
            pass
        i +=1
    elif op in ops:
        a, b = v.get(ins[1],0), v.get(ins[2],0)
        if op == 'add': v[ins[3]] = a + b
        elif op == 'sub': v[ins[3]] = a - b
        elif op == 'mul': v[ins[3]] = a * b
        elif op == 'div':
            v[ins[3]] = a / b if b != 0 else math.inf
        i +=1
    elif op in cmp:
        a, b = v.get(ins[1],0), v.get(ins[2],0)
        jump = False
        if (op == 'ifeq' and a == b) or \
           (op == 'ifne' and a != b) or \
           (op == 'ifgt' and a > b) or \
           (op == 'ifge' and a >= b) or \
           (op == 'iflt' and a < b) or \
           (op == 'ifle' and a <= b):
            i = l.get(ins[3], len(p))
            jump = True
        if not jump:
            i +=1
    elif op == 'out':
        print(v.get(ins[1],0))
        i +=1
    else:
        i +=1
