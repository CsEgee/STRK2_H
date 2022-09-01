with open("adat.txt", "r") as f:
    text_list = f.readlines()
    clean_text = []
    for i in text_list:
        clean_text.append(i.strip())
f.close()

print(' '.join(clean_text))
