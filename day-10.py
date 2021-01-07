# 정수를 한 개 입력받고, 해당 정수가 짝수인지 홀수인지 판단하는 함수
import sys

print("<<짝수/홀수 판별 프로그램>>")
print("-"*40)

terminate="exit"
print(f"프로그램을 종료하려면 {terminate}을 입력하세요.")

def isEven(a):
  try:
    if int(a)%2==0:
      print(f"{a}은(는) 짝수입니다.")
    else:
      print(f"{a}은(는) 홀수입니다.")
  except:
    print("숫자가 아닙니다.")

def repeat():
  user=input("숫자를 입력하세요 > ")
  while True:
    if user==terminate:
      sys.exit()
    else:
      isEven(user)
      repeat()

repeat()

