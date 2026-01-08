'''
project/
 ├─ school/     => 패키지
 │    ├─ __init__.py
 │    ├─ person.py      ==> 부모 클래스 Person클래스 [x]
 │    ├─ student.py     ==> Student
 │    └─ teacher.py     ==> Teacher
 │
 └─ main_app.py# school 패키지 사용하여 CRUD 실행
 http://bit.ly/data-pynote

 ### Student 클래스 (자식)
 - 속성 : student_id, name, cname(학급명)
 - 메서드 :
 'input_info()' : input()이용해서 학번/이름/학급명을 입력받는 함수
 'show_info()' : 학생정보를 문자열로 반환하는 메소드

  ### Teacher 클래스 (자식)
 - 속성 : t_id, name, subject(담당과목)
 - 메서드 :
 'input_info()' : input()이용해서 교번/이름/과목을 입력받는 함수
 'show_info()' : 교사정보를 문자열로 반환하는 메소드

 ### main_app.py에서
 메뉴구성
 1. 등록 ===> 서브 메뉴를 보여준다
    ------등록---------
    1. 학생  2. 교사
    ------------------
    1번 선택하면 학생정보 입력받기(학번/이름/학급)
    2번 선택 => 교사정보 입력받기 (교번/이름/과목)
    => 입력받은 값을 각 객체(Student/Teacher 객체)에 저장한 후 객체에 list에 저장
 2. 출력
    => 모든 학생과 교사 정보를 출력
'''

from project.school.student import Student, Tops
from project.school.teacher import Teacher, Topt
s1 = Student()
s2 = Tops()
t1 = Teacher()
t2 = Topt()
slst = []
tlst = []
while True:
    print(f"""  
    ------등록---------
    1. 학생  2. 교사
    ------------------
    """)
    menu = input(int('번호를 선택하세요'))
    if menu == 1:
        print(s2.input_info())
        slst.append(s2.input_info())
        print(s2.show_info())
        break
    elif menu == 2:
        print(t2.input_info())
        tlst.append(t2.input_info())
        print(t2.show_info())
        break

