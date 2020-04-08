#재귀: 자기 자신과 같은 형식의 함수를 호출해서 문제를 해결하는 방법
#3원칙: 자기 자신과 같은 형식으로 호출, 문제의 크기가 감소, 끝에는 예외 존재
def rfact(n):
    if n==1:
        return 1
    return n*rfact(n-1)

def ifact(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    print(fact)

#최대공약수
#rgcd(30,12) = 2*rgcd(15,6) ...
def rgcd(a,b):
    if a<b:
        a,b = b,a
    for i in range(2,b+1):
        if a%i==0 and b%i==0:
            return i*rgcd(a//i, b//i)
    return 1

#피보나치 수열
#rfib(n) = rfib(n-1)+rfib(n-2)
def rfib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return rfib(n-1)+rfib(n-2)

def ifib(n):
    fib=[]
    fib.append(0)
    fib.append(1)
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n-1]

#수열의 합
#Sn = a1+a2+...+an
def iterative_sum(a,low,high):
    sum=0
    for i in range(low,high):
        sum+=a[i]
    return sum

def recursive_sum(a,low,high):
    if low==high:
        return a[low]
    return a[low]+recursive_sum(a,low+1,high)

#하노이의 탑
#h(n) = h(n-1)+1+h(n-1) = 2*h(n-1)+1
def rHanoi(n):
    if n==1:
        return 1
    return 2*rHanoi(n-1)+1

def iHanoi(n):
    h=[]
    h.append(1)
    for i in range(1,n):
        h.append(2*h[i-1]+1)
    return h[n-1]

#정렬된 리스트의 합병
#2개의 정렬된 리스트를 입력받아 둘을 합친 정렬된 리스트를 출력
def merge(A,B):
    C = []
    n=len(A)
    m=len(B)
    idxA=0
    idxB=0
    while idxA<n and idxB<m:
        if A[idxA] <= B[idxB]:
            C.append(A[idxA])
            idxA += 1
            continue
        if A[idxA] > B[idxB]:
            C.append(B[idxB])
            idxB += 1
            continue
    while idxA<n:
        C.append(A[idxA])
        idxA += 1
    while idxB<m:
        C.append(B[idxB])
        idxB += 1
    return C

def rmerge(A,B):
    C = []
    if len(A)==0:
        return B
    if len(B) == 0:
        return A
    if A[0]<B[0]:
        C.append(A[0])
        A.remove(A[0])
        D = rmerge(A,B)
        C.extend(D)
    else:
        C.append(B[0])
        B.remove(B[0])
        D = rmerge(A,B)
        C.extend(D)
    return C

#애너그램: 단어/문장을 이루는 문자 위치를 바꿔서 새로운 단어/문장을 만드는 문자 퍼즐
#주어진 두 문자열이 애너그램인지 확인하는 프로그램
def anagrams(a,b):
    listA=list(a)
    listB=list(b)
    listA.sort()
    listB.sort()
    flag =True
    if len(listA) == len(listB):
        for i in range(0, len(listA)):
            if listA[i] != listB[i]:
                flag = False
                break
    else:
        flag = False
        
    if flag == False:
        print("Not anagram")
    else:
        print("Anagram")
