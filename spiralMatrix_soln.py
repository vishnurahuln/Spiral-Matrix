from typing import List


class spiralMatrix:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
            res = [] 
            self.helper(matrix,0,0,res)
            return res
        
        
    def helper(self,matrix: List[List[int]],i: int,j: int,res: List[int]):
        if i < 0 or i >= len(matrix) or j < 0 or j>=len(matrix[0]) or matrix[i][j] == '#':
            return

        if len(res) == (len(matrix))*(len(matrix[0])):
            return
        
        res.append(matrix[i][j])
        matrix[i][j] = '#'
        
        
        if j+1>=i:
            self.helper(matrix,i,j+1,res)
        self.helper(matrix,i+1,j,res)
        self.helper(matrix,i,j-1,res)
        self.helper(matrix,i-1,j,res)


def main():
    sol = spiralMatrix()
    matrix_ = [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40],[41,42,43,44,45,46,47,48,49,50],[51,52,53,54,55,56,57,58,59,60],[61,62,63,64,65,66,67,68,69,70],[71,72,73,74,75,76,77,78,79,80],[81,82,83,84,85,86,87,88,89,90],[91,92,93,94,95,96,97,98,99,100]]
    print(sol.spiralOrder(matrix_))
    matrix_ =[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    print(sol.spiralOrder(matrix_))
    matrix_ =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(sol.spiralOrder(matrix_))

if __name__ == "__main__":
    main()
