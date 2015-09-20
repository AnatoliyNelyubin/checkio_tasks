def decode_amsco(message, key):
    matrix_width = len(str(key))
    matrix = []
    row = 0
    copy_message = message
    # Here I am emulating final matrix in order to know the number of symbols which have to be inserted into
    # every ceil
    while copy_message:
        col = 0
        matrix_row = []
        while col < matrix_width and copy_message:
            cut_index = 1 if (col + row) % 2 == 0 else 2
            matrix_row.append(copy_message[:cut_index])
            copy_message = copy_message[cut_index:]
            col += 1
        matrix.append(matrix_row)
        row += 1
    # Here I am actually inserting all the symbols into prepared matrix
    for key_index in range(1, len(str(key)) + 1):
        row = 0
        col_index = str(key).index(str(key_index))
        while True:
            try:
                cut_index = len(matrix[row][col_index])
            except IndexError:
                break
            else:
                matrix[row][col_index] = message[:cut_index]
                message = message[cut_index:]
                row += 1
    message = ''
    for row in matrix:
        message += ''.join(row)
    return message

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"