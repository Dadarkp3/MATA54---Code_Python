def linear_search(A, x):
    for i in range(len(A)):
        if A[i] == x:
            return True
    return False


if __name__=="__main__":
    A = [10,20,-1,19,40]
    print(linear_search(A, 1))