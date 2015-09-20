def checkio(pattern, image):
    p_w = len(pattern[0])
    p_h= len(pattern)
    i_w = len(image[0])
    i_h = len(image)
    for row in range(i_h - p_h + 1):
        for col in range(i_w - p_w + 1):
            counter = 0
            for i in range(p_h):
                for j in range(p_w):
                    if image[row + i][col + j] == pattern[i][j]:
                        counter += 1
            if counter == (p_w * p_h) and image[row][col] < 2:
                for i in range(p_h):
                    for j in range(p_w):
                        image[row + i][col + j] += 2
    return image

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 0], [1, 1]],
                   [[0, 1, 0, 1, 0],
                    [0, 1, 1, 0, 0],
                    [1, 0, 1, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                          [0, 3, 3, 0, 0],
                                          [3, 2, 1, 3, 2],
                                          [3, 3, 0, 3, 3],
                                          [0, 1, 1, 0, 0]]
    assert checkio([[1, 1], [1, 1]],
                   [[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]]) == [[3, 3, 1],
                                    [3, 3, 1],
                                    [1, 1, 1]]
    assert checkio([[0, 1, 0], [1, 1, 1]],
                   [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
                                                         [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                         [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                                                         [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
                                                         [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                                                         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                                         [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
                                                         [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
                                                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
