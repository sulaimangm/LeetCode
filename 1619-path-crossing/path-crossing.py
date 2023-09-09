class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cordinates = [0,0]
        cordinateList = [[0,0]]
        for i in path:
            if (i == 'N'):
                cordinates[0] += 1
            if (i == 'S'):
                cordinates[0] -= 1    
            if (i == 'W'):
                cordinates[1] -= 1
            if (i == 'E'):
                cordinates[1] += 1
            if cordinates in cordinateList:
                return True
            cordinateList.append(cordinates.copy())
            print(cordinates,cordinateList)