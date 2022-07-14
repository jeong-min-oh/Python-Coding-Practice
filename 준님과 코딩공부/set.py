'''
s1 = set([1,2,3])
print(s1)
'''

'''
s2 = set('hello')
print(s2)
'''

'''
s1 = set([1,2,3])
l1 = list(s1) / 리스트형으로 만들기
print(l1)
print(l1[0])
t1 = tuple(s1) / 튜플형으로 만들기
print(t1)
print(t1[0])
'''

'''
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1&s2) /s1과 s2의 교집합 구하기
print(s1|s2) /s1과 s2의 합집합 구하기
print(s1-s2)
print(s2-s1) /s1과 s2의 차집합 구하기
'''

'''
s1 = set([1,2,3])
s1.add(4)
print(s1)
'''

'''
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)
'''

'''
s1 = set([1,2,3])
s1.remove(2)
print(s1)
'''