print("shape 1")
for i in range(3):
    for j in range(3):
        print("* ", end="")
    print()
# shape 2
print("shape 2")
count = 0
for a in range(3):
    for b in range(3):
        if count != 4:
            print("* ", end="")
        else:
            print("  ", end="")
        count += 1
    print()
# shape 3
print("shape 3")
count1 = 1
for y in range(3):
    for z in range(3):
        if count1 % 2 == 0:
            print("  ", end="")
        else:
            print("* ", end="")
        count1 += 1
    print()
