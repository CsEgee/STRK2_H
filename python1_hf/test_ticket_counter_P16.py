
def ticket_counter(base, age, distance):
    if age < 6 or age > 65:
        price = 0
        return price
    elif age in range(5, 19):
        price = (((distance // 100) + 1) * base * 0.5)
        return int(price)
    else:
        price = (((distance // 100) + 1) * base)
        return int(price)


def test_ticket_counter_regular():
    assert(ticket_counter(350, 40, 240) == 1050)


def test_ticket_counter_student():
    assert(ticket_counter(350, 12, 240) == 525)


def test_ticket_counter_retired():
    assert(ticket_counter(350, 70, 240) == 0)
