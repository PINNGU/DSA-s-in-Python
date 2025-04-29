#counting sort , works very well with a unique time complexity and additional space complexity
#we have 3 arrays,the original one , unsorted , the new one (sorted ) , and the counter array
#based on amounts of keys-values in the original array , we assign those counts to our counter array
#we also increase each element by the amount of the predecessor element
#as example our original array is [1,2,3,3,4,5,5] (yes,this algorithm can work even with repeating values), our counter at start will be
#[0,1,1,2,1,2] , and after the additions = [0,1,2,3,5,8] , then we go through our unsorted array and assign values at locations based of counter
#indices - 1 , its difficult and it has good complexity mostly when we have low values (like a large array of only 1s,2s and 3s)
#the complexity of time is O(n + k) , where the k is how big the numbers go, in worst cases the biggest number can be in billions and smallest in single digits,
#sometimes making the k larger than the n itself

from plotting import plot_array


def counting(nums):

    counter = [0]* (max(nums)+1) #im pretty sure this max also does a O(n) on the list too, and alot of array inits, still adds to the same complexity of n+k
    sorted_nums = [0]*len(nums)

    for n in nums:
        counter[n] = counter[n] + 1

    for i in range(1,len(counter)):
        counter[i] = counter[i] + counter[i-1]
        plot_array(counter,"Counter of the Counting sort")


    for n in nums:
        sorted_nums[counter[n]-1] = n
        counter[n] = counter[n] - 1
        plot_array(sorted_nums,"Placing in counting Sort")

    




