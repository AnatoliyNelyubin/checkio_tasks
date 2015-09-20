from math import pi, sqrt, atanh, asin, asinh


def checkio(height, width):
    volume = round((4 * pi / 3) * (width / 2) ** 2 * height / 2, 2)
    if height > width:  # prolate spheroid
        ecc = sqrt(1 - (width/2) ** 2 / (height/2) ** 2)
        surface_area = round(2 * pi * (width/2) ** 2
                             * (1 + (height/2) / (width/2 * ecc) * asin(ecc)), 2)
    elif height < width:  # oblate spheroid
        ecc = sqrt(1 - (height/2) ** 2 / (width/2) ** 2)
        surface_area = round(2 * pi * (width/2) ** 2
                             * (1 + (1 - ecc ** 2)/ecc * atanh(ecc)), 2)
    else:
        volume = round(4/3 * pi * (height/2) ** 3, 2)
        surface_area = round(4 * pi * (height/2) ** 2, 2)
    return [volume, surface_area]

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"