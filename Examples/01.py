#제어구조: 원하는 결과를 얻기 위해 프로그램의 흐름에 개입하는 구조
#순차/선택/반복

#선택구조 (if)
def comp(a,b):
    if a>b:
        print("%d > %d" %(a,b))
    elif a < b:
        print("%d < %d" %(a,b))
    else:
        print("%d == %d" %(a,b))

#반복구조(while)
def tree(n):
    times=1
    while times <= n:
        if times==1:
            print("Hit a tree %d time." %times)
        else:
            print("Hit a tree %d times." %times)
        if times >= 10:
            break
        times += 1
    if n >= 10:
        print("I can't hit the tree anymore.")
    else:
        print("The tree is falling.")

def odd(n):
    i=1
    while i<=n:
        if i%2 == 1:
            print(i)
        i += 1

def odd2(n):
    i=0
    while i<n:
        i += 1
        if i%2 == 0:
            continue
        print(i)


#함수
def sum(*many):
    sum=0
    for i in many:
        sum += i
    return sum


#클래스: 정보를 담는 틀(template)
#템플릿과 인스턴스
#각각의 인스턴스는 공통 틀을 공유, 틀에 담기는 정보는 각각 다름
#이 다른 정보를 저장하는 변수로 self를 사용함
class calc:
    def __init__(self, name, a, b):
        self.name = name
        self.a = a
        self.b = b
    def add(self):
        return self.a+ self.b
    def sub(self):
        return self.a-self.b
    def mult(self):
            return self.a* self.b
    def div(self):
        return self.a// self.b
    
