import time
##########################################################
# 만일, 2차원 배열을 초기화 하려면 list comprehension을 사용해야 한다.
matrix2 = [0 for _ in range(3)]
matrix = [[0 for _ in range(3)] for _ in range(3)]

print(matrix)

matrix[-1][-1] = 1

print(matrix)

matrix2 = [0 for _ in range(5)]
####################################################


# set 자료형 알아야 할 점.
#####################################################
"""
set 자료형 특징
1. 중복이 안된다.
2. 순서가 없다.
"""


"""
set 자료형 연산

합집합 a | b
교집합 a & b
차집합 a - b

특정 원소가 존재하는지를 검사
3 in a    # O(1)
"""

"""
집합 자료형 관련 함수
"""
data = set([1, 2, 3])

# 새로운 원소 추가
data.add(4)   # O(1) 

# 새로운 원소 여러개 추가
data.update(5, 6)   # O(1)??

# 특정 값을 갖는 원소 삭제
data.remove(3)      # O(1)
##########################################################
