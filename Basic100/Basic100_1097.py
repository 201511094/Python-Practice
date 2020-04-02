#1) 2차원배열 초기화
list = []
for i in range(19):
  list.append([])
  for j in range(19):
    list[i].append(0)

#2) 배열을 입력받아 값 복사(**)
# 문제에서 좌표는 1부터 시작이므로 인덱스 접근시 하나 빼는거 잊지 말아야 함
for i in range(19):
  temp = input().split()
  for j in range(19):
    if int(temp[j]) == 1:
      list[i][j] = 1

#3) 십자 뒤집기 기준값을 입력받아 뒤집기
# (1,1)은 실제로 (0,0)이므로 인덱스에서 1 빼서 계산하기
n = int(input())
for i in range(n):
  x,y = input().split()
  for j in range(19):
    if list[int(x)-1][j] == 0:
      list[int(x)-1][j] = 1
    else:
      list[int(x)-1][j] = 0
  for j in range(19):
    if list[j][int(y)-1] == 0:
      list[j][int(y)-1] = 1
    else:
      list[j][int(y)-1] = 0

#4) 완성된 배열 출력
# 배열 범위 조심
for i in range(19):
  for j in range(19):
    print(list[i][j], end=' ')
  print()

#2차원 배열 - 바둑알 십자 뒤집기(**)
