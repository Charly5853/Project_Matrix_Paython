# for clear screen
import platform
import os
import time


#time.sleep(2)


""" Show matrix's element by row  """
def print_Matrix(m):
      for row in m:
         print(row)
 
""" Print Matrix's element by element """
def print_Matrix_by_Element(m):
     for row in m:
         for element in row:
             print(element)

# Print Matrix's elements in matri's format    
def print_Matrix_in_Matrix_Format(m):
     for row in m:
         for element in row:
             print(element, end=" , ")
         print() 

""" Prin matrix"s by  rows with coordenates"""
def print_Matrix_by_Coordenates(m):   
    for row in range(len(m)):
         for col in range(len(m[0])):
             num = m[row][col]
             print(num, end=" - ")
         print()  

""" Prin matrix"s by column with coordenates"""
def print_Matrix_by_Columns(m):   
     for col in range(len(m[0])):   
        for row in range(len(m)):
             num = m[row][col]
             print(num, end=" - ")
        print()  


""" sum_Matrix """
def sum_Matrix(m1,m2, r1):
     for row in range(len(m1)):
         for col in range(len(m1[0])):
             num1 = m1[row][col]
             num2 = m2[row][col] 
             result = num1 + num2  
             r1[row][col] = result
             #print(result, end=" - ")
          

# execution program in main function
def main():
     os.system("cls")

     # Statement of matrix
     matrixA = [[5,3],
                [-2,9],
                [7,-4]]
     
     rowA = len(matrixA)
     colA = len(matrixA[0])
     print(" Row Ma ", rowA  )
     print(" Col Ma ", colA)

     matrixB = [[-2,8,5,3],
               [5,-6,7,-7]]
     
     rowB = len(matrixB)
     colB = len(matrixB[0])
     print(" Row Mb ", rowB  )
     print(" Col Mb ", colB)
      
     #rows = len(matrixA[0]) # col matrixA  colA
     #columns = len(matrixB[0]) # col matrixB
     # create a temp matriX
     temMatrix = [[0 for _ in range(colB)] for _ in range(colA)]
     
  
     for row in range(len(temMatrix)):   
         for col in range(len(temMatrix[0])):
             temMatrix[row][col] = row
     print("+++++++++++++++++++ ")
     print_Matrix_by_Coordenates(temMatrix)
     print("+++++++++++++++++++ ")

     # create a temp multiply_Temp
     multiply_Temp_M = [[1 for _ in range(colB)] for _ in range(colA+1)]
     mResult = [[1 for _ in range(colB)] for _ in range(colA+1)]
     # Display the multiply_Temp_M row format
     print("Matrix A:")
     for row in multiply_Temp_M:
         print(row)

     # Change row matrixA in columns temMatrix
     for row5 in range(len(matrixA)): # by row
         print("")
         print(row5," $$$  Row   $$$$ ")
         for col in range(len(matrixA[0])): # by colummn
             num = matrixA[row5][col]
             print(num, end=" / ")
             
             for col2 in range(len(temMatrix[0])):
                 temMatrix[col][col2] = num
                 print(temMatrix[col][col2], end=" * ")

             print(" ")       
         print(" ****** ") 

         # Multipli matrix b and temp
         for row in range(len(matrixB)):
             for col in range(len(matrixB[0])):
                 num3 =  matrixB[row][col]
                 num4 = temMatrix[row][col] 
                 result = num3 * num4  
                 multiply_Temp_M[row][col] = result
                 print(num3 , " * ", num4, " = ", multiply_Temp_M[row][col])
             print(" > ")  

         # sum matrix's columns
         for col in range(len(multiply_Temp_M[0])):
             sum = 0
             for row in range(len(multiply_Temp_M)-1):
                  sum = sum + multiply_Temp_M[row][col]
             multiply_Temp_M[len(multiply_Temp_M)-1][col] = sum  
         
         # print mmultiply_Temp_M
         for row in multiply_Temp_M:
             print(row)          

         # put resul in each row
         for col in range(len(multiply_Temp_M[0])):
             num = multiply_Temp_M[len(multiply_Temp_M)-1][col]
             mResult[row5][col] = num

         # print mResult
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



 