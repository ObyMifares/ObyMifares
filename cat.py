class Cat:
    name = ''
    color = ''
    weight = 0
    def meow(self, kol):
        m = 'meow meow im a cow\n' * kol
        print(m)
    def data(self):
        print(self.name, self.color, self.weight)

    def __init__(self, name):
        self.name = name


cat = Cat('nana')
cat.meow(5)