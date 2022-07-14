# 전형적인 for문
'''
test_List = ["one","two","three"]
for i in test_List:
    print(i)
'''

# 다양한 for문 사용
'''
a = [(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)
'''

#marks1
'''
marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number+1
    if mark >= 60:
        print("%d번 학생은 합격입니다" % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
'''

#marks2
'''
marks = [90,25,67,45,80]
number = 0
for mark in marks:
    number = number + 1
    if mark<60: continue
    print("%d번 학생 축하합니다. 합격입니다." % number) 
'''

#range 함수
'''
a = range(10)
print(a)

b= range(1,11)
print(b)
'''

#range 함수 예시
'''
add = 0
for i in range(1,11):
    add = add+i
    print(add)
'''

#example
'''
add = 0
for i in range(1,101):
    add = add+ i
    print(add)
'''

#구구단
'''
for i in range(2,10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')
'''

# 리스트 내포
'''
a = [1,2,3,4]
result = []
for num in a :
    result.append(num*3)
print(result)
'''

'''
a = [1,2,3,4]
result = [num *3 for num in a]
print(result)
'''
'''
a = [1,2,3,4]
result = [num *3 for num in a if num %2 == 0]
print (result)
'''
'''
a = "Life is too short, you need python"

if "wife" in a : print("wife")
elif "python" in a and "you" not in a : print("python")
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else: print("none")
'''
'''
from re import I


num = 0
sum= 0
while num <1000:
    num +=1
    if (num%3) != 0: continue
    sum = sum+num
    print(sum)
    '''
'''
i = 0
while True :
     i += 1
     if i>5 :break
     print("*" *i)
'''
'''
for i in range(1,101):
    print(i)
    '''

from numpy import average

'''
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A :
    total += score
average = total/10
print(average)
'''
'''
numbers = [1,2,3,4,5]
result = [n%2 == 1 for n in numbers]
print(result) 
'''