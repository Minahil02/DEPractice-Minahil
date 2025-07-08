def even():
    for num in range(2, 21, 2):
        yield num
for even in even():
    print(even)
