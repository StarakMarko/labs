from math import log, cos


x = 3
h = 0.2
a = 3
b = 8


while a <= x <= b:
    if x < 5:
        if log(abs(log(x, 3)), 4) == 0:
            print("x =", x, "y =", "error")
        else:
            y = log(abs(log(abs(log(x, 3)), 4)), 5)
            print("x =", x, "y =", y)
    elif 5 <= x < 7:
        y = 1 / (x**2 + 16)
        print("x =", x, "y =", y)
    elif x >= 7:
        y = log(x) + cos(x)
        print("x =", x, "y =", y)
    x += h
