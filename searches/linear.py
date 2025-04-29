#the most basic algorithm there is , the linear search , you will see it everywhere
#we basically just go through the array until we find our element , time complexity of O(n)

from plotting import plot_array

def alg(numbers,x):

    #the pythons implementation in one line of the linear search (under the hood), i use it here to showcase the id on the plot
    k = numbers.index(x)

    for i in range(0,len(numbers)):

        plot_array(numbers,"Linear Search",k,i)

        if numbers[i] == x:
            return i
        
    #if not found
    return -1
        
def linear(numbers,x):
    i = alg(numbers,x)
    if i == -1:
        print("The item does not exist in the array.")
    else:
        print("Item found at index ",i)