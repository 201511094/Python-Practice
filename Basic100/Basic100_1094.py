n = int(input())
list = input().split()
ans = []
for i in range(0,n):
  ans.append(int(list[i]))
for i in range(n-1, -1, -1):
  print(ans[i], end=' ')

#1차원 배열
# for문을 사용하여 배열 요소값을 끝에서부터 출력하기
