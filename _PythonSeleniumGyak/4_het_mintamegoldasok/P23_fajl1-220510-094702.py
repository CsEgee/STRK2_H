try:
    with open("adat.txt", "r") as adat_file:
        for line in adat_file:
            print(line.strip(), end = " ")
finally:
    adat_file.close()