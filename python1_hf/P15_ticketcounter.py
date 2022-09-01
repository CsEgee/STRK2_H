def ticket_counter(age, distance):
    if age < 6 or age > 65:
        price = 0
        return price
    elif age in range(5, 19):
        price = (((distance // 100) + 1) * 350 * 0.5)
        return int(price)
    else:
        price = (((distance // 100) + 1) * 350)
        return int(price)


age_in = int(input("Kérem adja meg az utas életkorát: "))
distance_in = int(input("Kérem adja meg az utazási távolságot (km): "))
price_in = ticket_counter(age_in, distance_in)
print("A vonatjegy ára: " + str(price_in) + " Ft")
