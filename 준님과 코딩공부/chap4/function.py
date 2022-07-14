# def
'''
def add(a,b):
    return a+b
a = 3
b = 4
c = add(a,b)
print(c)
'''

# def 2
'''
def add(a,b):
    result = a+b
    return result
    
a = add(3,4)
print(a)
'''

# def 3
'''
def say():
    return 'Hi'
a = say()
print(a)
'''

# def 4
'''
def add (a,b):
    print("%d, %d의 합은 %d입니다." % (a,b,a+b))
add (3,4)
a = add(3,4)
print(a)
'''

#def 5
'''
def add(a,b):
    return a+b

result = add (a=3,b=7)
print (result)


result = add(b=5, a=3)
print(result)
'''

'''
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
result = add_many(1,2,3)
print(result)
'''

'''
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i 
    elif choice == "mul":
            result = 1
            for i in args:
                result = result * i
    return result
result = add_mul('add', 1,2,3,4,5)
print(result)
result = add_mul('mul',1,2,3,4,5)
print(result)
'''

'''
def say_myself(name, old, man= True):
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself("박응용", 27)
say_myself("박응용", 27, True)
'''

# vartest. py
'''
a = 1
def vartest(a):
    a = a+1
vartest(a)
print(a)
'''

# vartest_return.py
'''
from pyrsistent import v


a = 1
def vartest(a):
    a = a+1
    return a
a=vartest(a)   
print(a)
'''

