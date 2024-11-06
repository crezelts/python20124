class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def __str__(self):
        return f"Person 설명, 이름은 {self.name} 키는 {self.height}"
    def __len__(self):
        """ 수행평가 """
        return self.height

    def __getitem__(self, key):
        if key == "name":
            return self.name
        # 수행평가
        elif key == "age":
            return self.age
        else:
            return None
        # 여기까지
        

p = Person("이광민", 18, 168)
print(p)
print(len(p))
print(p["age"])
print(p["HH"])