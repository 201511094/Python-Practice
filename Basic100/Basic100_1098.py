h,w = input().split() #세로(x),가로(y)
H = int(h)
W = int(w)
n = int(input()) #막대개수

list = []
for i in range(H):
  list.append([])
  for j in range(W):
    list[i].append(0)

for i in range(n): #막대개수만큼 반복
  #각 막대 길이(l), 방향(d,가로0/세로1), 좌표(x,y)
  l,d,x,y = input().split()
  l = int(l)
  d = int(d)
  x = int(x)
  y = int(y)
  if d == 0:  #가로방향
    for j in range(l):
      list[x-1][y+j-1] = 1
  else: #세로방향
    for j in range(l):
      list[x+j-1][y-1] = 1

for i in range(H):
  for j in range(W):
    print(list[i][j], end=' ')
  print()
