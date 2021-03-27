class A:
    def __init__(self):
        print('init A')

    def feature1(self):
        print('working on feature 1')

    def feature2(self):
        print('working on feature 2')


class B:
    def __init__(self):
        print('init B')

    def feature3(self):
        print('working on feature 3')

    def feature4(self):
        print('working on feature 4')


class C(A, B):
    def __init__(self):
        print('init C')
        super().__init__()

    def feature5(self):
        print('working on feature 3')


c = C()
c.feature4()
