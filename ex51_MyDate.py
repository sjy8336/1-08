class MyDate:
    content = 'MyDate 클래스'  # 클래스 변수
    # 인스턴스 변수 year, month, day  생성자 초기화하세요
    def __init__(self, yy, mm, dd):
        self.year = yy
        self.month = mm
        self.day = dd
    # display() 인스턴스 메서드 구성
    def display(self, sep='-'):
        return f'{self.year}{sep}{self.month}{sep}{self.day}'
    # 매개변수 sep를 받아서
    # 2026-01-08
    # 2026/01/08 식의 문자열을 반환하는 매서드로 구성
    """  
    - 인스턴스 메서드 : display()
    - 클래스 메서드
    - static 메서드
    """
    @classmethod  # 함수 장식자 @classmethod를 붙이면 클래스 메서드가 된다
    def date_string(cls, dateStr):  # 클래스 메소드에는 cls 를 인자로 포함한다
        print(cls)
        print(cls.content)
        # print(MyDate.content)와 동일함
        yy = dateStr[:4]
        mm = dateStr[4:6]
        dd = dateStr[6:]
        return f'{yy}년 {mm}월 {dd}일'
    
    @staticmethod   # 정적 메소드는 @staticmethod를 붙인다
    def print_info():
        print('MyDate 클래스 입니다')
        # 정적 메소드는 순수 함수처럼 인스턴스의 상태를 변화시키지 않는 기능을 만들 때 사용하면 "클래스명.메소드명()" 형식으로 접근한다

    # classmethod는 cls를 인자로 받고, staticmethod는 인자를 받지 않음

if __name__ == '__main__':
    m1 = MyDate(2026, 1, 8)
    m2 = MyDate(2025, 12, 31)

    # [1] 클래스 변수 content 출력
    print(MyDate.content)
    # [2] m1의 년도 정보만 출력하기
    print(m1.year, '년')
    # [3] 2025/12/31 출력하기
    sdata = m2.display('/')
    print(sdata)
    print(m1.display())

    # date_string()호출해서 출력하기
    x = MyDate.date_string('20260508')
    print(x)
    # 클래스 변수를 접근할 때 클래스 메서드를 사용

    # print_info() 호출해서 출력하기
    MyDate.print_info() # 권장
    m1.print_info() # 권장하지 않음