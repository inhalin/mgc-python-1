# 난이도 하

# 객관식 문제로 파이썬 개념 복습하기
# - 조건문을 사용해봅시다.
# - 1번 문제 출력->답 입력 -> 2번 문제 출력->답 입력 -> ... -> 채점 결과 출력

score=0

print("""
1. 다음 중 옳은 것을 하나만 고르시오. (5점)
  파이썬의 자료형에는 ______이 있다.
  1)친척형 2)아는형 3)우리형 4)실수형 5)변수형
""")

answer1=int(input("1번 답의 번호를 적어주세요: "))

while answer1<1 or answer1>5:
  print("잘못된 번호를 입력하였습니다.")
  answer1=int(input("1번 답의 번호를 적어주세요: "))

if answer1==4:
  score+=5

print("""
2. 다음 중 옳은 것을 하나만 고르시오. (5점)
  파이썬의 형변환에는 ______가 있다.
  1)float() 2)stl() 3)florida() 4)ins() 5)sto()
""")

answer2=int(input("2번 답의 번호를 적어주세요: "))

while answer2<1 or answer2>5:
  print("잘못된 번호를 입력하였습니다.")
  answer2=int(input("2번 답의 번호를 적어주세요: "))

if answer2==1:
  score+=5

print(f"""
----채점 결과----
총점은 {score}점입니다.
""")

