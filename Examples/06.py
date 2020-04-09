#확장
#1. import (외장함수)
#달력
import calendar
calendar.prcal(2020)    #년도별 달력
calendar.prmonth(2020,4)    #월별 달력
calendar.weekday(2020,4,9)  #요일(월=0, 일=6)
calendar.monthrange(2020,4) #월의 1일의 요일과 월의 날짜 수

#시간
import time
def count():    #1초씩 세는 함수
    for i in range(3):
        print(i+1)
        time.sleep(1)
count()

#웹 브라우저
import webbrowser
#webbrowser.open("http://www.google.com")

#난수 발생
import random
print(random.random())
print(random.randint(1,10))
print(random.choice([1,2,3,4,5]))

#파일로 리스트 만들기
import glob
#glob.glob("C\")    #해당 폴더 아래의 파일들을 리스트로 저장

#시스템 명령
import os
#os.system("dir")


#2. 내장함수: import가 필요하지 않음
print(all([1,2,0])) #하나라도 거짓이면 거짓
print(any([1,2,0])) #하나라도 참이면 참
print(dir([1,2,3])) #객체가 가지고 있는 변수/함수를 리스트 형태로 출력

#enumerate: 시퀀스를 입력받아 enumerate객체를 리턴, 리스트 원소값과 인덱스가 필요한 경우에 사용
for i, name in enumerate(['apple', 'banana', 'pear']):
    print(i, name)

#filter: 함수와 시퀀스형 자료형을 입력받아 참으로 리턴하는 값만 리스트로 저장
def positive(x):
    return x>0
print(list(filter(positive, [1,-1,2,-2,3,-3,0])))

#id: 객체의 고유값을 리턴, 프로그램에서 사용하고 있는 변수가 같은 값을 가리키는지 점검할 때 사용
a = 3
print(id(a))
print(id(3))

#lambda: def와 동일, 복잡하지 않을 때 많이 사용
sum = lambda a,b:a+b

#map: 함수와 반복가능한 자료형을 입력받아 각 요소에 함수를 적용한 결과를 리턴
def two_times(x):
    return 2*x
list(map(two_times, [1,2,3,4]))

#range([start,] stop [,step]): 해당되는 범위의 값을 반복가능한 자료구조로 만들어 리턴
print(list(range(5)))
print(list(range(1,10,2)))


#3. 모듈
#import 명령어를 사용해서 이미 작성한 함수를 불러와 사용 가능
