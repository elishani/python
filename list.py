
def square(x):
        return (x**2)
def cube(x):
        return (x**3)

squares = map(square, range(10))
print squares

funcs = [square, cube]
for r in range(5):
    value = map(lambda x: x(r), funcs)
    print value