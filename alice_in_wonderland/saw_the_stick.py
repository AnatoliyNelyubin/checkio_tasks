def checkio(number):
    tri_number_list = [int(item*(item + 1)/2) for item in range(1,50)]
    for tri_number_index in range(len(tri_number_list)):
        my_list, counter = [], 0
        while sum(my_list) < number:
            my_list.append(tri_number_list[tri_number_index + counter])
            counter += 1
        if sum(my_list) == number:
            return my_list
    return []

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
     assert checkio(64) == [15, 21, 28], "1st example"
     assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
     assert checkio(225) == [105, 120], "1st example"
     assert checkio(882) == [], "1st example"
