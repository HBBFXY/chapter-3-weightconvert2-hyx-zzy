initial_weight = float(input("请输入您的初始体重(kg):"))
earth_weight = initial_weight
moon_rate = 0.165
print("未来10年地球和月球体重变化情况:")
for year in rage(1,11):
  earth_weight +=0.5
  moon_weight =earth_weight * moon_rate
  print(f"第{year}年:地球体重{earth_weight:.2f}kg,月球体重{moon_weight:.2f}kg")
