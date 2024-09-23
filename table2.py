from math import factorial


x = 0
h = 0.02
d = 0.001
a = 0
b = 0.2


while a <= x <= b:
    element = abs(x**2 - 1)
    y = 0
    n = 1

    while element > d:
        y += (x**(2*n) - 1) / factorial(2*n - 1)
        element = abs((x**(2*(n + 1)) - 1) / factorial(2*(n + 1) - 1))
        n += 1

    print("x =", x, "y =", y)
    x += h
