#similar to selection as it also separates into unsorted and sorted as its happening , we start from the second element
#each element compares itself to the sub array before it , until it finds its sorted place inbetween , and then switches places
#its time complexity is also O(n^2)

from plotting import plot_array

def insertion(numbers):
    for i in range(1,len(numbers)):
        for j in range(i-1,-1,-1):
            if numbers[j+1] < numbers[j]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
                plot_array(numbers,"Insertion",j,j+1)




    print("Sorted array: ",numbers)

