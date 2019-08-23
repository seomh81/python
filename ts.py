input_name = input("이름을 입력해주세요(영문)")
input_age = input("나이를 입력해주세요(숫자)")

def pr_name(name,age):
  print('사용자의 이름은 '+name+' 입니다.')
  print('사용자의 나이는 '+age+' 입니다.')
pr_name(input_name,input_age)
