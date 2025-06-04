
l = [25, 23, 26, 23, 33, 25, 24, 22]


for i in l:
    for j in l:
        if j >= i:
            break
        else:
            for k in l:
                if k > i:
                    print(k)

