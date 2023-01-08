# 37m 48s

"""
1024

1) 홀수, 짝수 구분해주어야 하는데 그부분에서 오류가 많음.
2) 짝수 case에서 알고리즘에서 조금 해맸음.
"""
def isodd(a):
    if a % 2 == 1:
        return True
    else :
        return False

def main():
    
    N, L =  input().split()
    N, L = int(N), int(L)
    
    flag = 0
    
    for i in range(L, 101):
        if i % 2 == 1:
            #                  몫     -  (한쪽 팔의 길이)
            if N % i == 0 and (N // i) - (i // 2) >= 0:
                flag = 1
                break
        else:
            #                   (정수center) - (팔의길이)
            if 2*N % i == 0 and isodd(2*N // i) and (N // i) - (i // 2) + 1>= 0:
                flag = 1
                break
    
    if flag == 1:
        if i % 2 == 0:
            start = N // i - (i // 2) + 1 
            end = N // i + (i // 2) 
        else :
            start = N // i - (i // 2)
            end = N // i + (i // 2)
        
        for i in range(start, end + 1):
            
            print("{}".format(i), end=' ')
    else :
        print("{}".format(-1))
    
    
main()
