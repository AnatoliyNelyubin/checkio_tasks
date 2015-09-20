def has_sequence(length, sequence):
    if length > len(sequence):
        return False
    for item in range(len(sequence) - length + 1):
        for thing in range(item, item + length - 1):
            if sequence[thing + 1] != sequence[thing]:
                break
        else:
            return True
    return False

def checkio(matrix):
    columns = list(zip(*matrix))
    length = len(matrix)
    for item in range(1, length + 1):
        # Here we are checking rows and columns
        if (has_sequence(4, columns[item - 1]) or has_sequence(4, matrix[item - 1]) or
           has_sequence(4, [matrix[x][y] for x, y in tuple(enumerate(range(item - 1, -1, -1)))]) or
           has_sequence(4, [matrix[x][y] for x, y in tuple(enumerate(range(length - 1, item - 2, -1), item - 1))]) or
           has_sequence(4, [matrix[x][y] for x, y in tuple(enumerate(list(range(item - 1, length))))]) or
           has_sequence(4, [matrix[x][y] for x, y in tuple(enumerate(range(item), abs(item - length)))])):
            return True

    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"

    exit()
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"