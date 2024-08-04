class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name
class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
     def eat(self, food):
        self.food = Plant
        if food is Fruit(Plant):
            print(self.name, 'съел', food.name)
            fed = True
        else:
            print(self.name, 'не стал есть', food.name)
            alive = False

class Predator(Animal):
     def eat(self, food):
        self.food = Plant
        if food is Plant:
            print(self.name, 'не стал есть', food.name)
            alive = False
class Flower(Plant):
    edible = False
    pass

class Fruit(Plant):
    edible = True
    pass


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)