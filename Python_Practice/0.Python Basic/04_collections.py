# 자료형에 대한 학습을 진행합니다
# List, Tuple, Dictionary, Set 의 형태가 있습니다.

# List
# List 자료형의 특징은 다음과 같습니다.
# List_collection = [a, 1, 'a']
# 다양한 타입의 데이터를 넣을 수 있습니다.
# 데이터의 변경이 가능합니다.
list_collection = [1, 2, 3.0, [1, 2, 3.0], 'a', 'b', 'c']
print('collection type : ', type(list_collection))
print('collection data : ', list_collection)

# List 에 데이터를 추가하는 경우 List.append() 를 사용합니다.
# 이 경우 추가되는 데이터는 List 의 가장 마지막 인덱스 다음에 저장됩니다.
# list_collection : [1, 2, 3.0, [1, 2, 3.0], 'a', 'b', 'c', '3']
list_collection.append('3')
print("'3'이 추가된 list_collection : ", list_collection)

# List 는 데이터를 자를 수 있습니다. 이 경우, 원래의 데이터는 변경되지 않습니다.
# 자르는 방법은 list_collection[a:b] 의 형태로 표현하며, index 번호가 a 이상 b 미만인 데이터를 가져옵니다.
# index 번호 2, 3 번의 데이터를 잘라서 가져옵니다.
print("list_collection[2:4] : ", list_collection[2:4])
print("list_collection[3][0:2] : ", list_collection[3][0:2])

# List 의 데이터를 수정할 수 있습니다.
list_collection[0] = 100
print('list_collection[0] = 100 으로 변경된 list_collection : ', list_collection)

# Tuple
# Tuple 자료형의 특징은 다음과 같습니다
# Tuple_collction = (1, 2, 3.0, (1, 2, 3.0), 'a', 'b', 'c')
# 다양한 타입의 데이터를 넣을 수 있습니다.
# 데이터의 변경이 불가능합니다
tuple_collection = (1, 2, 3.0, (1, 2, 3.0), 'a', 'b', 'c')
print('collection type : ', type(tuple_collection))
print('collection data : ', tuple_collection)

# Tuple 의 데이터는 자를 수 있습니다.
print('tuple_collection[2:4] : ', tuple_collection[2:4])

# Tuple 의 데이터는 변경이 불가능합니다.
# Tuple 에는 데이터를 추가하는 함수가 존재하지 않습니다.
# Tuple 은 데이터 변경 선언이 불가능합니다.
try:
    tuple_collection.append('3')
    print("'3'이 추가된 tuple_collection : ", tuple_collection)
except Exception as e:
    print('Tuple.append()가 실패한 이유 : ', e)

tuple
try:
    tuple_collection[0] = 100
    print(
        'tuple_collection[0] = 100 으로 변경된 tuple_collection : ', tuple_collection)
except Exception as e:
    print('Tuple[a] = b 가 실패한 이유 : ', e)

# Dictionary
# Dictionary 자료형의 특징은 다음과 같습니다
# Dictionary_collection = {key1 : value1 , key2 : value2 , ...}
# key 값을 이용하여 value 값을 찾을 수 있습니다
dictionary_collection = {'a': '1', 'b': 2, 'c': {'a': 1, 'b': '2', 3: 'C'}}
print('collection type : ', type(dictionary_collection))
print('collection data : ', dictionary_collection)

# Dictionary 는 key 값을 이용하여 value를 불러올 수 있습니다.
# Dictionary_collection[key] -> value
# return 값이 str 인지 int 인지는 실제 type을 확인하지 않으면 알기 어렵다
print("dictionary_collection['a'] : ", dictionary_collection['a'])
print("dictionary_collection['c'][3] : ", dictionary_collection['c'][3])

# Dictionary 에 새로운 키 값을 이용하여 데이터를 추가할 수 있습니다.
# Dictionary_collection[New Key] = New Value
dictionary_collection['d'] = list_collection
dictionary_collection['d'].append(tuple_collection)
print('새로운 데이터가 추가된 dictionary_collection : ', dictionary_collection)

# Dictionary 는 키 값의 중복이 허용되지 않습니다.
# 같은 키 값을 입력하는 경우 가장 마지막에 지정한 입력한 값으로 데이터가 추가됩니다.
test_dic_collection = {'1': 1, '1': 2}
print('test_dic_collection : ', test_dic_collection)

# Set
# Set 자료형의 특징은 다음과 같습니다.
# Set_collection = set([1, 2, 3, 4, 5, ...])
# Set 자료형은 중복이 허용되지 않습니다.
# Set 자료형의 데이터로 List, Tuple, Dictionary, Set 등의 자료형은 사용할 수 없습니다.
# Set 자료형의 데이터는 순서가 없습니다.
set_collection = set([1, 2, 3.0, 'a', 'b', 'c', "HELLO"])
print('collection type : ', type(set_collection))
print('collection data : ', set_collection)

# Set 자료형은 중복을 허용하지 않습니다.
set_collection = set([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 3, 4, 5, 6])
print(
    'set_collection = set([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 3, 4, 5, 6]) : ', set_collection)

# Set 자료형은 데이터의 순서가 없습니다.
set_collection = set("This is why I'm not good at English.")
print('set_collection = set("This is why I\'m not good at English.") : ', set_collection)
