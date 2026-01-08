# [1] 100부터 600까지 100단위로 건너뛰기한
# 정수를 'numbers.txt' 파일에 줄 단위로 쓰세요
# 100
# 200
# 300
num = 100
for i in range(6):
    with open('numbers.txt', 'a') as f:
        f.write(str(num) + '\n')
    num += 100
print('문제 1 완료!')

# [2] 'numbers.txt' 파일을 읽어서 해당 파일에 
# 저장돼 있는 모든 숫자의 합계와 평균을 구해 출력하세요
with open('numbers.txt', 'r') as f:
    lst = int(f.readlines())
    print(lst, type(lst))
print('문제 2 완료!')

# [3] story.txt 파일을 읽어서 모두 대문자로 변환하여
# 콘솔에 출력하세요
with open('story.txt', 'r') as f:
    r = f.readlines()
    print(r.upper())
print('문제 3 완료!')

# [4] input('검색할 단어 입력>>')으로 입력받은 단어가
# story.txt 파일에 총 몇 번 등장하는지 계산하세요
""" search = input('검색할 단어 입력 >>')
with open('story.txt', 'r') as f:
    read = f.readlines() """