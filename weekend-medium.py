# 마름모를 ' * '을 이용해서 출력해보자.
# - 가장 많은 수의 '*' 이 있는 줄의 '*'의 개수가 n이라고 하자.
# - (n은 2 이상의 정수이다)

print("<< 마름모 그리기 >>")

terminate="exit"
print(f"프로그램을 종료하려면 {terminate}을 입력하세요.")
print("-"*40)

def repeat():
  while True:
    user=input("가장 많은 '*'의 개수 입력 > ")

    if user==terminate:
      break
    
    try:
      number=int(user)
      i=1 if number%2==1 else 2

      while i<number:
        blank=' '*((number-i)//2)
        star='*'*i
        print(blank,star)
        i+=2

      while i>0:
        blank=' '*((number-i)//2)
        star='*'*i
        print(blank,star)
        i-=2
    except :
      print("숫자가 아닙니다.")

repeat()