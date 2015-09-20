def recall_password(cipher_grille, ciphered_password):

    password = ''
    cipher_grille = [list(row) for row in cipher_grille]
    for iteration in range(4):
        temp_grille = [[], [], [], []]
        for row in range(4):
            for col in range(4):
                if cipher_grille[row][col] == 'X':
                    password += ciphered_password[row][col]
                temp_grille = zip(*cipher_grille[::-1])
        cipher_grille = tuple(temp_grille)
    return password

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'