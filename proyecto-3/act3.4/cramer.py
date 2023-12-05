'''
    Originally written by Equipo 1 @ EDA II Fi-UNAM
'''

import numpy as np 
def det(mat):
    n = len(mat)

    # Base case
    if n == 1:
        return mat[0][0]
    
    result = 0
    for i in range(n):
        cofactor = (-1)**i * mat[0][i]
        submat = [row[:i] +row[i+1:] for row in mat[1:]]
        subdet = det(submat)
        result +=  cofactor * subdet
    return result

def cramer(mat, const):
    n = len(mat)
    D = det(mat)
    if D != 0:
        solutions = []
        for i in range(n):
            mat_copy = [row[:] for row in mat]
            for j in range(n):
                mat_copy[j][i] = const[j]
            Di = det(mat_copy)
            xi = Di / D
            solutions.append(xi)

        return tuple(solutions)
    return None

if __name__ == '__main__':
    a = [[10, 40, 70], [20, 50, 80], [30, 60, 80]] 
    b = [300, 360, 390]

    print(f"Solution: {cramer(a,b)}")
    print(f"Solution: {np.linalg.inv(a).dot(b)}")