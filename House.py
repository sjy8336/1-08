# 집을 class로 설계해 구성해봅시다
# 클래스명: [명사형, 대문자로 시작. Camel 표기법]
# - 속성 -> 3개 추출 [명사형, 소문자, Camel, Snake 표기]
# - 행동 양식(기능) => 메서드 2개 [동사형, 소문자]
# - 생성자 구성
# - 클래스변수 : house_type = '아파트'

""" class HOUSE:
    house_type = '아파트'


def __init__(self, eat, sleep):
    self.eat = eat
    self.sleep = sleep

def info(self):
    print(f'''
    주거형태 : {HOUSE.house_type}
    ''') """

# 테스트
# 객체 2개 생성해서 메소드 호출하기
# 속성 has a 관계. House has a owner House has a engine [x]
class House:
    house_type = '단독주택'
    def __init__(self, owner = '아무개', room=1, addr=''):  # 생성자
        # print('--init호출됨---')
        self.owner = owner
        self.room = room
        self.addr = addr

    def show(self):
        print('---House 정보')
        print(f'소유주: {self.owner}')
        print(f'방  수: {self.room}')
        print(f'주  소: {self.addr}')

    def detail_addr(self, bunji):
        """집정보 보여주고 세부 주소까지 출력"""
        self.show()  # 집 정보 출력
        print(f'{bunji}번지에 위치한 집이에요')
        print('--------------------------------------')

    # def __del__(self):  # 소멸자
        # print('--del 호출됨---')

h1 = House('홍길동', 2, '서울 동작구')
h2 = House()  # 기본생성자 default contructor
"""  
TypeError: House.__init__() missing 3 required positional arguments: 'owner', 'room', and 'addr'
"""
h1.show()
h2.show()

# h1 서울 동작구 45번지
# h2에 주소 지정. 인천 서구 55번지
h1.detail_addr(45)
h2.addr = '인천 서구'
h2.detail_addr(55)