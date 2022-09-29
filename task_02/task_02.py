# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

def Truth():
    res = 0
    for n in range(0, 8):
        num = bin(n)
        num = num.replace('b', '0')
        X = int(num[-3])
        Y = int(num[-2])
        Z = int(num[-1])
        left = not(X or Y or Z)
        right = (not X) and (not Y) and (not Z)
        if left == right:
            res += 1
        print(X, Y, Z, left, right, left == right, res)
    print()
    if res == 8:
        return print(True)
    else:
        return print(False)


Truth()
