with open("input.txt", "w") as file:
    file.write("alma")

with open("input.txt", "r") as file2:
    result = file2.read()

print(result)

with open("input.txt", "a") as file:
    file.write("XY")

with open("input.txt", "r") as file2:
    result = file2.read()

print(result)