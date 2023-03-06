def function(x, a, b, c):
    return a*x**2 + b*x + c

a = 2
b = 2
c = 2
start = -6
stop = 4
step = 1

print("x\ty")
for x in range(start, stop+step, step):
    y = function(x, a, b, c)
    print(f"{x}\t{y}")
