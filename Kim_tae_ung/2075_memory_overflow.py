# 35m정도 소요했으나, 메모리 사용량 초과
def find_biggest(buffer, N):
    max_value = buffer[0]
    max_index = 0
    
    for i in range(1, N):
        if buffer[i] > max_value:
            max_value = buffer[i]
            max_index = i
    
    # 새로운 값으로 변경
    return max_index
    
    
def main():
    N = int(input())
    L = []
    
    # 각 행별 최대값의 index
    index_list = [N-1 for _ in range(N)]
    for i in range(N):
        buffer = input().split()
        for j in range(N):
            buffer[j] = int(buffer[j])
        L.append(buffer)
    
    # buffer변수는 가장 큰 N개의 변수를 가지고 있다.
    
    for x in range(N-1):
        index = find_biggest(buffer, N)
    
        index_list[index] -= 1
        buffer[index] = L[index_list[index]][index]
        
    index = find_biggest(buffer, N)
    
    print(buffer[index])
    
main()
