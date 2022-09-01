
# A txt fájl beolvasása egy az egyben, majd a sortörések eltávolítása és space-k mentén a string vágása
with open("petofi.txt", "r", encoding="utf-8" ) as vers_beolvas:
    egybe_szoveg = vers_beolvas.read()
    print(egybe_szoveg)
    print(type(egybe_szoveg))
    szo_lista = egybe_szoveg.replace("\n", " ").split(" ")
    print(szo_lista)
    print(szo_lista[1::2])

# A csak string-et tartalmazó listából a megfelelő elemek kiíratása fájlba
with open("results.csv", "w", encoding="utf-8") as vers_kiiras:
    for w in szo_lista[1::2]:
        vers_kiiras.write(f"{szo_lista.index(w)+1}, {w}\n")




