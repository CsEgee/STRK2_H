
def traffipax(limit, actual, percentage):
    if (actual > limit + limit * percentage / 100):
        return True
    else:
        return False

