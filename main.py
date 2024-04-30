car = ["BMW", "MB", "LADA", "KIA", "HONDA"]
for i in car:
    print('Я езжу на автомабиле марки', i)

car = ["BMW", "MB", "LADA", "KIA", "HONDA"]
for i in car:
    print(i)
    cars_count = 0
    for j in range(len(car)):
        cars_count += 10
        print(cars_count)
