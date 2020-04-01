n = int(input())
list = []
for i in range(20):
  list.append([])
  for j in range(20):
    list[i].append(0)

for i in range(n):
  a,b = input().split()
  x=int(a)
  y=int(b)
  list[x][y] = 1   #list[int(a)][int(b)] = 1과 같음

for i in range(1,20):
  for j in range(1,20):
    print(list[i][j], end=' ')
  print()   #print("\n") 아님

#2차원 배열
# 2차원 배열 생성법 알아두기
# 배열의 인덱스와 출력방식 중요
