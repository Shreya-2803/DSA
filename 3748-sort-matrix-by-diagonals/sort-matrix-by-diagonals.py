from collections import defaultdict
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        g=len(grid)
        diag=defaultdict(list)
        for i in range(g):#hashmap insertion of diagonals
            for j in range(g):
                d=i-j
                diag[d].append(grid[i][j])
        for d in diag:#sorting and putting in order
            if d>=0:
                diag[d].sort(reverse=True)
            else:
                diag[d].sort()
        for i in range(g):
            for j in range(g):
                d=i-j
                grid[i][j]=diag[d].pop(0)
        return grid