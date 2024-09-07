'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# for clear screen
import platform
import os
import time


#time.sleep(2)


""" Show matrix's element by row  """
def print_Matrix(m):
      for row in m:
         print(row)
         
""" sum_Matrix """
def sum_Matrix(m1,m2, r1):
     for row in range(len(m1)):
         for col in range(len(m1[0])):
             num1 = m1[row][col]
             num2 = m2[row][col] 
             result = num1 + num2  
             r1[row][col] = result
             #print(result, end=" - ")
             
def function_Transpose_Matrix(m2, transposeMatrix2):
         matrix_length_Y = len(m2) 
         matrix_length_X = len(m2[0])
         #print(" Rows = ",matrix_length_Y)
         #print(" Columns = ",matrix_length_X)
         #print(" Print matrix ")
         
         for column2 in range(matrix_length_X):
             for row2 in range(matrix_length_Y):
                 #print(m2[row2][column2], end = " ")
                 num = m2[row2][column2]
                 transposeMatrix2[column2][row2] = num
                 #print(transposeMatrix[column2][row2], end = " ")
             print()                
def function_Multiply_Matrix(matrixB, temMatrix, multiply_Temp_M):   
     for row3 in range(len(matrixB)):
         for col3 in range(len(matrixB[0])):
             num3 =  matrixB[row3][col3]
             num4 = temMatrix[row3][col3] 
             result = num3 * num4  
             multiply_Temp_M[row3][col3] = result
             #print(num3 , " * ", num4, " = ", multiply_Temp_M[row3][col3])
             #print(" > print  multiply_Temp_M ")       

# execution program in main function
def main():
     os.system("cls")

     # Statement of matrix
     matrixA = [[5,3],
                [-2,9],
                [7,-4]]
     print_Matrix(matrixA)
     rowA = len(matrixA)
     colA = len(matrixA[0])
     print(" Row Ma ", rowA)
     print(" Col Ma ", colA)
     
     #create TransposeMatrix
     print(" ")
     print(" >>>>>>>>>>>> Transpose Matrix ")
     transpose_Matrix = [[0 for x in range(rowA)] for y in range(colA)] # x = width, y = height
     function_Transpose_Matrix(matrixA, transpose_Matrix)
     print_Matrix(transpose_Matrix)
     
     
     print(" ")
     print(" >>>>>>>>>>>> Matrix B ")
     matrixB = [[-2,8,5,3],
               [5,-6,7,-7]]
     rowB = len(matrixB)
     colB = len(matrixB[0])
     print(" Row Mb ", rowB  )
     print(" Col Mb ", colB)
     print_Matrix(matrixB)
     
     #rows = len(matrixA[0]) # col matrixA  colA
     #columns = len(matrixB[0]) # col matrixB
     # create a temp matriX
     temMatrix = [[0 for _ in range(colB)] for _ in range(colA)]
    
     for row in range(len(temMatrix)):   
         for col in range(len(temMatrix[0])):
             temMatrix[row][col] = row
     print("++++++++++++ Temporal Matrix ")
     print_Matrix(temMatrix)
     print("+++++++++++++++++++ ")
     
     # create a multiply_Temp
     multiply_Temp_M = [[1 for _ in range(colB)] for _ in range(colA+1)]
     mResult = [[1 for _ in range(colB)] for _ in range(colA+1)]
     # Display the multiply_Temp_M row format
     print("Create a multiply_Temp")
     print("Matrix multiply_Temp_M:")
     for row in multiply_Temp_M:
         print(row)
       
     
     # copy column transpose_Matrix in to columns temMatrix
     for col in range(len(transpose_Matrix[0])): # by colummn
         print("")
         print(col," $$$  Row   $$$$ ")
         for row2 in range(len(transpose_Matrix)): # by row
             num = transpose_Matrix[row2][col]
             print(num, end=" / ")
             
             for col2 in range(len(temMatrix[0])):
                 temMatrix[row2][col2] = num
                 #print(temMatrix[row5][col2], end=" * ")

             print(" - ") 
         print_Matrix(temMatrix)    
         print(" ^^^^^^^^^^^^^^^^^ ")  
         # Multiply matrixB * temMatrix = multiply_Temp_M
         function_Multiply_Matrix(matrixB, temMatrix, multiply_Temp_M)    
         print_Matrix(multiply_Temp_M)   
       
         # sum multiply_Temp_M's columns and put result at las row
         for col4 in range(len(multiply_Temp_M[0])):
             sum = 0
             for row4 in range(len(multiply_Temp_M)-1):
                  sum = sum + multiply_Temp_M[row4][col4]
                  multiply_Temp_M[len(multiply_Temp_M)-1][col4] = sum  
         print(" > sum multiply_Temp_M's columns and put result at las row ")  
         print_Matrix(multiply_Temp_M)
         print(" > !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")  
    
         # put results of multiply_Temp_M at mResult
         row5 = col
         for col5 in range(len(multiply_Temp_M[0])):
             num = multiply_Temp_M[len(multiply_Temp_M)-1][col5]
             mResult[row5][col5] = num
     
         # print mResult
         for row6 in mResult:
             print(row6)    
     print(row5, " Matrix  Result >>>>>>>>>>>>>>>> ")      
     for row6 in mResult:
         print(row6)
     
main()

 #multiply_Matrix(matrixA,matrixB, matrixR)
     
""" Show matrix's element by row  """
     # print("  Show matrix's element by row  ")
     # print_Matrix(matrixA)

""" Print Matrix's element by element """
     # print(" Print Matrix's element by element ")
     # print_Matrix_by_Element(matrixA)

     # Print Matrix's elements in matrix's format: 
     # print(" Print Matrix's elements in matri's format")
     # print_Matrix_in_Matrix_Format(matrixA)

""" Print matrix"s by coordenates rows and col  """
     #print(" Print matrix  by coordenates rows and   ")
     #print_Matrix_by_Coordenates(matrixB)

     #print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
     #print_Matrix_by_Columns(matrixB)
     #sum_Matrix(matrixA,matrixB, matrixR)
     #print_Matrix_in_Matrix_Format(matrixA)


""" 
     matrixA = [[1,2,3],
                [4,5,6],
                [7,8,9]]
     
     matrixB = [[10,20,30],
                [40,50,60],
                [70,80,90]]
     
     matrixR = [[0,0,0],
                [0,0,0],
                [0,0,0]]
     
     matrixA = [[5,3,-4,2],
                [8,-1,0,-3]]
     
     matrixB = [[1,4.0],
                [-5,3,7],
                [0,9,5],
                [5,1,4]]
     
     matrixR = [[1,2,3],
                [1,2,3]]
              
                
                  
                    
                        """



 