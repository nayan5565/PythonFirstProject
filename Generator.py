def top_ten():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


valuse = top_ten()

for i in valuse:
    print(i)
