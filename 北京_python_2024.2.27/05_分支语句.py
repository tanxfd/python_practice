
a = int(input())

#   双分支
if a > 0:
    print("|a|=" + str(a))
else:
    print("|a|=" + str(0-a))

#   单分支
result = a if a > 0 else -a
print("|a|=" + str(result))

#   abs()
print("|a|=" + str(abs(a)))
