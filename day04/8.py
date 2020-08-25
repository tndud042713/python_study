# 문제
# 나이 계산하는 프로그램
# 이름 / 올해의 년도 / 태어난 년도를 입력받기
# 이름과 현재 나이를 출력

# 문제
# 표준 체중 = (현재키 - 100)*0.9
# 이름 현재키를 입력 받아서 표준체중을 출력

#한국식 나이를 기준으로 출력하였음
name = input('이름을 입력 하시오 : ')
year = int(input('현재의 해를 입력하시오 : '))
birth_year = int(input('태어난 해를 입력하시오 : '))
age = year-birth_year+1
print(f"이름은 {name}이고, 현재는 {year}년이고 태어난 년도는 {birth_year}년 이다. 현재 나이는 {age}살이다")
print("이름은 {}이고, 현재는 {}년이고 태어난 년도는 {}년 이다. 현재 나이는 {}살이다".format(name,year,birth_year,age))
print("이름은 %s이고, 현재는 %d년이고 태어난 년도는 %d년 이다. 현재 나이는 %d살이다"%(name,year,birth_year,age))


print("\n")

h = float(input("키 : "))
st = (h-100)*0.9
print(f"이름은 {name}이고, 표준체중은 {st:.1f}kg이다")
print("이름은 {}이고, 표준체중은 {:.1f}kg이다".format(name,st))
print("이름은 %s이고, 표준체중은 %.1fkg이다"%(name,st))




