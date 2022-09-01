
osszeg = 0
count = 0
szam = int(input("Kérem adjon meg egy számot: "))
osszeg += szam
count += 1

while int(szam) < 20:
    szam = int(input("Kérem adjon meg egy számot: "))
    osszeg += szam
    count += 1
else:
    print(osszeg)
    print("{:.2f}".format(float(osszeg / count)))
