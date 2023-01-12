""" 41m 소요  
시간 오래걸린 이유
1) 끝자리가 0인경우를 생각못했음 
2) 중간숫자가 1일경우를 "1 곱하기"를 해야한다고 착각하고 잇엇음.. 
"""
def main():
    N = int( input() )
  
    L = input().split()
    
    # 최고차항은 1이므로
    answer = 1
    # 두번째 자리부터 계산
    for i in range(1, N):
        if int(L[i]) == 0:
            answer += 2
        elif int(L[i]) == 1:
            answer += 4
        else :
            answer += len(L[i]) + 3
    
    # 끝자리가 0인경우 '=' 입력하고 끝!
    if int(L[-1]) != 0:
        answer += len(L[-1]) + 2
    # 
    else :
        answer += 1
    print(answer)
main()

