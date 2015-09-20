def simple_areas(*args):
    if len(args) == 1:
        return round(3.14 * (list(args)[0] / 2) ** 2, 2)
    elif len(args) == 2:
        return round(list(args)[0] * list(args)[1], 2)
    elif len(args) == 3:
        side_a, side_b, side_c = list(args)[0], list(args)[1], list(args)[2]
        hlf_p = (side_a + side_b + side_c) / 2
        square = (hlf_p * (hlf_p - side_a) * (hlf_p - side_b) * (hlf_p - side_c)) ** 0.5
        square = (hlf_p * (hlf_p - side_a) * (hlf_p - side_b) * (hlf_p - side_c)) ** 0.5
        return round(square, 2)
    else:
        return 0


if __name__ == '__main__':
#These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
