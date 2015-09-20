def weak_point(matrix):
    min_row_index = None
    min_col_index = None
    min_row_value = None
    min_col_value = None
    for i in range(len(matrix[0])):
        row_summ = sum(matrix[i])
        if min_row_value == None or row_summ < min_row_value:
            min_row_value = row_summ
            min_row_index = i
        col_summ = sum([matrix[j][i] for j in range(len(matrix[0]))])
        if min_col_value == None or col_summ < min_col_value:
            min_col_value = col_summ
            min_col_index = i
    return min_row_index, min_col_index  # [0, 0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3], "Example"
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0], "Top left"
