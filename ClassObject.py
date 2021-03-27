class Computer:
    processor = 3

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
        self.name = 'nayan'
        self.age = 32
        self.br = self.Brand()

    def config(self):
        return print('conf is', self.cpu, self.ram)

    def show(self):
        print(self.name)
        self.br.show()

    @classmethod
    def info(cls):
        return cls.processor

    @staticmethod
    def sm():
        return print('this is static method')

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

    class Brand:
        def __init__(self):
            self.brand = 'hp'

        def show(self):
            return print(self.brand)


com = Computer('i5', 12)
com.age = 33
com2 = Computer('i5', 13)
com.processor = 6
if com.compare(com2):
    print('they are same')

else:
    print('they are not same', com.processor, com2.processor, Computer.info())

com.show()
