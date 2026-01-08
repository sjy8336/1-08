# - 캡슐화(Encapsulation)
# 클래스의 멤버변수들을 외부에서 함부로 변경 못하도록
# 은닉변수(private변수)로 만드는 것
# - 은닉할 변수에 _기호를 연속해서 2 개 넣으면 외부에서 접근 불가함
#   Account클래스를 캡슐화 해보자
# - 은닉변수를 외부에서 접근할 수 있는 공용 인터페이스는
#   getter와 setter 메서를 만들어서 사용하게 한다
# - setter는 외부에서 값을 수정하기 위한 메소드
# - getter는 외부에서 값을 꺼내기 위한 메소드

# TypeError: 'module' object is not callable. Did you mean: 'Account.Account(...)'?
import Account as ac
# import 모듈명
# 모듈명 : Account.py
# 클래스명 : Account
# print(ac.Account.money)    # 10

from Account import Account, TopAccount
# from 모듈명 import 클래스명
print(Account.money)
a = Account()
Account.money -= 7
print('현재 잔액:', Account.money)
# 현재 잔액: 3
print('*************************************')
# TopAccount 클래스는 캡슐화를 해보자
# TopAccount 객체 생성 후 showInfo() 호출하기
a1 = TopAccount('A001', '김부자', 500)
print(a1.showInfo())

# a1.__money -= 300  # ==> 캡슐화된 변수에는 접근 불가
print(a1.showInfo()) 
""" 
a1.__money -= 300
AttributeError: 'TopAccount' object has no attribute '__money'
"""

a1.setMoney(-300)
print(a1.getMoney())
print(a1.showInfo())
a1.setMoney(700)
print(a1.showInfo())
a1.setMoney(-1000)
print(a1.showInfo())
a1.setName('김거지')
print(a1.showInfo())

a1.__accNo = 'B002'
print(a1.showInfo())
print(a1.__accNo)