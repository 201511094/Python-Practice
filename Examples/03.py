#자료구조
#1. 리스트
#여러 개의 값들을 저장하는 자료구조, 다양한 값을 저장 가능
#Q. 에라토스테네스의 체: 입력값(n)보다 작은 소수를 출력하는 프로그램
#1~n까지 수를 리스트에 저장 -> 모든 배수를 지운 후 남은 수 출력
def erasto(n):
    num = []
    for i in range(1,n+1):
        num.append(i)   #리스트에 넣고
    for i in range(1,n):
        if num[i] < 0:
            continue
        for j in range(i+1, n): #다음 수부터 배수인지 판별
            if num[j] < 0:
                continue
            if num[j]%num[i] == 0:  #배수이면 -1
                num[j] = -1
    for i in range(1,n):
        if num[i]>0:
            print(num[i], end=' ')

#2. 튜플
#리스트와 비슷하지만 값 변경이 불가능한 자료구조
#장점: 값 교환이 간단, 인자 수가 미정인 함수, 2개 이상의 값 리턴 가능
def printArgs(x,y,*args):
    print (x,y,args)

def minmax(*args):
    min = 1001
    max = -1
    for i in args:
        if i<min:
            min = i
        if i>max:
            max = i
    return min, max

#3. 사전
#인덱스가 없는 리스트, key와 value의 나열
#장점: hashtable로 구현됨 -> in 명령은 사전의 크기에 상관없이 일정한 시간이 걸림
mydict = dict()
def add_dict(s1,s2):
    for c in mydict:
        if c==s1:
            print("Cannot add %s" %s1)
            return
    mydict[s1] = s2
def remove_dict(s1):
    del mydict[s1]
def modify_dict(s1,s2):
    for c in mydict:
        if c==s1:
            mydict[s1] = s2
def search_dict(s):
    print(mydict[s])
def print_dict():
    mylist = mydict.keys()
    #mylist.sort()
    for i in mylist:
        print(i, mydict[i])

#Q. 알파벳 카운터
#문자열을 입력받아 알파벳이 나오는 횟수를 출력, 소문자만 세기
def wc(str):
    wdict = dict()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for c in alpha:
        wdict[c] = 0
    for c in str:
        if c in alpha:
            wdict[c] += 1
    for c in alpha:
        print("%c: %d" %(c, wdict[c]))
    
