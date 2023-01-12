def main():
  T = int(input())
  input_list = []
  for i in range(T):
    input_list.append(int(input()))
  max_value = max(input_list)
  L = {}
  L[0] = [1, 0]
  L[1] = [0, 1]

  for i in range(2, max_value+1):
    L[i] = [L[i-1][0] + L[i-2][0] , L[i-1][1] + L[i-2][1]]

  for j in input_list:
    print( L[j][0], end='')
    print(" ", end='')
    print( L[j][1])

main()