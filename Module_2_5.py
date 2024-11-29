def get_matrix (N, M, Value):
    matrix = []
    for i in range(N):
        list_ = []
        matrix.append(list_)
        for j in range(M):
            list_.append(Value)

    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)