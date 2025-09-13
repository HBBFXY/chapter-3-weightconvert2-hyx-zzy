initial_weight = float(input("请输入您的初始体重(kg):"))

for year in rage(1,11):
  earth_weight = initial_weight + year *0.5
  moon_weight =earth_weight * 0.165
  print(f"第{year}年,地球上的体重:{earth_weight:.2f}kg,月球上的体重:{moon_weight:.2f}kg")
