w,x,y,z=input().split()
A=int(w)
M=int(x)
D=int(y)
N=int(z)
list=[]
list.append(A)
for i in range(1,N):
  list.append(list[i-1]*M+D)
print(list[N-1])

#수열 규칙을 이용하서 N번째 수 계산하기
# 전 값을 알아야하므로 list에 저장한 후 출력
