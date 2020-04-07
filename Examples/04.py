#입출력
a = input("Write something: ")
print(a)

def inf_input():
    while True:
        data=input()
        if not data:
            break
        print(data)

#알고리즘
#탐색: 주어진 집합에서 내가 찾는 원소가 포함되어 있는지 판단하는 연산, 또는 그 원소의 인덱스를 찾는 연산
#1. 선형탐색 -> 정렬되지 않은 리스트
def linear_search(l, x):
    list = []
    for i in range(len(l)):
        list.append(l[i])
    for i in range(len(list)):
        if list[i] == x:
            print("Found")
            return
    print("Not found")

#2. 이진탐색 -> 정렬된 리스트에서만
def binary_search_init(l, x):
    list = []
    for i in range(len(l)):
        list.append(l[i])
    low = 0
    high = len(list)-1
    binary_search(list, x)
    binary_search2(list,x,low,high)

def binary_search(list,x):
    low = 0
    high = len(list)-1
    while low<high:
        mid = (low+high)//2
        if list[mid] == x:
            print("Found, %d" %mid)
            return
        if x<list[mid]:
            high = mid-1
        else:
            low = mid+1
    if list[low] == x:
        print("Found: %d" %low)
    else:
        print("Not found")

def binary_search2(list, x, low, high):
    if low==high:
        if list[low] == x:
            print("Found: %d" %low)
            return
        else:
            print("Not found")
    mid = (low+high)//2
    if list[mid] == x:
        print("Found: %d" %mid)
        return
    if x<list[mid]:
        binary_search2(list,x,low,mid-1)
    else:
        binary_search2(list,x,mid+1,high)

#3. 보간탐색
#이진탐색과 비슷하지만 mid를 계산하는 방식이 다름
def int_sch(list,x):
    cnt = 1
    low = 0
    high = len(list)-1
    while low<high:
        mid = low+(x-list[low])*(high-low)//(list[high]-list[low])
        if mid<low or mid>high:
            break
        if list[mid] == x:
            print("Found: %d, %d" %(mid, cnt))
            return
        if x<list[mid]:
            high = mid-1 #앞에서 찾기
        else:
            low = mid+1 #뒤에서 찾기
        cnt += 1
    if low >= len(list):
        print("Not found")
        return
    if list[low] == x:
        print("Found:%d, %d" %(low,cnt))
    else:
        print("Not found")

#4. 삽입정렬
#삽입연산: 정렬된 리스트에 새로운 원소를 추가하면서 정렬 상태를 유지하는 연산
def insert(list,key):
    i = 0
    keyX = 0
    n = len(list)
    while i<n:
        if list[i]>=key or list[i]<0:
            keyX = i
            break
        i += 1
    j = n-1
    while j>keyX:
        list[j] = list[j-1]
        j -= 1
    list[keyX] = key
    return list

def insertion_sort(a):
    n = len(a)
    b = list()
    i  = 0
    while i<n:
        b.append(-1)
        i += 1
    b[0] = a[0]
    i = 1
    while i<n:
        insert(b, a[i])
        i += 1
    print(b)
