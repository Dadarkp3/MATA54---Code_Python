def segundo_menor(A):
    primeiro = 100000000000000
    segundo = 10000000000000000
    for i in range(0, len(A)):
        if A[i] < primeiro:
            primeiro = A[i]
        elif (A[i] < segundo) and (A[i] != primeiro):
            segundo = A[i]
    return segundo


if __name__ == "__main__":
    A = [2, 3, 1]
    print(segundo_menor(A))
