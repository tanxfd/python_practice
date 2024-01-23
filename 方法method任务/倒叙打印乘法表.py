
def _multiply():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(repr(i), "*", repr(j), "=", repr(i * j).ljust(2), end=' ')
        print('\n')


print(_multiply())

