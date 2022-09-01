with open("adat.txt", "r") as f:
    text_list = f.readlines()
    clean_text = []
    for i in text_list:
        clean_text.append(i.strip())
f.close()

with open("adat3.txt", "w") as f2:
    f2.write("\n".join(clean_text))
f2.close()
