"""  
os 모듈
- 파일과 디렉토리를 조직하고 경로를 설정하는 모듈
- getcwd() : 현재 작업 디렉토리의 위치를 반환
- chdir(path) : 현재 작업 디렉토리의 위치를 변경
- listdir(path) : 해당 경로에 있는 파일과 디렉토리 목록 반환
- remove(path) / mkdir(path) / makedirs(path) / rmdir(path) / removedirs(path)
- os.rename(src, dest) : src 원본파일명을 dest로 변경
"""
import os
print('현재 위치1: ', os.getcwd())
# 현재 위치1:  D:\dev_source\PyWork
# 경로 수정
os.chdir('c:/')
print('현재 위치2: ', os.getcwd())
# os.chdir('D:\\dev_source\\testPkg')   # \n, \t, \", \' \\
os.chdir(r'D:\dev_source\testPkg')  # raw
print('현재 위치3: ', os.getcwd())
# 현재 위치의 파일목록을 출력하세요
file_list = os.listdir()
print(type(file_list))
print(file_list)

#c:/의 목록도 출력해보세요
os.chdir('c:/')
flist = os.listdir()
for f in flist:
    print(f)
print('--------------------------------------')
import codecs
f = codecs.open(r'D:\dev_source\PyWork\ex46_quiz.py', 'r', encoding = 'utf8')
print(f.read())
f.close()

