# 강제 형변환의 예시

num = input('정수 입력 : ')
print(type(num))
num = int(num)
print(type(num))
print(num/5)

#입력 할 때 부터 형변환 해서 처리 하는 방법

num = int(input('정수 입력 : '))
print(type(num))
print(num/5)

f1 = float(input('실수 입력 : '))
print(type(f1))
print(f1)

st = str(input('문자열 입력 : '))
print(type(st))
print(st)