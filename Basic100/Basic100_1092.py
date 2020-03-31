x,y,z=input().split()
a=int(x)
b=int(y)
c=int(z)
day=1
while(day%a != 0 or day%b != 0 or day%c != 0):
  day += 1
print(day)

#최소공배수
# while문 안의 조건을 알아두기
