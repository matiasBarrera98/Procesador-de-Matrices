import math
menu = "1. Add matrices\n2. Multiply matrix by a constant\n" \
       "3. Multiply matrices\n4. Transpose matrix\n" \
       "5. Calculate a determinant\n6. Inverse matrix\n0. Exit"

diagonal_menu = "1. Main diagonal\n2. Side diagonal\n3. Vertical line" \
                "\n4. Horizontal line"


class Matrix:

    @classmethod
    def sum_lists(cls, first_list, second_list):
        result_list = []
        for i in range(len(first_list)):
            result_list.append(first_list[i] + second_list[i])
        return result_list

    def __init__(self, n_rows, n_columns, matrix):
        self.rows = n_rows
        self.columns = n_columns
        self.matrix = matrix

    def __add__(self, second_matrix):
        if (second_matrix.rows == self.rows) and \
                (second_matrix.columns == self.columns):
            final_matrix = []
            for row in range(self.rows):
                new_row = \
                    Matrix.sum_lists(self.matrix[row], second_matrix.matrix[row])
                final_matrix.append(new_row)
            return final_matrix
        else:
            return None

    def __mul__(self, other):
        if self.columns == other.rows:
            final_matrix = []
            for row in self.matrix:
                new_row = []
                for x in range(other.columns):
                    total = 0
                    for i in range(self.columns):
                        total += row[i] * other.matrix[i][x]
                    new_row.append(total)
                # print(new_row)
                final_matrix.append(new_row)
            return final_matrix
        else:
            return None

    def number_multi(self, number):
        result_matrix = []
        # number = math.trunc(number)
        for row in self.matrix:
            new_row = [i * number for i in row]
            result_matrix.append(new_row)
        return result_matrix

    def main_diagonal(self):
        new_matrix = []
        for i in range(self.columns):
            new_row = [row[i] for row in self.matrix]
            new_matrix.append(new_row)
        return new_matrix

    def side_diagonal(self):
        matrix = self.main_diagonal()
        final_matrix = []
        for row in matrix:
            new_row = row[::-1]
            final_matrix.insert(0, new_row)
        return final_matrix

    def vertical_line(self):
        matrix = []
        for row in self.matrix:
            new_row = row[::-1]
            matrix.append(new_row)
        return matrix

    def horizontal_line(self):
        matrix = []
        for row in self.matrix:
            matrix.insert(0, row)
        return matrix

    def inverse_matrix(self):
        matrix = []
        row_pos = 0
        for row in self.matrix:
            new_row = []
            item_pos = 0
            for _ in row:
                cofactor = calculate_determinant(smaller(self.matrix, item_pos, row_pos))
                new_row.append((pow(-1, row_pos + 1 + item_pos + 1)) * cofactor)
                item_pos += 1
            matrix.append(new_row)
            row_pos += 1
        new_matrix = Matrix(self.rows, self.columns, matrix)
        transpose_matrix = Matrix(self.rows, self.columns, new_matrix.main_diagonal())
        # print(transpose_matrix.matrix)
        # print(int(1 / calculate_determinant(self.matrix) * 100) / 100)

        return transpose_matrix.number_multi(1 / calculate_determinant(self.matrix))


def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n


def print_matrix(matrix):
    print("The result is:")
    for i in matrix:
        # print(type(i))
        print(*i)


def capture_matrix(number=None):
    if number is not None:
        message = f" {number}"
    else:
        message = ""
    n_rows, n_columns = [int(x) for x in input(f"Enter size of{message} matrix: ").split()]
    full_matrix = []
    print(f"Enter{message} matrix:")
    for i in range(n_rows):
        row = [eval(item) for item in input().split() if item != ' ']
        full_matrix.append(row)
    return Matrix(n_rows, n_columns, full_matrix)


def add_matrices():
    matrix1 = capture_matrix("first")
    matrix2 = capture_matrix("second")
    if (matrix1 + matrix2) is not None:
        print_matrix(matrix1 + matrix2)
    else:
        print('The operation cannot be performed')


def constant():
    matrix = capture_matrix()
    number = eval(input("Enter constant: "))
    print_matrix(matrix.number_multi(number))


def multi_matrices():
    matrix1 = capture_matrix("first")
    matrix2 = capture_matrix("second")
    if (matrix1 * matrix2) is not None:
        print_matrix(matrix1 * matrix2)
    else:
        print('The operation cannot be performed')


def transpose():
    print(diagonal_menu)
    option = int(input("Your choice: "))
    matrix = capture_matrix()
    if option == 1:
        print_matrix(matrix.main_diagonal())
    elif option == 2:
        print_matrix(matrix.side_diagonal())
    elif option == 3:
        print_matrix(matrix.vertical_line())
    else:
        print_matrix(matrix.horizontal_line())


def smaller(matrix, pos, row_matrix=0):
    new_matrix = []
    for row in matrix:
        if row is matrix[row_matrix]:
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
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        position = 0
        for i in matrix[0]:
            if position % 2 == 0:
                total += i * calculate_determinant(smaller(matrix, position))
            else:
                total += -i * calculate_determinant(smaller(matrix, position))
            position += 1
        return total


def determinant():
    matrix = capture_matrix()
    print(calculate_determinant(matrix.matrix))


def inverse():
    matrix = capture_matrix()
    if calculate_determinant(matrix.matrix) == 0:
        print("This matrix doesn't have an inverse.")
    else:
        print_matrix(matrix.inverse_matrix())


def main_program():
    while True:
        print(menu)
        option = int(input("Your choice: "))
        if option == 1:
            add_matrices()
        elif option == 2:
            constant()
        elif option == 3:
            multi_matrices()
        elif option == 4:
            transpose()
        elif option == 5:
            determinant()
        elif option == 6:
            inverse()
        else:
            break


main_program()
