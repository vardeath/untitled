matrix = [
    [25, 10, 11, 12, 13],
    [24, 9, 2, 3, 14],
    [23, 8, 1, 4, 15],
    [22, 7, 6, 5, 16],
    [21, 20, 19, 18, 17],
]
# size = int(input())
# matrix = []
# for i in range(size):
#     raw = tuple([int(x) for j, x in enumerate(input().split()) if j < size])
#     matrix.append(raw)


class Point:
    def __init__(self, x_pos, y_pos):
        self.X = x_pos
        self.Y = y_pos

    def __str__(self):
        return f' X = {self.X} | Y = {self.Y}'


center_matrix = Point(len(matrix) // 2, len(matrix) // 2)
m_points = {}


def set_matrix_points(matrix_size):
    half_size = matrix_size // 2
    m_points['first_point'] = Point(
        center_matrix.X - half_size,
        center_matrix.Y - half_size
    )
    m_points['second_point'] = Point(
        center_matrix.X + half_size,
        center_matrix.Y - half_size
    )
    m_points['third_point'] = Point(
        center_matrix.X + half_size,
        center_matrix.Y + half_size
    )
    m_points['forth_point'] = Point(
        center_matrix.X - half_size,
        center_matrix.Y + half_size
    )


def spiral_print(start_point, matrix_size=1):
    if matrix_size == 1:
        if len(matrix) == 1:
            print(matrix[0][0])
            return
        else:
            print(matrix[start_point.X][start_point.Y])
        next_start_point = Point(center_matrix.X, center_matrix.Y - 1)
        matrix_size += 2
        spiral_print(next_start_point, matrix_size)
    else:
        set_matrix_points(matrix_size)

        y = m_points['first_point'].Y
        for x in range(start_point.X, m_points['second_point'].X + 1, 1):
            print(matrix[y][x])
        x = m_points['second_point'].X
        for y in range(
            m_points['second_point'].Y + 1, m_points['third_point'].Y + 1, 1
        ):
            print(matrix[y][x])
        y = m_points['forth_point'].Y
        for x in range(
            m_points['third_point'].X - 1, m_points['forth_point'].X - 1, -1
        ):
            print(matrix[y][x])
        x = m_points['first_point'].X
        for y in range(
            m_points['forth_point'].Y - 1, m_points['first_point'].Y - 1, -1
        ):
            print(matrix[y][x])

        if matrix_size == len(matrix):
            return
        next_point = Point(
            m_points['first_point'].X, m_points['first_point'].Y - 1
        )
        matrix_size += 2
        spiral_print(next_point, matrix_size)


spiral_print(center_matrix)
