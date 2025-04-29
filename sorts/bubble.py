#the algorithm of bubble sort,in python
#pretty easy sorting algorithm , and also not as efficient , with a time complexity of O(n^2)
#goes through an array and compares the two adjacent elements , rearranging them in ascending or descending order
#every iteration , we get one sorted element ,and the rest unsorted , gets its name from the bubble effect , of bubbles rising to the end of the array
#inplace algorithm , pretty common for practices

from plotting import plot_array
import matplotlib.pyplot as plt


def bubble(numbers):

    for i in range(0,len(numbers)-1):
        for j in range(0,len(numbers)-i-1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
                plot_array(numbers,"Bubble Sort",j,j+1)
                
    
    

  
    print("Sorted array: ",numbers)

