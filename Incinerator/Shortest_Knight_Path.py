def list_of_moves(square):
    start_col, start_row, result_list = square[0], square[1], []
    for (col_offset, row_offset) in zip([-1, -1, -2, -2, 1, 2, 1, 2], [-2, 2, -1, 1, -2, -1, 2, 1]):
        target_col = chr(ord(start_col) + col_offset)
        target_row = chr(ord(start_row) + row_offset)
        if target_col in 'abcdfegh' and target_row in '12345678':
            result_list.append(target_col + target_row)
    return result_list

def checkio(cells):
    number_of_moves = 1
    start_square, end_square = cells.split('-')
    visited_squares = [start_square]
    possible_moves = list_of_moves(start_square)
    queue = [(key, number_of_moves) for key in possible_moves if key not in visited_squares]
    visited_squares.extend(possible_moves)
    while queue:
        if end_square in possible_moves:
            break
        start_square, number_of_moves = queue.pop(0)
        possible_moves = list_of_moves(start_square)
        number_of_moves += 1
        for item in possible_moves:
            if item not in visited_squares:
                visited_squares.append(item)
                queue.append((item, number_of_moves))
    return number_of_moves

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("b1-d5") == 2, "1st example"
    assert checkio("a6-b8") == 1, "2nd example"
    assert checkio("h1-g2") == 4, "3rd example"
    assert checkio("h8-d7") == 3, "4th example"
    assert checkio("a1-h8") == 6, "5th example"