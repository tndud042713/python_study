# 문제
# 11개의 지하철역을 지나왔다
# 출발에서 도착까지의 시간은 37분이 소요되었다.
# 한역을 지날 때 마다 걸린 시간의 평균 시간을 구하세요
# 소수점은 2자리까지만 출력
# 계산은 변수 이용해서 해 보세요!

station=11
time=37
avg=time/station

print("한 역을 지날 때 마다의 평균 시간은 {}분이다".format(round(avg,2)))
print(f"한 역을 지날 때 마다의 평균 시간은 {round(avg,2)}분이다")
print("한 역을 지날 때 마다의 평균 시간은 %4.2f분이다"%round(avg,2))

print("%d 개의 역을 지난 시간은 %d 분이고, 한 역을 지나는 시간은 %.2f 분 입니다."%(station,time,avg))
print("{} 개의 역을 지난 시간은 {} 분이고, 한 역을 지나는 시간은 {:.2f} 분 입니다.".format(station,time,avg))
print(f"{station}개의 역을 지난 시간은 {time} 분이고, 한 역을 지나는 시간은 {round(avg,2)} 분 입니다.")