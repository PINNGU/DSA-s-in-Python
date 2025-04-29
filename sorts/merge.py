#a divide and conquer champ,beats the quicksort at worst cases , and keeps its time complexity of O(n*logn) all the time
#quite simple aswell, we divide at half point an array, creating 2 subarrays. then using recursion we continue the same process 
#until we are left with single elements,then we compare and merge them in order and backtrack to bigger arrays
#in the end we have everything sorted , with great time usage

from plotting import plot_merge


def merge(numbers):

    def combine(left,right):
        ret = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ret.append(left[i])
                i = i + 1
            else:
                ret.append(right[j])
                j = j + 1
            
            

        ret.extend(left[i:])
        ret.extend(right[j:])
        plot_merge(ret)
        return ret

    def divide(nums):
        if len(nums) <= 1:
            return nums

        middle = len(nums) // 2
        left = divide(nums[0:middle])
        right = divide(nums[middle:])

        
        return combine(left,right)


    sorted_numbers = divide(numbers)
    print(sorted_numbers)