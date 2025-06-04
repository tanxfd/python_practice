
def print_triangle(n):
    for i in range(0, n):
        for j in range(0, n - i - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print('*', end='')
        print('\n')

print_triangle(4)
