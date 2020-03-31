list = input().split()
for i in list:
  if int(i) == 0:
    break
  else:
    print(i)

#0이 입력될 때까지 무한 출력하기

a = input().split()
b = map(int, a)
# 입력받을 때 위와 같은 코드를 사용해도 ok
