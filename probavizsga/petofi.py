import csv

with open("petofi.txt", "r") as f:
    tartalom = f.read()
    tartalom_lista = tartalom.split()
    kettesevel_lista = tartalom_lista[1::2]
    print(kettesevel_lista)

with open("results.csv", "w") as f2:
    writer = csv.writer(f2)
    writer.writerow(kettesevel_lista)
