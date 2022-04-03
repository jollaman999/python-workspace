'''
변수명 정하기
 1) 영문과 숫자, _ 로 이루어진다.
 2) 대소문자를 구분한다.
 3) 문자나, _ 로 시작한다.
 4) 특수문자를 사용하면 안된다. (&, % 등)
 5) 키워드를 사용하면 안된다. (if, for 등)
'''

a=1
print(a)
A=2
c=3
_b=4
# 2b=5
print(a, A, c, 4)
a, b, c=3, 2, 1
print(a, b, c)

# 값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 타입
a=1234538402389408304810980814908239048209840938402380942890428309
print(type(a))
a=12.123456789123456789
print(a) # 실수형은 8바이트까지 차지가능
a='student'
print(a)

# 출력방식
print("number")
a, b, c=1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
print(a, b, c, sep=', ')
print(a, b, c, sep=',')
print(a, b, c, sep='')
print(a, b, c, sep='\n')
print(a, end=' ')
print(b, end=' ')
print(c, end=' ')

'''
변수입력과 연산자
'''
# a=input("슷자를 입력하세요 : ")
# print(a)
# a, b = input("숫자를 입력하세요 : ").split()
print(a+b) # 문자형으로 나옴
a=int(a)
b=int(b)
print(a+b) # 정수형으로 나옴
# a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) # 몫
print(a%b) # 나머지
print(a**b) # 거듭제곱
a=4.3
b=5
c=a+b
print(c, type(c))

'''
조건문 if(분기, 중첩)
'''
x=5
if x!=7:
   print("Lucky")
   print("ㅋㅋ")

x=12
if x>= 10:
    if x%2==1:
        print("10이상의 홀수")

x=9
if x>0:
    if x<10:
        print("10보다 작은 자연수")

x=7
if x>0 and x<10:
    print("10보다 작은 자연수")

x=7
if 0<x<10:
    print("10보다 작은 자연수")

x=-3
if x>0:
    print("양수")
else:
    print("음수")

x=50
if x>=90:
    print("A")
elif x>=80:
    print("B")
elif x>=70:
    print("C")
elif x>=60:
    print("D")
else:
    print("F")

'''
반복문 (for, while)
'''
a=range(10)
print(list(a))
a=range(1, 11)
print(list(a))

# for i in range (10):
#     print("hello")
# for i in range (10):
#     print(i)
# for i in range (1, 11):
#     print(i)
# for i in range(10, 0): # 아무일도 일어나지 않는다.
#     print(i)
# for i in range(10, 0 ,-1):
#     print(i)

# i=1
# while i<=10:
#     print(i)
#     i=i+1
# i=10
# while i>=1:
#     print(i)
#     i=i-1
# i=1
# while True:
#     print(i)
#     if i==5:
#         break
#     i+=1

for i in range (1, 11):
    if i%2==0:
        print(i, "넌 짝수임")
        continue
    print(i)

for i in range (1, 11):
    print(i)
    if i>15:
        break
else:
    print(11)

'''
반복문을 이용한 문제풀이
1) 1부터 N까지 홀수출력하기
2) 1부터 N까지의 합 구하기
3) N의 약수출력하기
'''

# n = int(input("수를 입력하시오: "))
# for i in range(1, n+1):
#     if i%2 != 0:
#         print(i, end= ' ')
# else:
#     print('\n')
#
# n = int(input("수를 입력하시오: "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# else:
#     print(sum)
#
# n = int(input("수를 입력하시오: "))
# for i in range(1, n+1):
#     if n%i == 0:
#         print(i, end=' ')

'''
중첩 반복문(2중 for문)
'''
for i in range(5):
    print('i:', i, sep='', end=' ')
    for j in range(5):
        print('j:', i, sep='', end=' ')
    print()

for i in range(5):
    for j in range(5):
        print('*', end=' ')
    print()

for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    print()

for i in range(5):
    for j in range(5-i):
        print('*', end=' ')
    print()

'''
문자열과 내장함수
'''
msg="It is Time"
print(msg.upper())
print(msg.lower())
print(msg)
tmp=msg.upper()
print(tmp)
print(tmp.find('T'))
print(tmp.count('T'))
print(msg)
print(msg[:2])
print(msg[3:5])
print(msg[tmp.find('S'):len(msg)])
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.isupper():
        print(x, end= ' ')
print()

for x in msg:
    if x.islower():
        print(x, end= ' ')
print()

for x in msg:
    if x.isalpha(): # 알파벳이냐?
        print(x, end= '')
print()

tmp='AZ'
for x in tmp:
    print(ord(x)) # ASCII Number 출력

tmp='az'
for x in tmp:
    print(ord(x)) # ASCII Number 출력

tmp=65
print(chr(tmp)) # ASCII Number를 문자로 출력

'''
리스트와 내장함수(1)
'''
import random as r
b=list()
print(b)

a=[1, 2, 3, 4, 5]
print(a)
print(a[0])

b=(list(range(1, 11)))
print(b)

c=a+b
print(c)

print(a)
a.append(6)
print(a)

a.insert(3, 7)
print(a)

a.pop()
print(a)
a.pop(3)
print(a)

a.append(4)
print(a)
a.remove(4) # 첫번째만 없어진다.
print(a)

print(a.index(5))

a=list(range(1, 11))
print(a)
print(sum(a))
print(max(a))
print(min(a))
print(min(7, 5))
print(min(7, 3, 5))
print(a)
r.shuffle(a)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.sort()
print(a)
a.clear()
print(a)

'''
리스트와 내장함수(2)
'''
a=[23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

for x in a:
    if x%2==1:
        print(x, end=' ')
print()

for x in enumerate(a): # 인덱스 값과 값을 튜플 (0, 23) 로 출력한다
    print(x)

b=(1, 2, 3, 4, 5) # 튜플
print(b[0])
# b[0]=7 # 튜플은 값을 바꿀수 없다.

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

# 모든 값이 조건이 맞으면 True
# 그렇지 않으면 False를 리턴함
if all(60>x for x in a):
    print("YES")
else:
    print("NO")

# 하나 라도 조건이 만족 되면 True
if any(11>x for x in a):
    print("YES")
else:
    print("NO")

'''
2차원 리스트 생성과 접근
'''
a=[0]*3
print(a)

a=[[0]*3 for _ in range(3)]
print(a)
a[0][1]=1
print(a)
a[1][1]=2
print(a)

for x in a:
    print(x)

for x in a:
    for y in x:
        print(y, end=' ')
    print()

'''
함수 만들기
'''
def add(a, b):
    c=a+b
    print(c)

add(3, 2)
add(5, 7)

def add(a, b):
    c=a+b
    return c

print(add(3, 2))
x=add(3, 2)
print(x)

def add(a, b):
    c=a+b
    d=a-b
    return c, d
print(add(3, 2))

def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True
a=[12, 13, 7, 9, 19]
for y in a:
    if isPrime(y):
        print(y, end=' ')