
def substract_abs_val(x, y):
    z = x - y
    return abs(z)


a = int(input("Add meg a kissebítendő számot: "))
b = int(input("Add meg a kivonandó számot: "))

print("A különbség abszolút értéke: " + str(substract_abs_val(a, b)))
