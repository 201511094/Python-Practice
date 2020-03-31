x = int(input())
i = 2
sum = 1

while sum < x:
  if sum+i >= x:
    print(i)
    break
  else:
    sum += i
    i += 1

#1부터 n까지 정수를 계속 더하다가 입력받은 수 이상이 되었을 때 마지막에 더한 정수를 출력하기
# 문제 잘 이해하기 + 부등호 주의
