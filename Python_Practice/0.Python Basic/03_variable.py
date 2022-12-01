# 변수를 선언하는 방법에 대해서 확인합니다``

# 기본 기능
a = 10
b = '안녕하세요'
c = True
# 각 변수의 자료형에 대해 알아보기 위한 print()
print(f'각 변수의 타입 | a : {type(a)}, b : {type(b)}, c : {type(c)}')

# case 1
# 두 개의 int 형 변수를 선언한 후 연산하여 출력
val_1 = 10
val_2 = 20
print('case 1 :',
      f'두 변수의 합 : {val_1 + val_2}, 두 변수의 합의 타입 : {type(val_1 + val_2)}')

# case 2
# str 형 변수를 선언하여 위의 변수와 + 연산 수행
# str 형 변수와 int 형 변수 사이에는 + 연산이 불가능하다. 따라서 오류를 출력한다.
val_3 = '30'

try:
    print('case 2-1 :', val_1 + val_2 + val_3)
except Exception as e:
    print('case 2-2 :', e)

# case 3
# str 형 변수를 int 형을 변환하여 + 연산 수행
# 이 경우는 정상적으로 출력이 된다
print('case 3 :', val_1 + val_2 + int(val_3))

# case 4
# int 형을 문자형으로 변환하여 출력
print('case 4 :', str(val_1 + val_2) + val_3)

# case 5
# int 형과 float 형을 연산하는 경우 int 형을 자동으로 float 형으로 변환하여 계산함
# int 형 변수를 영구적으로 float 형으로 변환하는 것이 아니므로 다시 연산할 때는 int 형으로 연산함
val_4 = 3.14
print('case 5-1 :', val_1 + val_4)
print('case 5-2 :', val_1 + val_2)

# case 6
# int 형 변수들을 float 형으로 변환하여 계산하는 경우 float 형으로 출력됨
# 연산 결과값은 변함이 없음(type만 변경)
print('case 6 :', float(val_1) + float(val_2))

# case 7
# bool 형의 True, False 에 대해 특징은 다음과 같다
# True 는 1 과 같다
# 서로 타입은 다르나 동일한 값을 가진다
# bool 형의 + 연산을 수행하는 경우 값은 int 형이 된다.
true_val = True
false_val = False
print('case 7 :', true_val, false_val, true_val + false_val,
      true_val + true_val, false_val + false_val, false_val + true_val)
