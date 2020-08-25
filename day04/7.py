# 문제
# su1 = 100
# num2 = '100'
# flt = '123.123'

# [출력내용]
# su1 + num1 = 200
# su1 + flt = 223.123
# su1 + num1 = 100100
# num1 + flt = 100123.123

su1 = 100
num1 = '100'
flt = '123.123'

print(f'su1 + num1 = {su1+int(num1)}')
print(f'su1 + flt = {float(su1)+float(flt)}')
print(f'su1 + num1 = {str(su1)+num1}')
print(f'num1 + flt = {num1+str(flt)}')