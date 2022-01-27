RANGE = list(map(lambda x: x / 10, range(-50, 50, 5)))

TRUTH_TABLE = [
    # x1 x2 wynik
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 0],
]

def activation(x):
    return x >= 0


for w11 in RANGE:
    for w12 in RANGE:
        for w10 in RANGE:
            for w21 in RANGE:
                for w22 in RANGE:
                    for w20 in RANGE:
                        good = True
                        for row in TRUTH_TABLE:
                            x1, x2, result = row
                            y = activation(w11 * x1 + w12*x2 + w10)
                            z = activation(3 * y + w21 * x1 + w22 * x2 + w20)
                            if result != z:
                                good = False
                                break
                        if good:
                            print('w11 ', w11)
                            print('w12 ', w12)
                            print('w10 ', w10)
                            print('w21 ', w21)
                            print('w22 ', w22)
                            print('w20 ', w20)
                            exit(0)
