## remove multiple values in O(N) time complex

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않는 값만을 저장.
result = [i for i in a if not in remove_set]
print(result)

# 내가 예전에 작성했던 안좋은 예시
# O(N^2)의 알고리즘으로 동작한다.
while 3 in a:   # O(N)
  a.remove(3)   # remove 함수는 기본적으로 O(N)
while 5 in a:
  a.remove(5)
  
