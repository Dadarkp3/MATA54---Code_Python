def busca_binaria(A, x):
    i = 0
    f = len(A) - 1
    while i <= f:
        m = (i + f) // 2
        if x == A[m]:
            return m
        else:
            if x < A[m]:
                f = m - 1
            else:
                i = m + 1
    return -1


if __name__ == "__main__":
    A = [1, 2, 3, 4, 10]
    print(busca_binaria(A, 1))
