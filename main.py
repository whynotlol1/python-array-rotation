#program that rotates a 2d array 90 degrees clockwise

def rotate_array(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            array[i][j], array[j][i] = array[j][i], array[i][j]
    for i in range(len(array)):
        array[i].reverse()
    return array

array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

new_array = rotate_array(array)

for el in new_array:
    print(el)
