# függvény definiálása
def special_eleven(number_in):
    if number_in % 11 == 0:
        return True
    else:
        return False


# függvény tesztelése a feladatban megadott számokkal
tesztszamok = [23, 24, 122, 96]
print("Tesztelés " + str(tesztszamok) + " számokkal")
for szamok in tesztszamok:
    print(special_eleven(szamok))
print("=" * 40)

# függvény tesztelése egy bekért számmal
print("Tesztelés bekért számmal")

number = int(input("Adjon megy egy számot: "))
if special_eleven(number) == True:
    print("A megadott szám osztható 11-gyel.")
else:
    print("A megadott szám nem oszthat 11-gyel.")
