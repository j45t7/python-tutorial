class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        return f'{self.name} is talking'


person1 = Person('John')

print(person1.talk())
