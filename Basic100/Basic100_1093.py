n = int(input())
list = input().split()
ans = []
for i in range(0,24):
  ans.append(0)
for i in range(0,n):
  ans[int(list[i])] += 1
for i in range(1,24):
  print(ans[i], end=' ')
print("\n")

#1차원 배열
# 인덱스 범위 주의
