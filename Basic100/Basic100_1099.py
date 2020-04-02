list=[]
for i in range(10):
  list.append([])
  for j in range(10):
    list[i].append(0)

for i in range(10):
  temp=input().split()
  for j in range(10):
    list[i][j] = int(temp[j])
  
#(1,1) start
sx=1
sy=1
if list[sx][sy] == 2:   #스타트에 먹이가 있는 경우
  list[sx][sy] = 9
else:   #스타트가 0인 경우
  list[sx][sy] = 9
  while True:
  #0은 통로, 1은 벽, 2는 먹이
    #1.끝에 도달하면 끝
    if sx==8 and sy==8:
      break
    #2. 이동중..
    if list[sx][sy+1] == 0: #오른쪽이 통로
      list[sx][sy+1] = 9
      sy += 1
    elif list[sx][sy+1] == 2:   #오른쪽이 먹이
      list[sx][sy+1] = 9
      break
    elif list[sx][sy+1] == 1:   #오른쪽이 벽 -> 아래로 이동
      if list[sx+1][sy] == 0:   #아래칸이 통로면
        list[sx+1][sy] = 9
        sx += 1
      elif list[sx+1][sy] == 2: #아래칸이 먹이면
        list[sx+1][sy] = 9
        break
      else: #아래칸이 벽이면 멈춤
        break
    else:
      break

for i in range(10):
  for j in range(10):
    print(list[i][j], end=' ')
  print()
