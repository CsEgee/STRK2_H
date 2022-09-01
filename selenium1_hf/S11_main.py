from S11_calculator import calculator

atmero_in = int(input("Add meg a henger átmérőjét (cm): "))
magassag_in = int(input("Add meg a henger magasságát (cm): "))

palast_in = calculator(atmero_in, magassag_in)
print("A hengerpalást területe: " + str(round(palast_in, 2)) + " négyzetcentiméter")
