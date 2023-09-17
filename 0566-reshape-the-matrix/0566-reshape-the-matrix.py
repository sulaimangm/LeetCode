class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rLen = len(mat)
        cLen = len(mat[0])
        counter = 0
        temp = []
        newmat = []
        if rLen*cLen != r*c:
            return mat
        for i in range(rLen):
            for j in range(cLen):
                temp.append(mat[i][j])
                counter += 1
                if counter == c:
                    newmat.append(temp)
                    temp = []
                    counter = 0
        return newmat