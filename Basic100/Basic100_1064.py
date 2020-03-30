a,b,c = input().split()
x = int(a)
y = int(b)
z = int(c)
num = x if x<y else y
print(num if num<z else z)

#정수 3개 입력받아 가장 작은 수 출력하기
# 파이썬 삼항연산자

a,b,c=map(int, input().split())
ans = a if a<b else b
print(ans if ans<c else c)
