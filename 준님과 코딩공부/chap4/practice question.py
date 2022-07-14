# 1번 문제
'''
def is_odd(number):
    if number %2 == 1:
        return True
    else:
        return False
print(is_odd(3))
'''

#4번 문제
# 답 : 3번 : , 를 사용하면 띄어쓰기가 된다.

#6번 문제

user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')
f.write(user_input)
f.write("\n")
f.close()