# 문자열 => string : str
s1 = "First string"
s2 = 'Second string'
print(s1 + s2)  # 문자열 결합
s3 = s1 + s2    # First stringSecond string
print(s1[0])    #F
# slicing 지원
# s1에서 First를 추출해보세요
print(s1[:5])
# s1에서 string 추출하기
print(s1[6:])
print(s1[-6:])
# 문자열은 immutable (불변성) - 원본 편집 불가
# s3[0] = 'f'
print(s3)
"""  
TypeError: 'str' object does not support item assignment
"""
s4 = 'i like python i Like React.js'
s5 = s4.upper()     # 대문자
print(s5)   # I LIKE PYTHON I LIKE REACT.JS
print(s4)   # i like python i Like React.js
print(s4.lower())   # 소문자  |  i like python i like react.js
print(s4.capitalize())  # 첫글자 대문자  |  I like python i like react.js
print(s4.title())   # 단어의 첫글자를 대문자  |  I Like Python I Like React.Js
print('--------------------------------------')
print(s4)   # i like python i Like React.js
print(s4.count('like'))  # 1
print(s4.lower().count('like'))  # 2
print(s4.upper().count('LIKE'))    # 2
print(s4.lower().count('i'))    # 4
print('--------------------------------------')
# find()
print(s4.lower().find('python'))    # 7 / 검색한 단어의 인덱스 번호 반환
print(s4.lower().find('java'))    # -1 / 검색한 단어가 없으면 -1을 반환
print(s4.lower().find('like'))   # 2
print(s4)
print(s4.lower().find('like', 5))   # 16 / 인덱스 5 이후부터 like를 찾아 해당 인덱스 반환

# stratswith(prefix) / endswith(suffix)
print(s4.startswith('i'))   # True
print(s4.endswith('python'))    # False
# strip() : 좌우 공백을 제거하여 새로운 문자열을 반환한다
# lstrip() : 왼쪽 공백 제거
# rstrip() : 오른쪽 공백 제거
s = '   I like Python:Java:React.js   '
print(len(s))   # 32자
s2 = s.strip()
print(s2)
print(len(s2))  # 27자
s3 = s.lstrip()
print(s3)
print(len(s3))  # 30자
s4 = s.rstrip()
print(len(s4))  # 30자

# split() : 공백으로 분리. 반환타입은 list
# split(구분자) : 구분자로 분리
print(s)
st = s.strip()
lst = st.split()
print(lst)
# ['I', 'like', 'Python:Java:React.js']

# st를 분리해서 아래와 같은 목록으로 나오도록 만들어보세요
# ['I', 'like', 'Python', 'Java', 'React.js']
lst2 = lst[-1].split(':')
print(lst2)
lst3 = lst[:2] + lst2
print(lst3)   # ['I', 'like', 'Python', 'Java', 'React.js']
'''
isdigit() : 숫자면 True, 숫자가 아니면 False
isalpha() : 알파벳 여부 체크
isalnum() : 알파벳 + 숫자
isspace() : 공백문자 여부
isupper() : 대문자 여부
islower() : 소문자 여부
istitle() : 문자열이 title형식인가?
'''
cnt = st.lower().count('s')
print(st.lower())
print(cnt)
i = st.index('Python')
print('i: ', i) # 7
try:
    i = st.index('javascript')
    print('i: ', i)  # 검색어가 없으면 에러 발생
except: 
    print('찾는 단어는 없어요')

i = st.find('javascript')   # 없으면 -1을 반환
print('i: ', i)
if i < 0:
    print('검색어가 없어요')
# 기준문자열.join(iterable) : list, tuple, set, dict의 경우는 key값만 가능
data = 'Once upon a time, there was a small village near the forest'
# Once@upon@a@time,@there@was@a@small@village@near@the@forest
list1 = data.split()
print(list1)
data2 = "@".join(list1)
print(data2)
print('--------------------------------------')
tdata = ('Python', 'is', 'fun')
print('-'.join(tdata))  # Python-is-fun
sdata = 'ABC'
print('.'.join(sdata))  # A.B.C
set1 = {'apple', 'banana', 'kiwi'}
print(' '.join(set1))   # apple kiwi banana

# dict는 key만 join가능
dict1 = {"name":"김철수", "age":"22"}
result = "#".join(dict1)
print(result)   # name#age

# ages = [22, 23, 24]   # 문자열이 아닌 목록은 에러 발생
ages = ['22', '33', '44']
print("세".join(ages))
# TypeError: sequence item 0: expected str instance, int found

# [1]
file = ['index.html', 'test.py', 'oper.js', 'student.java']
# 위 리스트에서 .을 기준으로 분리하여 분리된 결과를 리스트 형태로 모두 출력하세요
# ['index', 'html'] ['test', 'py'] ...

for f in file:
    lst = f.split('.')
    print(lst)

# [2] 위 리스트에서 확장자가 '.js'인 파일명만 찾아 출력하세요
for f in file:
    lst = f.split('.')
    if lst[1].lower() == 'js':
        print('.'.join(lst))