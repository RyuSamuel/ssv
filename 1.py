class FourCal: # 클래스(class)란 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면이고, 객체(object)란 클래스로 만든 피조물을 뜻한다.
               #클래스로 만든 객체에는 중요한 특징이 있다. 바로 객체마다 고유한 성격을 가진다는 것이다.
               # 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다.

    def __init__(self, first, second): #__init__는 생성자(Constructor)으로, 객체에 초깃값을 설정해야 할 필요가 있을 때는
                                       # setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법이다. 이 때 이름은 반드시 __init__이여만 한다.
                                       # 생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다. 초기화 (initialize) 메소드라고 부르기도 한다.
                                       # 함수를 선언 할 때는 첫번째 인자는 항상 self가 되어야하고 이건 무조건 해야한다. 룰이다.
                                       # 그리고 함수를 하용할 때는 self를 빼도 되는데 이는 self가 무조건 주어지기때문에 생략해도 되는 것이다.
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mult(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal): #위의 FourCal를 상속함. 클래스를 상속하는 이유는 기존 클래스를 바꾸지 않고 기능을 추가하기 위함. 기존 클래스가 라이브러리 형태면 상속을 사용해서 추가하는 수 밖에 없음

    def pow(self):
        result = self.first ** self.second
        return result

class safeFourCal(MoreFourCal): #오버라이딩 = 덮어쓰기. 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(Overriding, 덮어쓰기)이라고 한다. safeFourCal은 MoreFourCal로부터 상속되었고,
                                #MoreFourCal은 FourCal로 부터 상속이 되었다.
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second



a = safeFourCal(4,0) #가장 아래의 상속 클래스를 사용해야 모든 클래스를 쓸 수가 있음. a는 safeFourClass 클래스로 만든 객체이다.

b = safeFourCal(8,2.3)


print(a.add())
print(a.sub())
print(b.mult())
print(a.div())
print(a.pow())