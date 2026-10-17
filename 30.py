matrix=[[1,2,3],[4,5,6],[7,8,9]]
for row in matrix: print(row,"sum",sum(row))
print("Diagonal sum",sum(matrix[i][i] for i in range(3)))
