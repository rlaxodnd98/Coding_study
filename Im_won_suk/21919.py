import sys

def input():
    return sys.stdin.readline().rstrip()
N = int(input())
arr = list(map(int, input().split()))
inital = 1

def prime_number(N):
    for i in range(2,N):
        if N%i ==0:
            return False
        if i*i > N:
            break

        
    return True
    
for N in arr:
    if prime_number(N):
        inital =  inital * N

if inital ==1:
    print(-1)
else:
    print(inital)