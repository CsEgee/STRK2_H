def between(a, b):
    lista = []
    for i in range(a, b + 1):
        lista.append(i)
    return lista


a_in = int(input("Adja meg a lista kezdő számát: "))
b_in = int(input("Adja meg a lista befejező számát: "))

print(between(a_in, b_in))
