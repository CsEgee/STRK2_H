"""
def between(a, b):
    pass # write your code here

print(between(5, 10))
# >>> kimenet: [5,6,7,8,9,10]

print(between(1,2))
# >>> kimenet: [1,2]
"""

# Függvény kidolgozása
def between(a, b):
    list = []
    for i in range(a, (b + 1)):
        list.append(i)
    return list


# Kimenetek
print(between(5, 10))

print(between(1, 2))


# Opcionális rész
number1 = int(input("Adj meg egy pozitív egész számot!\n"))
number2 = int(input("Adj meg egy nagyobb pozitív egész számot!\n"))
print(between(number1, number2))
