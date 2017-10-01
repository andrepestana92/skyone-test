def init_matrix(lines, columns):
    return [[(0,0,0) for i in range(lines)] for j in range(columns)]

def clear_matrix(matrix):
    try:
      return [[(0,0,0) for i in range(len(matrix))] for j in range(len(matrix[0]))]
    except IndexError:
      return matrix