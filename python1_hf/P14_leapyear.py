
def leapyear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


year_in = int(input("Adjon meg egy évszámot: "))

if leapyear(year_in) is True:
    print("A megadott évszám: " + str(year_in) + " >>> SZÖKŐÉV")
else:
    print("A megadott évszám: " + str(year_in) + " >>> NEM SZÖKŐÉV")
