# 7개의 수를 입력받고 그 수들의 합을 구하는 프로그램

print("<<총합 구하기 프로그램>>")
terminate="exit"
print(f"프로그램을 종료하려면 {terminate}을 입력하세요.")
print("-"*40)

while True:
  try:
    print("7개의 수를 띄어쓰기로 구분하여 입력하세요.")
    user=input("> ").split()
    print(user)
    if user[0]==terminate:
      break

    numbers=list(map(float,user))
    if len(numbers)>7 or len(numbers)<7:
      print("입력된 숫자의 갯수가 맞지 않습니다. ")
    else:
      print(f"입력한 수 {numbers}의 합은 {sum(numbers)}입니다.")
  except :
    print("숫자가 아닙니다.")
