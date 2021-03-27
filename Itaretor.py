class TopTen:
    def __init__(self):
        self.numb = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.numb <= 10:
            val = self.numb
            self.numb += 1
            return val
        else:
            raise StopIteration

values = TopTen()
for i in values:
    print(i)
