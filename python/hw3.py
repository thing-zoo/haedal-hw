#객체지향 프로그래밍 코드를 짜보자
#인스턴스 변수를 추가했을 때의 결과가 출력되도록

class Dormitory:
    total = 0
    girl = 0
    boy = 0
    
    def __init__(self, girl, boy):
        self.total = girl + boy
        self.girl = girl
        self.boy = boy
    
    def info(self):
        print(f'전체 학생 수: {self.total}')
        print(f'여학생 수: {self.girl}')
        print(f'남학생 수: {self.boy}\n')
        
    def come(self, girl, boy):
        self.girl += girl
        self.boy += boy
        self.total += (girl + boy)

    def out(self, girl, boy):
        self.girl -= girl
        self.boy -= boy
        self.total -= (girl + boy)

dom = Dormitory(60, 60)

dom.info()  #120 60 60

dom.come(3, 5)
dom.info()  #128 63 65

dom.out(6, 7)
dom.info() #115 57 58