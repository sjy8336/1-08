'''
# 프로그래밍 방식
1) 절차지향 프로그래밍(Procedural)
- 순서대로 실행되는 절차(로직) 중심
- 함수 호출 중심 구조
- 작은 스크립트, 간단한 데이터 처리에 적합

예시
    def add(a, b):
        return a + b

    x = 10
    y = 20
print(add(x, y))

2) 객체지향 프로그래밍(OOP, Object-Oriented)

- 데이터와 기능을 객체로 묶어서 구성
- 클래스, 객체, 상속, 캡슐화 등 OOP 기능을 모두 지원
- 대형 프로젝트, 구조화된 설계에 적합
    예시
    class Calculator:
        data = 10
        def add(self, a, b):
            return a + b

    c = Calculator() # 객체
    print(c.add(10, 20)) # 객체명.메소드()

==========================
객체지향 프로그래밍
- 현실세계에 존재하는 객체를 프로그래밍 세계로 끌어들인 것
- 객체 = 속성 + 행동양식  
    속성==> 멤버변수로
    행동양식(기능)=> 메서드로 구현
---syntax------------------
class 클래스명:
    멤버변수
    def __init__(self):
        ...
    def 메서드명(self):
        ...
-----------------------------
# 클래스의 구성요소 = 멤버(Member) + 생성자(Constructor)
                        +----<1> 멤버변수(자료)
                        +----<2> 메서드 (기능)
클래스             객체
--------------------------------
설계도             구현물: 설계도에 의해 지어진 집
붕어빵틀                   붕어빵
--------------------------------------
Object ===============> object, instance
'''
# 인사관리 프로그램 (사원 / 부서 / 급여 / 매출 / 회사 ...)
# 학사관리 프로그램 (사원 / 학생 / 교사 / 커리큘럼)
# 부동산 관련 프로그램 (집 / 땅 / 중개인/ ....)
# 사원 (속성 + 행동양식)
# 속성 ==> 멤버변수 (varialbe, property, field) 사번, 이름, 부서, 연봉
# 행동양식 ====> method
# 멤버변수 (1. 클래스 변수 2. 인스턴스 변수)
class Emp:
    company_name = "SM Universe"    # 속성 => 멤버변수(클래스변수)
    # 속성 => 멤버변수(클래스변수)=> 객체마다 공유하는 변수 "클래스명.변수"
    # 멤버변수(인스턴스 변수) => 객체마다 다른 값을 갖는다 "객체명.변수"

    def __init__(self, no, name, dept):   # 생성자 함수 (인스턴스 변수 초기값을 부여)
        self.no = no    # self.no ==> 인스턴스 변수 (객체가 메모리 올라갈 때 같이 올라감)
        self.name = name    # no, name, dept ==> 지역변수(인자/매개변수)
        self.dept = dept

    # 메소드나 생산자에는 기본적으로 self라는 인수를 갖는다. self를 생략하면 에럭 발생
    # self는 인스턴스 변수나 인스턴스 메소드를 참조하는 역할한다
    def info(self):
        print(f'''
        ----사원정보--------------
        회사명 : {Emp.company_name}
        사  번 : {self.no}
        사원명 : {self.name}
        부  서 : {self.dept}
        ''')
# --------------------------------------------------------------------------------------------
# 클래스 구성 => 설계도, 붕어빵 등
# 객체로 메모리에 올리면 => 집, 붕어빵

# 객체를 생성
# 변수명 = 클래스명() ==> 객체
# 를 생성. 생성자가 호출된다
e1 = Emp(100, "이효림", "기획부")
e2 = Emp(101, '김철수', "총무부")

print(e1)   # <__main__.Emp object at 0x000001FEE86F8590>
print(e2)   # <__main__.Emp object at 0x000001FEE86F0550>

print(e1.name, e1.dept)  # 객체명.변수  이효림
print(e2.name, e2.dept)  # 김철수
# info() 호출해보기
e1.info()
e2.info()
# 회사명 출력
print(e1.company_name)   # 에러는 나지 않지만 클래스명으로 접근하자
print(Emp.company_name)   # 클래스 변수이므로 클래스명. 변수로 접근해야 함

# e1 -> 부서변경 -> 노무부
e1.dept = '노무부'
# info() 호출하기
e1.info()

# e2 => 김명철 변경 info() 호출하기
e2.name = '김명철'
e2.info()
# 회사명 변경 YG로 변경
e1.company_name = 'YG Universe' # 클래스변수가 아니라 e1의 instance변수로 취급
print(e1.company_name, e2.company_name)  # YG Universe SM Universe
Emp.company_name = "VICTORY UNIVERSE"
print('---회사명 변경------------')
# e1.info() e2.inf0()호출하기
e1.info()
e2.info()
# 클래스변수는 객체들간에 공유하는 데이터
# 인스턴스변수는 객체들마다 가지고 있는 변수