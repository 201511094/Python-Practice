w,x,y,z = input().split()
h=int(w)
b=int(x)
c=int(y)
s=int(z)
ans = h*b*c*s/8/1024/1024
print("%.1f MB" %ans)

#소리파일 저장용량 계산하기
# bit -> byte -> KB -> MB
