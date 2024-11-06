class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    """ 수행평가 """
    def eat(self, food):
        print(f"{self.name}이(가) {food}를 먹습니다")
    """ -------- """
    def __str__(self):
        return f"{self.name}은 {self.age}살 입니다"

class Employee(Person):
    def __init__(self, name, age, salary):
        """ 수행평가 """
        super().__init__(name, age)
        self.salary = salary
        """ -------- """
    def work(self):
        print("열심히 일합니다")
    """ 수행평가 """
    def get_s(self):
        print("급료를 받습니다.")
        return self.salary
    """ -------- """
    
e = Employee("우진", 18, 1000)
print(e)
e.eat("치킨")
e.work()
r = e.get_s()
print(f"급료는 {r}만원 입니다")