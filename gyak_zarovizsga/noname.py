def get_sum(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n / 10)
    return sum


n = 12345
print(get_sum(n))
