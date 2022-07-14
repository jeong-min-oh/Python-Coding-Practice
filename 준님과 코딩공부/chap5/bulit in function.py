#abs

#print(abs(-3))

#chr
'''
print(chr(97))
print(chr(48))
'''

#dir

#print(dir([1,2,3]))

#divmod

#print(divmod(7,3))

#enumerate
'''
for i, name in enumerate(['body','foo','bar']):
    print(i,name)
'''

#eval
'''
print(eval('1+2'))
print(eval("'hi'+'a'"))
print(eval('divmod(4,3)'))
'''

#filter
'''
def positive(x):
    return x>0
print(list(filter(positive,[1,-3,2,0,-5,6])))
'''

#hex
'''
print(hex(234))
print(hex(3))
'''

#id
'''
a =3
print(id(3))
'''

#input
'''
a = input()
print(a)
'''
#len

#print(len("python"))

#list

#print(list("python"))

#map

#two  times.py
'''
def two_times(numberlist):
    result =[]
    for number in numberlist:  
        result.append(number*2)
    return result
result = two_times([1,2,3,4])
print(result)
'''

#max
'''
print(max([1,2,3]))
print(max("python"))
'''

#oct

#print(oct(34))

#ord

#print(ord('0'))

#pow
#print(pow(3,3))

#round

#print(round(4.6))

#sorted

#print(sorted([3,1,2]))

