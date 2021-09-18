def sumEvenAfterQueries(A, queries):
    res = []
    tem = 0
    for a in A:
        if a % 2 == 0:
            tem += a
    for val,index in queries:
        a = A[index]
        A[index] += val
        if a % 2==0:
            if A[index] % 2 == 0:
                tem += val
            else:
                tem -= a
        else:
            if A[index] % 2 == 0:
                tem += A[index]
        res.append(tem)
    return res

if __name__ == '__main__':
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    print(sumEvenAfterQueries(A,queries))