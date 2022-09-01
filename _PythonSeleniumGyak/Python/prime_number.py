
def isprime(szam):
    for i in range(2, szam):
        if (szam % i) == 0:
            return False
    return True

while True:
    szam = int(input("Adj meg egy egész számot 2 felett "))
    if isprime(szam):
        print(str(szam) + " primszám!")
    else:
        print(str(szam) + " nem primszám!")
