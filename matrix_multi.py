# matri1 =
# 4 4
# 1 2 2 7
# 3 3 4 5
# 5 0 0 1
# 0 1 0 8

# matrix2 =
# 4 4
# 9 8 7 13
# 15 14 0 1
# 3 7 2 3
# 0 9 0 35

matrix_1 = [[1, 1, 1, -1], [2, 2, 2, -2], [3, 3, 3, -3], [4, 4, 4, -4]]
matrix_2 = [[9, 15, 7], [8, 14, 5], [4, 3, 1]]

rows_1 = 4
columns_1 = 4

rows_2 = 2
columns_2 = 2

final = []


# a = matrix_2[0][0] * matrix_2[1][1]
# print(a)
# b = matrix_2[0][1] * matrix_2[1][0]
# print(b)
# det = a - b
# print(det)

# position = 0
# for j in matrix_2[0]:
#     new_matrix = []
#     for i in matrix_2:
#         if i is matrix_2[0]:
#             continue
#         else:
#             counter = 0
#             new_row = []
#             for x in i:
#                 if counter == position:
#                     counter += 1
#                     continue
#                 else:
#                     new_row.append(x)
#                     counter += 1
#         new_matrix.append(new_row)
#     print(new_matrix)
#     position += 1

def smaller(matrix, pos):
    new_matrix = []
    for row in matrix:
        if row is matrix_2[0]:
            continue
        else:
            counter = 0
            new_row = []
            for item in row:
                if counter == pos:
                    counter += 1
                    continue
                else:
                    new_row.append(item)
                    counter += 1
        new_matrix.append(new_row)
    return new_matrix


def calculate_determinant(matrix):
    total = 0

    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        position = 1
        for i in matrix[0]:
            if position % 2 == 0:
                total += -i * determinant(smaller(matrix, position - 1))
            else:
                total += i * determinant(smaller(matrix, position - 1))
            position += 1
        return total


print(determinant(matrix_2))
# fila = matrix_1[0]


# def row_calculator(matrix1, matrix2):
#     final_matrix = []
#     for row in matrix1:
#         new_row = []
#         for x in range(columns_2):
#             total = 0
#             for i in range(columns_1):
#                 total += row[i] * matrix2[i][x]
#             new_row.append(total)
#         final_matrix.append(new_row)
#     print(final_matrix)
#
#
# # row_calculator(matrix_1, matrix_2)
#
# # new_row = []
# # for row in matrix_1:
# #     new_row.append(row[0])
# # new_matrix = []
# # for i in range(columns_1):
# #     new_row = [row[i] for row in matrix_1]
# #     new_matrix.append(new_row)
# #
# # final = []
# # for i in new_matrix:
# #     i = i[::-1]
# #     # final.insert(0, final_row)
# #
# # print(new_matrix)
#
# def range_sum(numbers, start, end):
#     if not numbers:
#         return 0
#     suma = 0
#     for numb in numbers:
#         if start <= numb <= end:
#             suma += numb
#         else:
#             continue
#
#     return suma
#
#
# input_numbers = [int(i) for i in input() if i != ' ']
# a, b = [int(x) for x in input().split()]
# print(range_sum(input_numbers, a, b))
