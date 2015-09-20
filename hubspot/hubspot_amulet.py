def checkio(matrix):
    m = matrix
    for f in range(-9000, 9001, 5):
        for s in range(-9000, 9001, 5):
            for t in range(-9000, 9001, 5):
                if (315 - t - m[1][2] * s - m[0][2] * f == 0 and
                    225 - m[2][1] * t - s - m[0][1] * f == 0 and
                        0 - m[2][0] * t - m[1][0] * s - f == 0):
                            print(f,s,t)
                            f = f % 180 if f > 180 or f < -180 else f
                            s = s % 180 if s > 180 or s < -180 else s
                            t = t % 180 if t > 180 or t < -180 else t
                            return [f, s, t]

print(checkio(
                    [[1, 3, 5],
                     [3, 1, 5],
                     [2, 5, 1]]))

exit()

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    def check_it(func, matrix):
        result = func(matrix)
        if not all(-180 <= el <= 180 for el in result):
            print("The angles must be in range from -180 to 180 inclusively.")
            return False
        f, s, t = result
        temp = [0, 0, 0]
        temp[0] += f
        temp[1] += matrix[0][1] * f
        temp[2] += matrix[0][2] * f

        temp[0] += matrix[1][0] * s
        temp[1] += s
        temp[2] += matrix[1][2] * s

        temp[0] += matrix[2][0] * t
        temp[1] += matrix[2][1] * t
        temp[2] += t
        temp = [n % 360 for n in temp]
        if temp == [0, 225, 315]:
            return True
        else:
            print("This is the wrong final position {0}.".format(temp))
            return False

    assert check_it(checkio,
                    [[1, 2, 3],
                     [3, 1, 2],
                     [2, 3, 1]]), "1st example"
    assert check_it(checkio,
                    [[1, 4, 2],
                     [2, 1, 2],
                     [2, 2, 1]]), "2nd example"
    assert check_it(checkio,
                    [[1, 2, 5],
                     [2, 1, 1],
                     [2, 5, 1]]), "3rd example"