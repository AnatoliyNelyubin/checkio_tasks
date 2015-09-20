def checkio(data):
    new_data = []
    for col in range(len(data[0])):
        new_data.append([data[x][col] for x in range(len(data))])
    return new_data


# print(checkio([[1, 2, 3],
#                      [4, 5, 6],
#                      [7, 8, 9],
#                      [10, 11, 12]]))


if __name__ == '__main__':
    assert isinstance(checkio([[0]]).pop(), list) is True, "Match types"
    assert checkio([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]) == [[1, 4, 7],
                                    [2, 5, 8],
                                    [3, 6, 9]], "Square matrix"
    assert checkio([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                    [4, 2, 8, 9, 8],
                                    [3, 6, 3, 6, 1]], "Rectangle matrix"
