
def cons_single(cons_hw, cons_ct, dist_hw, dist_ct):
    cons_single = (cons_hw * (dist_hw / 100) + cons_ct * (dist_ct / 100))
    return cons_single


def cons_return(cons_hw, cons_ct, dist_hw, dist_ct):
    cons_return = 2 * (cons_hw * (dist_hw / 100) + cons_ct * (dist_ct / 100))
    return cons_return


def cost_return(cons_hw, cons_ct, dist_hw, dist_ct, petrol_pr):
    cost_return = petrol_pr * (2 * (cons_hw * (dist_hw / 100) + cons_ct * (dist_ct / 100)))
    return cost_return


cons_hw = int(input("Add meg az országúti fogyasztást (l / 100 km): "))
cons_ct = int(input("Add meg a városi fogyasztást (l / 100 km): "))
dist_hw = int(input("Add meg az odaút országúton megtett távolságát (km): "))
dist_ct = int(input("Add meg az odaút városban megtett távolságát (km): "))
petrol_pr = int(input("Add meg az üzemanyag árát (Ft / l): "))

print("Az odaúton fogyasztott üzemanyag: " + str(cons_single(cons_hw, cons_ct, dist_hw, dist_ct)) + " l")
print("Az oda-vissza úton fogyasztott üzemanyag: " + str(cons_return(cons_hw, cons_ct, dist_hw, dist_ct)) + " l")
print("A teljes út költsége: " + str(cost_return(cons_hw, cons_ct, dist_hw, dist_ct, petrol_pr)) + " Ft")
