# 1) 1부터 100까지의 수 중에서 3의 배수이면서 2의 배수는 아닌 수의 개수를 출력해보세요. 

count=0

for i in range(101):
  if i%3==0 and i%2!=0:
    print(i, end=" ")
    count+=1

print(f"총 {count}개")

# 2) 4자리 비밀번호를 설정하고, 사용자로부터 그 비밀번호가 입력될 때까지 계속 비밀번호를 입력하도록 하는 프로그램을 만들어보세요

from time import sleep

print("비밀번호로 사용할 숫자 4개를 입력하세요.")
password=input("> ")

def isdigit(password):
  try:
    int(password)
    return True
  except: 
    return False

def check_length(password):
  if len(password)==4:
    return True
  else:
    return False

while True:
  if isdigit(password) and check_length(password):
    print("비밀번호가 정상적으로 등록되었습니다.")
    break
  elif isdigit(password) and check_length(password)==False:
    print("자리수가 틀립니다. 숫자 4개를 입력하세요.")
    password=input("> ")
  elif isdigit(password)==False:
    print("숫자가 아닙니다. 숫자 4개를 입력하세요.")
    password=input("> ")

count=0
print("잠금을 풀려면 등록된 비밀번호를 입력하세요.")
unlock=input("> ")

while True:
  if password==unlock:
    print("잠금이 해제되었습니다.")
    break
  else:
    count+=1
    print(f"잘못된 비밀번호를 입력하였습니다. 5회 이상 오류시 10초간 잠깁니다. ({count}회 오류)")
    if count==5:
      print("5회 이상 잘못 입력하였습니다. 10초 후에 다시 시도하세요")
      sleep(10)
    unlock=input("> ")


