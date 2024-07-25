def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    length = len(matrix)

    TL_BR_sum = 0
    BL_TR_sum = 0

    for i in range(length):
        TL_BR_sum += matrix[i][i]
        BL_TR_sum += matrix[i][length - 1 - i]
    
    return TL_BR_sum + BL_TR_sum