# 문제
# 호텔 한 층의 높이는 260cm 이다.
# 14개의 층이 있으며 1층 로비의 높이는 500.23cm 라면
# 이 건물의 총 높이는 얼마 일지 소수점 3자리로 출력

# 문제
# 100m 가는데 걸리는 시간이 11.27라면 1시간 후 
# 몇 km를 갈 수 있을 지 소수점 2자리로 출력

# 문제
# # 표준 체중 = (현재키 -100)*0.9
# # 소수점 1자리 까지 반올림 하고 출력

# print("문제1")
# roby=500.23
# floor=260
# hotel = (roby+floor*13)/100
# print(hotel)
# print(f"이 건물의 총 높이는{round(hotel,3)}m입니다")
# print("\n")

# print("문제2")
# #100미터당 11.27초가 걸리는 것을 고려해야됨
# #초당 몇미터 가는지 고려해야된다.
# second_per_Meter=100/11.27
# #print(second_per_Meter)
# #1시간후 거리는 km이고 초당거리에 3600을 곱해준 값
# hour_Killometer=3600*second_per_Meter/1000
# print(f"100미터 가는데 걸리는 시간은 11.27초라면 초당{round(second_per_Meter,2)}m를 가는 것이다.")
# print(f"1시간 후라면 {round(hour_Killometer,2)}km를 갈 수 있다.")
# print("\n")

# print("문제3")
# my_cm=173
# standard=(my_cm-100)*0.9
# print("나의 현재 키는 {}cm이고 표준 체중은 {:.1f}kg이다".format(my_cm,standard))

floor_avg = 260
lobby = 500.23
floor_cnt = 14
sum1 = lobby + (floor_cnt-1)*floor_avg
print("건물의 높이는",(sum1/100),'m 입니다')
print("건물의 높이는 %.3f m 입니다"%(sum1/100))
print("건물의 높이는 {:.3f} m 입니다".format(sum1/100))
print(f"건물의 높이는 {sum1/100:.3f} m 입니다")

print("\n")
hundred = 11.27
time = 60*60
res = time/hundred
meter = res * 100
kilo = meter/1000

print("총 거리는",kilo,"km 입니다")
print("총 거리는 %.2fkm 입니다"%(kilo))
print("총 거리는 {:.2f}km 입니다".format(kilo))
print(f"총 거리는 {kilo:.2f}km 입니다")

print("\n")
height = 173.2
st=(height-100)*0.9

print(round(height,1),'cm의 표준 체중은',round(st,1),'kg 입니다.')
print('%.1f cm의 표준 체중은 %.1f kg 입니다.'%(height,st))
print('{:.1f} cm의 표준 체중은 {:.1f} kg 입니다.'.format(height,st))
print(f'{height:.1f} cm의 표준 체중은 {st:.1f} kg 입니다.')

