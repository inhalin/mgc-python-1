strings=("12345","12345678","00000000011","00000000000000017","123456789")
count_len={}

for i in range(len(strings)):
  count_len[f"{i}번째 문자열 길이"]=len(strings[i])

print(count_len)