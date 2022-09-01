def check_input_int(input_text, error_text):
    input_value = input(input_text)
    while input_value.isnumeric() is False:
        input_value = input(error_text)
    return int(input_value)


# példa a futtatásra:
x = check_input_int("adjon meg egy egész számot ", "hiba, kérem egész számot adjon meg ")
print(x)
