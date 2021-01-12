print("<< Simple Calculator using Function >>")

terminate="exit"
print(f"프로그램을 종료하려면 {terminate}을 입력하세요.")
print("-"*40)

def calc(string):
  try:
    print(round(eval(string)))
  except:
    print("연산이 불가합니다. 숫자와 연산자만 입력하세요")

def repeat():
  while True:
    user=input("> ")
    if user==terminate:
      break
    else:
      calc(user)

repeat()
