

def insertionSortAlgorithm(A):

    for i in range(1, len(A)):
        
        #Assign "value" to the number in the position i
        value = A[i]

        #Create a new variable that is identical to the index i
        j=i
        

        #while j is less than 0 and the value in the position 1 before j
        #is greater than the current value then we execute the while list
        while j>0 and A[j-1] > value:
            A[j] = A[j-1]
            j=j-1

        #Either the value stays the same or because j index value changes if 
        A[j] = value

if __name__ == '__main__':
 
    A = [3, 8, 5, 4, 1, 9, -2]
 
    insertionSortAlgorithm(A)
 
