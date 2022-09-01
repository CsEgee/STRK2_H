# számok megadása
numbers = [1, 2, 3, 4, 5]

# változók deklarálása
result = 1
keplet = []

# szorzás képlet
for i in numbers:
    result = result * i
    keplet.append(i * "*")

# eredmény kiírása
print(str(numbers) + " => " + str(keplet) + " = " + str(result))
print(result)

# képlet sajnos nem megy :/
