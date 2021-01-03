# 난이도 중 1

# 집에 있는 소설책이나 유명한 소설의 구절을 이용해 빈칸을 채워넣고 이야기가 말이 되는지 알아봅시다.
# - 입력받을 것: 제목, 동사, 명사, 형용사 등 자유롭게
# - 포맷팅 사용 후 출력

from random import randrange

print("""<< 무작위 소설 생성기 >>
명사, 동사, 부사, 형용사를 입력합니다.
각 품사에 입력하는 단어들은 빈칸으로 구분해 입력하세요.
예) 명사 입력 : 당나귀 영웅 손가락 고양이
""")

noun=list(map(str,input("명사 입력 : ").split()))
verb=list(map(str,input("동사 입력 : ").split()))
adv=list(map(str,input("부사 입력 : ").split()))
adj=list(map(str,input("형용사 입력 : ").split()))

# % 서식문자
print("""
------제목 : %s와 %s에 관한 논고------"""
%(noun[randrange(len(noun))], noun[randrange(len(noun))]))

# format 함수
print("{}와 {}이었던 {}가 {} 오후들을 보내던 나로 하여금 이 이야기를 구상하도록 하는 데 {} {}을 {}.".format(
  noun[randrange(len(noun))],
  noun[randrange(len(noun))],
  noun[randrange(len(noun))],
  adj[randrange(len(adj))], 
  adj[randrange(len(adj))],
  noun[randrange(len(noun))],
  verb[randrange(len(verb))],
))  # 비어있는 {}는 순서대로 출력

print("나는 그 이야기를 쓰게 될 것이고, {1} 방식으로 {0} 하고 있는지도 모른다.".format(
  adv[randrange(len(adv))], # {0}
  adj[randrange(len(adj))]  # {1}
))  # 숫자를 주면 숫자 순서대로 출력

# f-string
print(f"""아직 {noun[randrange(len(noun))]}이나 {noun[randrange(len(noun))]}, {adj[randrange(len(adj))]} {noun[randrange(len(noun))]} 따위가 진척되어 있지는 않다. 
심지어 어떻게 쓸 것인가 결정조차 하지 못하고 있는 부분들도 {verb[randrange(len(verb))]}. 
{noun[randrange(len(noun))]}, 나는 이 이야기를 {noun[randrange(len(noun))]}와 같이 {verb[randrange(len(verb))]}.
{noun[randrange(len(noun))]}은 압제에 시달리고 있지만 {adv[randrange(len(adv))]} 저항을 멈추지 않고 있는 한 나라에서 {verb[randrange(len(verb))]}.
{adj[randrange(len(adj))]} {noun[randrange(len(noun))]}, {adj[randrange(len(adj))]} {noun[randrange(len(noun))]}의 어떤 나라, 또는 {adj[randrange(len(adj))]} {noun[randrange(len(noun))]}의 어떤 나라...
화자가 {adj[randrange(len(adj))]} {noun[randrange(len(noun))]}을 가지고 있기는 하지만 그가 언급하는 사건은 19세기 중엽 또는 초에 {verb[randrange(len(verb))]}.
우리는 그 장소를 {noun[randrange(len(noun))]}라고 하자. 
우리는 그 때를 {noun[randrange(len(noun))]}이라고 하자.
화자는 {noun[randrange(len(noun))]}이라고 불린다. 
그는 {noun[randrange(len(noun))]}의 중손자이다.
""")