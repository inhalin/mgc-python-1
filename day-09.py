# 입력된 연도가 윤년인지 아닌지 판단하는 프로그램
# 1. 연도가 4로 나누어 떨어지는 해는 윤년이다.
# 2. 그 중 100으로 나누어 떨어지는 해는 윤년이 아니다.
# 3. 400으로 나누어 떨어지는 해는 무조건 윤년이다.

print("<<윤년 판별 프로그램>>")
print("-"*40)
print("프로그램을 종료하려면 exit를 입력하세요.")
terminate='exit'

while True:
  year=input("연도를 입력하세요 > ")
  if year=="exit":
    break

  try:
    if int(year)%4==0 and int(year)%100!=0:
      print(f"{year}년은 윤년입니다.")
    elif int(year)%400==0:
      print(f"{year}년은 윤년입니다.")
    else:
      print(f"{year}년은 윤년이 아닙니다.")
  except :
    print("잘못 입력하였습니다.")

