import math


def checkio(a, b, c):
    if a >= b+c or b >= a+c or c >= a+b or a == 0 or b == 0 or c == 0:
        return [0, 0, 0]
    alpha = round(math.degrees(math.acos((b*b + c*c - a*a)/(2*b*c))))
    beta = round(math.degrees(math.acos((a*a + c*c - b*b)/(2*a*c))))
    gamma = 180 - alpha - beta
    return sorted([alpha, beta, gamma])

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(10, 20, 30) == [0, 0, 0], "0,0,0"