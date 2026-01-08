# os.path 모듈 : 파일 디렉토리의 경로를 설정하고 조작하게 하는 모듈
import os.path
print(os.getcwd())
print(os.path.abspath('story.txt'))
# 파일의 절대경로 반환
# D:\dev_source\PyWork\story.txt
# 디렉토리 유무 확인
# print(os.path.exists(r'D:\dev_source\PyWork'))    # True
print(os.path.exists(r'D:\dev_source\PyWork\yourpkg'))  # False
# 파일 여부 확인
print(os.path.isfile(r'D:\dev_source\PyWork\story.txt'))    # True
# 디렉토리 여부 확인
print(os.path.isdir(r'D:\dev_source\PyWork\story.txt')) # False
# 디렉토리와 파일 분리
print(os.path.split(r'D:\dev_source\PyWork\story.txt'))
# ('D:\\dev_source\\PyWork', 'story.txt')
tp = os.path.split(r'D:\dev_source\PyWork\story.txt')
print(tp[0])
print(tp[1])
# 디렉토리와 파일 결합
print(os.path.join('c:/', 'hello.py'))  
# 파일 크기 반환: getsize(파일명)
# story.txt의 파일 크기를 출력
print(os.path.getsize('story.txt'))   # 685