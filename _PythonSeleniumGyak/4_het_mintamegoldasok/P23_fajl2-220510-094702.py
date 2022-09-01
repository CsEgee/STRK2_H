try:
    with open("adat.txt", "r") as adat_file:
        lines = adat_file.readlines()
        for line in lines:
            print(line.strip(), end = " ")
finally:
    adat_file.close()