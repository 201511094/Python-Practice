#Q. 금값 계산
def gold(weight):
    import locale
    locale.setlocale(locale.LC_ALL, '')
    PPG = 41733
    price = weight*1000*PPG
    s = locale.format_string("%d", price, 1)
    print(s)

#Q.시간 계산
def time(sec):
    hour = sec / 3600
    sec = sec % 3600
    minu = sec / 60
    sec = sec % 60
    print("%d hr, %d min %d sec" %(hour,minu,sec))

#Q. 온도 변환
def temp(t):
    state = t[-1]
    t2 = t[:-1]
    a = int(t2)
    if state=="C":
        print("%dC -> %dF" %(a, a*(9.0/5.0)+32.0))
    elif state == "F":
        print("%dF -> %dC" %(a, (a-32)*5/9.0))
    else:
        print("Error")

#Q. 성적 처리
def score(s):
    if s>=90:
        grade='A'
    elif s>=80:
        grade='B'
    elif s>=70:
        grade='C'
    else:
        grade='D'
    print(grade)

#Q. 가위바위보
def rsp():
    import random
    hands = ["rock", "scissors", "papaers"]
    a = random.choice(hands)
    b = random.choice(hands)
    if a == b:
        print("%s vs %s, Draw." %(a,b))
    elif a == "rock" and b == "scissors" or a == "scissors" and b == "papers" or a == "papers" and b == "rock":
        print("%s vs %s, A wins." %(a,b))
    else:
        print("%s vs %s, B wins." %(a,b))
    
#Q. 소수 판정
def prime(n):
    for i in range(2,n):
        if n%i==0:
            print("%d is not a prime number." %n)
            return
    print("%d is a prime number." %n)

def prime2(n):
    import math
    k = int(math.sqrt(n))
    for i in range(2,k):
        if n%i==0:
            print("%d is not a prime number." %n)
            return
    print("%d is a prime number." %n)

#Q. 진수 변환(10->8)
def dec2hex(n):
    hex = ""
    while n>0 :
        k = n%8
        x = ("%d" %k)
        hex = x+hex #문자를 문자열에 하나씩 저장
        n = n//8
    print(hex)

#Q. 삼각형 그리기
#몇 줄인지, 각 줄에 공백과 별의 개수는 몇 개인지?
def triangle(n):
    if n%2==0:
        k = n//2
    else:
        k = n//2 + 1
    for i in range(1,k+1):  #줄 수만큼 반복
        s = n-n//2-i+1  #공백 개수
        t = n-2*(k-i)
        board = ""
        for j in range(1,s):
            board += " "
        for j in range(s,s+t):
            board += "*"
        print(board)

#Q. 버블정렬
def bubbleSort(*args):
    a=[]
    for arg in args:
        a.append(arg)
    n=len(a)
    i = 0
    while i<n-1:
        j=n-2
        while j>= i:
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
            j -= 1
        i += 1
    print(a)

#Q. 소인수분해
def pf(n):
    import math
    k = int(math.sqrt(n))
    primes = []
    i = k
    while i>=1:
        if n%i == 0:
            primes.insert(0,i)  #약수
            if i != n//i:   #제곱이 아니면
                primes.append(n//i)
        i -= 1
    print(primes)
