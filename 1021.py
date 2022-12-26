def abs(a):
    if a > 0:
        return a
    else:
        return -a

    
def distance(N, start, end):
    if N - abs(start - end) > abs(start-end):
        return abs(start - end)
    else:
        return N - abs(start - end)
        
def main():
    N, M = input().split()
    N = int(N)
    M = int(M)
    
    L = list(input().split())
    for i in range(len(L)):
        L[i] = int(L[i])
    
    L.insert(0, 1)
    # return value
    answer = 0
    
    while len(L) != 1:   # infinite loop until L is empty
        answer += distance(N, L[0], L[1])
        N -= 1
        del L[0]
        for i in range(len(L)):
            if L[i] > L[0]: 
                L[i] -= 1
    
    print(answer)

        
    
main()
