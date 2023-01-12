import sys
input = sys.stdin.readline

a = []
for _ in range(int(input())):
    s = input().rstrip()
    
    summ = 0
    for i in s:
        if i.isdigit():
            summ += int(i)
    a.append((s,summ))
    
a.sort(key=lambda x:(len(x[0]),x[1],x[0]))

for i in a:
    print(i[0])