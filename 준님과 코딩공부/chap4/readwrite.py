# 파일 쓰기 모드로 열어 출력값 적기
# writedata.py
'''
f = open ("C:/Users/dhwjd/Desktop/준님과 코딩공부/chap4/새파일.txt", "w")
for i in range(1,11):
    data =  " %d번째 줄입니다.\n" % i
    f. write(data)
f.close() 
'''

#read함수 사용하기
'''
f = open ("C:/Users/dhwjd/Desktop/준님과 코딩공부/chap4/새파일.txt", "r")
data = f.read()
print(data)
f.close()
'''

#adddata.py
'''
f  = open("C:/Users/dhwjd/Desktop/준님과 코딩공부/chap4/새파일.txt", "a")
for i in range(11,20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()
'''

