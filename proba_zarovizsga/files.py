file = open("data.txt")
redline = file.readline()

file = open("data.txt")
redlines = file.readlines()

file = open("data.txt")
red = file.read()

file = open("data.txt")
rows = []
for row in file:
    rows.append(row.removesuffix("\n"))

print(redline)
print("-------------------------------------------------")
print(redlines)
print("-------------------------------------------------")
print(red)
print("-------------------------------------------------")
print(rows)
