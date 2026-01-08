class MyDate:
    content = 'MyDate 클래스'  # 클래스 변수
    # 인스턴스 변수 year, month, day  생성자 초기화하세요
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    # display() 인스턴스 메서드 구성
    def display(self):
        print(f'{self.year}-{self.month}-{self.day}')
    # 매개변수 sep를 받아서
    # 2026-01-08
    # 2026/01/08 식의 문자열을 반환하는 매서드로 구성

md = MyDate(2026, '01', '08')
md.display()