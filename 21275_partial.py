def power(a, n):
    val = 1
    for i in range(n):
        val *= a
    return val

def cal_num(string, base):
    value = 0

    for i in range(len(string)):
        value += power(base, len(string) - i - 1) * int(dic[string[i]])
    
    return value



x, y = input().split()

string = "0123456789abcdefghijklmnopqrstuvwxyz"
dic = {}

for i in range(len(string)):
    dic[string[i]] = i

min_A, min_B = 36, 36
# 1) min_A 와 min_B를 찾는다
for i in x:
    if min_A > dic[i]:
        min_A = dic[i] + 1
for j in y:
    if min_B > dic[j]:
        min_B = dic[j] + 1


# 2) for i in range(min_A, 37): 와 for j in range(min_B, 37):로 O(n^2)으로 찾는다.
flag = 0
for i in range(min_A, 37):
    num_x = cal_num(x, i)
    for j in range(min_B, 37):
        if i == j:
            continue
        num_y = cal_num(y, j)


        if num_y >= power(2, 63):
            break
        if num_x == num_y:
            if flag == 1:
                flag = 2
                break
            else:
                flag = 1
                X = num_x
                A = i
                B = j
    if flag == 2:
        break

if flag == 0:
    print("Impossible")
if flag == 2:
    print("Multiple")
if flag == 1:
    print("{} {} {}".format(X, A, B))

# 3) 다 찾았을때, 아예 경우의 수가 없으면 impossible, 여러개면 Multiple을 출력한다.





