
#   11题在word上没看到，12题几乎和第9题一样

def input_string():
    while 1:
        string = input()
        print(string)
        for i in list(string):
            if i == ' ':
                return 0

input_string()


