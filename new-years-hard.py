# 난이도 상

# 음료수와 잔돈을 반환하는 음료수 자판기
# - 입력으로 음료와 넣을 돈을 받는다.
# - 출력으로 음료의 이름과 남은 돈을 출력한다.

print("[음료 자판기]")

drinks={"콜라":1200,"사이다":1000,"물":500,"커피":1500,"박카스":700}
keys=list(drinks.keys())
values=list(drinks.values())

for i in range(len(keys)):
  print(f"{i+1} : {keys[i]} ({values[i]})")

drink=int(input("원하시는 음료수 번호를 입력하세요 > "))-1
money=int(input("돈을 넣어주세요 > "))

if money>=values[drink]:
  print(f"[{keys[drink]}](이)가 나왔습니다.\n잔돈은 {money-values[drink]}원 입니다.")
else:
  print("돈이 부족합니다.")

