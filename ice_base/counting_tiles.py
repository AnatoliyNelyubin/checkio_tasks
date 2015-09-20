def checkio(radius):
    """count tiles"""
    from math import sqrt
    if radius <= 1:
        return [0, 4]
    elif 1 < radius < sqrt(2):
        return [0, 12]
    elif radius == sqrt(2):
        return [4, 8]
    elif sqrt(2) < radius <= 2:
        return [4, 12]
    elif 2 < radius < sqrt(5):
        return [4, 20]
    elif radius == sqrt(5):
        return [12, 12]
    elif sqrt(5) < radius < sqrt(8):
        return [12, 20]
    elif radius == sqrt(8):
        return [16, 16]
    elif sqrt(8) < radius <= 3:
        return [16, 20]
    elif 3 < radius < sqrt(10):
        return [16, 28]
    elif radius == sqrt(10):
        return [24, 20]
    elif sqrt(10) < radius < sqrt(13):
        return [24, 28]
    elif radius == sqrt(13):
        return [32, 20]
    elif sqrt(13) < radius <= 4:
        return [32, 28]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
    print(checkio(1.1))
