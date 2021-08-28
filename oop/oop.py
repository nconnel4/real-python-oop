class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}'.format(self.name, sound)

    def birthday(self):
        self.age += 1


mikey = Dog('Mikey', 4)
print(mikey.description())

print(mikey.speak('Gruff gruff!'))

mikey.birthday()
print(mikey.description())