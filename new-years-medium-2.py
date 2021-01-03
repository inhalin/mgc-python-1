# 난이도 중 2

# 시간을 분으로, 분을 시간으로 환산해주는 프로그램

print("""[시간 ↔ 분 변환 프로그램]
1 : 시간 → 분
2 : 분 → 시간""")
convertee = int(input("선택하세요(1 또는 2) : "))

while convertee!=1 and convertee!=2:
  print("1 또는 2 중에 입력하세요.")
  convertee = int(input("선택하세요(1 또는 2) : "))

if convertee==1:
  hr=float(input("시간을 입력하세요 : "))
  to_min=int(hr*60)
  print(f"시간을 분으로 환산했습니다.\n{to_min}분입니다.")
elif convertee==2:
  min=float(input("분을 입력하세요 : "))
  to_hr=round(min/60,1)
  print(f"분을 시간으로 환산했습니다.\n{to_hr}시간입니다.")
