
def multy(*args):
    count = 1
    for i in args:
        count *= i
    return count


print(multy(1, 2, 3))
