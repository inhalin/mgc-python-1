# 시험 점수를 입력받아 
# 90 ~ 100점은 A, 
# 80 ~ 89점은 B, 
# 70 ~ 79점은 C, 
# 60 ~ 69점은 D, 
# 나머지 점수는 F를 출력하는 프로그램을 작성하시오

print("<< 성적 산출 프로그램 >>")
print("-"*40)
print("프로그램을 종료하려면 exit를 입력하세요.")
terminate='exit'

while True:
  score=input("시험점수를 입력하세요 > ")

  if score=="exit":
    break

  if int(score)<0 or int(score)>100:
    print("잘못 입력했습니다.")
  elif 90<=int(score):
    print("당신의 학점은 A입니다.")
  elif 80<=int(score):
    print("당신의 학점은 B입니다.")
  elif 70<=int(score):
    print("당신의 학점은 C입니다.")
  elif 60<=int(score):
    print("당신의 학점은 D입니다.")
  else:
    print("당신의 학점은 F입니다.")