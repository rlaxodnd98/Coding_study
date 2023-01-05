# 10m 정도
N = int(input())
L = []
    

# 메모리 사용량 줄이기 위해, 절반씩만 사용
# sorted함수를 사용해서 제일 큰것 N개만 추려냄
for i in range(N // 2):
    buffer = input().split()
    for j in range(N):
        L.append( int(buffer[j]) )
    L = sorted(L, reverse=True)[0:N]
    
for i in range(N//2, N):
    buffer = input().split()
    for j in range(N):
        L.append( int(buffer[j]) )
    L = sorted(L, reverse=True)[0:N]
    
print(L[-1])
