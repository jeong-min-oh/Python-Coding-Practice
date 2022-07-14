'''
#1번
from this import d


a = 80
b = 75
c = 55

print((a+b+c)/3)

'''

#2번
'''
number = (int(input("숫자를 입력하세요")))

if number % 2 == 0 :
    print("짝수입니다")
elif number % 2 == 1 :
    print("홀수입니다.")
'''

#3번
'''
pin ="881120-1068234"
yy = "19"
new = yy + pin 
yyyymmdd = print(new[ :8])
num = print(pin[7:])
print(pin[: 6])
print(pin[7:])
'''

#4번
'''
pin = "881120-1068234"
print(pin[7])
'''

#5번
'''
a = 'a:b:c:d'
b = a.replace(':','#')
print(b)
'''

#6번
'''
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)
'''

#7번
'''
a = ['Life', 'is', 'too', 'short']
result = a[0] + a[1] + a[2] +a[3]
print(result)
'''

#8번
'''
a = (1,2,3)
a = list(a) 

print(a)
'''

#9번

#dic()은 변하는 값을 사용할 수 없다.
# 답:3번

#10번
'''
a = {'A': 90, 'B': 80, 'C': 70}
result = a.pop('B')

print(a)
print(result)
'''

#11번
'''
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = (set(a))
print(aSet)
b = list(aSet)
print(b)
'''

#12번
'''
a = b = [1,2,3]
a[1] = 4
print(b)
'''