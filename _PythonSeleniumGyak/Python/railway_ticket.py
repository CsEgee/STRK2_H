def decision(student_card, family, weekend):
    if student_card:
        return 50

    discount = 0
    if family:
        discount += 25
    if weekend:
        discount += 10

    return discount


studen_card = input("Van diákigazolványa? I/N ")
if studen_card.upper() == "I":
    studen_card = True
else:
    studen_card = False

family = input("Családi kedvezményre jogosult? I/N ")
if family.upper() == "I":
    family = True
else:
    family = False

weekend = input("Hétvégén utazik? I/N ")
if weekend.upper() == "I":
    weekend = True
else:
    weekend = False

print("A kedvezmény mértéke: ", decision(studen_card, family, weekend), " %")

# print(decision(True, False, False))
# print(decision(False, False, False))
# print(decision(False, True, False))
# print(decision(False, False, True))
# print(decision(False, True, True))
