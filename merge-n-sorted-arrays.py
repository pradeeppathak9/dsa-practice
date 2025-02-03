
def solution(arr):
    pointers = [0] * len(arr)
    res  = []
    while True:
        mpi = None
        for i in range(len(pointers)):
            if pointers[i] < len(arr[i]):
                if mpi is None or arr[i][pointers[i]] < arr[mpi][pointers[mpi]]:
                    mpi = i
        print(mpi, pointers)
        if mpi is None:
            break
            
        res.append(arr[mpi][pointers[mpi]])
        pointers[mpi] += 1
    return res


arr = [[1, 3, 5, 7], [2, 4, 6], [0, 9, 10, 11], [-1, 8]]
print(solution(arr))
# [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
