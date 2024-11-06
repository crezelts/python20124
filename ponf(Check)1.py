class Car:

    """ 수행평가 """

    def __init__(self, type, speed):
        self.t = type
        self.s = speed
    def move(self):
        return self.t + "가" + str(self.s) + "속도로 움직입니다" # print 넣으면 출력시 print() 반복 X

    """ 여기까지 """
    def speed_up(self, amount):
        self.s = self.s + amount
    def speed_down(self, amount):
        self.s = self.s - amount

goodCar = Car("람보르기니", 100)
print(goodCar.t, goodCar.s)
g = Car("페라리", 100)
print(g.move())

g.speed_up(10)
print(g.move())

""" speed_down 메소드도 사용하기 """
g.speed_down(10)

print(g.move())
