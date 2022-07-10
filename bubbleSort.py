def bubbleSort(listOfNo):

    #Iterate through the list as many times as there are elements
   for i in range(len(listOfNo)):
    #Iterate through list but only go to the end of sequence - 1
    #due to the if statement always comparing the number infront (j+1)
    for j in range(len(listOfNo)-1):
        if listOfNo[j] > listOfNo[j+1]:
            #swap
            listOfNo[j], listOfNo[j+1] = listOfNo[j+1], listOfNo[j]
    print(listOfNo)


def optimized_bubble_sort(b_list):
    has_swapped = True

    while(has_swapped):
        has_swapped = False
        for i in range(len(b_list) - 1):
            if b_list[i] > b_list[i+1]:
                # Swap
                b_list[i], b_list[i+1] = b_list[i+1], b_list[i]
                has_swapped = True

                
if __name__ == '__main__':
 
    A = [3, 8, 5, 4, 1, 9, -2]
 
    bubbleSort(A)