# print() 함수를 이용한 console 출력 기능에 대해 알아봅니다.

# 기본 기능
# console에 hello 를 출력합니다.
print("hello")

# print('hello')와 print("hello")는 결과값이 동일합니다.

# case 1
print('case 1 :' + 'hello')

# case 2
print('case 2 :' + "hello")

# '' 안의 " 혹은 "" 안의 '는 그대로 출력됩니다.
# case 3
print('case 3 :' + 'hello "안녕하세요"')

# case 4
print('case 4 :' + "hello '안녕하세요'")

# + 를 사용하는 경우 두 단어 사이에 띄어쓰기 없이 출력됨/, 를 사용하는 경우 띄어쓰기가 추가된 상태로 출력됨
# case 5
print('case 5 :' + "H", "ELL", "O")

# case 6
print('case 6 :' + "H" + "ELL" + "O")

# '''''' 또는 """""" 을 사용하는 경우 줄바꿈 이후 여러줄로 출력하는 형태가 가능함
# case 7
print('case 7 :' + '''안녕하세요
오늘은 날씨가 좋네요''')

# case 8
print('case 8 :' + """안녕하세요
오늘은 날씨가 좋네요""")

# \ 를 이용하는 경우 코드를 다음줄에 이어서 입력할 수 있음. 텍스트의 경우 띄어쓰기 없이 이어서 출력됨
# case 9
print('case 9 :' + '안녕하세요'
      "오늘은 날씨가 좋네요")

# format 형식을 이용하여 변수를 바로 출력할 수 있음
# case 10
a = '첫 번째 변수'
b = 2
print('case 10 :' + '1번 변수 : {}, 2번 변수 : {}'.format(a, b))

# case 11
c = '첫 번째 변수'
d = 2
print('case 11 :' + f"1번째 변수 : {c}, 2번째 변수 :{d}")
