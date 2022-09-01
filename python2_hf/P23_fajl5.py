with open("adat.txt", "r") as f:
    with open("adat4.txt", "w") as f2:
        f2.write(str(f.read()))
f.close()
f2.close()