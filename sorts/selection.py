#also not that of an efficient algorithm, but a popular one nevertheless , as its simple and splits the array as it progresses in sorted and unsorted
#goes through and finds the smallest or largest element,then it switches the positions with the first one
#then continues to the second and third and so forth
#time compl of O(n^2) , as we loop through everything to find and again to iterate

from sorts.plotting import plot_array

def selection(numbers):

    for i in range(0,len(numbers)):
        curr_i = i
        for j in range(i,len(numbers)):
            if numbers[j] < numbers[curr_i]:
                curr_i = j
                plot_array(numbers,"Selection",curr_i,i)

        temp = numbers[i]
        numbers[i] = numbers[curr_i]
        numbers[curr_i] = temp

        
        

    print("Sorted array: ",numbers)



     