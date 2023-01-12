# 26m 15s

### 배운 내용 정리!
""" sorting 하는 방법!

1) sort method 사용

num_list = [1, 5, 3, 7]   # list example
num_list.sort()           # default값은 오름차순

2) sorted 함수 사용
num_list = [1, 5, 3, 7]      # list example
num_list = sorted(str_list)  # default값은 오름차순

3) parameter
sort, sorted함수 모두 key와 reverse 매개변수를 가지고 있다.

3-1) reverse
num_list = [1, 5, 3, 7]
num_list.sort(reverse=True)  # 내림차순으로 정렬

num_list = sorted(num_list, reverse=True)

3-2) key
정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 넣을수도 있다

tuple_list = [('좋은하루', 0),
    	      ('niceday', 1), 
    	      ('좋은하루', 5), 
    	      ('good_morning', 3), 
    	      ('niceday',5)]

tuple_list.sort(key=lambda x: x[1])  # 이렇게 lambda 함수를 이용하여 정렬 가능함
tuple_list.sort(key=len)             # 길이를 이용하여 정렬

정렬 순서가 여러개일때 사용하는 것.
tuple_list.sort(key=lambda x: (x[0], -x[1]))   
# lambda함수의 반환값은 tuple과 list 모두 가능하다고 함
# tuple 객체를 비교하는 방법을 비교하는것을 이해해야함!
# (1st_element, 2nd_element, ...) tuple을 비교할때는 첫번째, 두번째 함수.. 등으로 비교!





L = sorted(L, key=len)
과 같은 함수등으로 정렬이 가능함.


"""
def isdigit(num):
    if "0" <= num and "9" >= num:
        return True
    else: 
        return False

def hap(string):
    sum = 0
    for i in string:
        if isdigit(i):
            sum += int(i)
    return sum

N = int( input() )
L = []

# 저장 단계
for i in range(N):
    string = input()
    L.append( [string, len(string), hap(string)] )
    

# 정렬 단계
L_sort = sorted(L, key = lambda x: (x[1], x[2], x[0]))

for i in range(N):
    x = L_sort[i]
    print(x[0], end=' ')
