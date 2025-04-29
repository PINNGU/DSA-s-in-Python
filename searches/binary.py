#much better search algorithm with a time complexity of O(logn) , as best as we can do , however our array must be sorted first (a big downside)
#in cases where our array must be sorted this is a very good algorithm  - we find the midpoint and then compare to our search value - if our search value is 
#smaller we disregard the right half , and viceversa. we continue the same pattern using recursion , until we find our element
#for small arrays and unsorted ones binary might be slower

from sorts.merge import merge
from plotting import plot_array
from plotting import plot_binary_search


def alg(nums,x,loc,low = 0,high = None):

    if high == None:
        high = len(nums) - 1 

    if high < low:
        return -1
    
    mid = (low + high) // 2

    plot_binary_search(nums,low,mid,high)

    #best case on start,at the end reaches anyways
    if(nums[mid] == x):
        return mid;
    elif(x < nums[mid]):
        return alg(nums,x,loc,low,mid)
    elif(x > nums[mid]):
        return alg(nums,x,loc,mid,high)
    
 
def binary(nums,x):
    nums = merge(nums)
    loc = nums.index(x)

    i = alg(nums,x,loc)
    if(i == -1):
       print("The item does not exist in the array.")
    else:
        print("Item found at index ",i)