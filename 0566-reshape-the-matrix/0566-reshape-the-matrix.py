class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rLen = len(mat)
        cLen = len(mat[0])
        temp = []
        newmat = []
        if rLen*cLen != r*c:
            return mat
        for i in range(rLen):
            for j in range(cLen):
                temp.append(mat[i][j])
                if len(temp) == c:
                    newmat.append(temp)
                    temp = []
        return newmat