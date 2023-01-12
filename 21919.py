"""
43m 25s

1) DP(?)를 사용함
--> prime_number에 대한 list를 쫙 적고..
--> 그 list에 해당하는 





"""
def isprime(a):

    flag = 1
    if a == 2:
        return True
    for i in range(3, a+1, 2):
        if a % 2 == 0:
            flag = 0
            break
        if i ** 2 > a:
            break
        if a % i == 0:
            flag = 0
            break
    if flag:
        return True
    else:
        return False
    
N = int( input() )
A = input().split()

# find max_number
# O(n^2)
max_A = 0
L = []
for i in range(len(A)):
    A[i] = int(A[i])

    # 중복 걸러내기
    if A[i] not in L:
        L.append(A[i])
        
    if max_A < A[i]:
        max_A = A[i]
        

# prime_number값의 list 저장

prime = [2]

for i in range(3, max_A+1, 2):
    if isprime(i):
        prime.append(i)


# 소수들만 변별.
prime_list = []
val = 1
for i in range(len(L)):
    if L[i] in prime:
        if L[i] in prime_list:
            continue
        else :
            val *= L[i]

if val == 1:
    print(-1)
else :
    print(val)
