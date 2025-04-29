#quicksort , another divide and conquer algorithm , similar to mergesort , we find a pivot in the list (whatever we want)
#then we place all the elements on the side of the pivot , on the left the smaller ones , on the right the bigger ones (or vice versa)
#we recursively repeat the process , until everything is sorted , in each iteration one element will be in its right place
#time complexity is usually O(n*logn) but in worst cases when the pivot is bad it can reach O(n^2)

numbers = [2, 7, 54, 17, 29, 64, 43, 33, 47, 4, 82, 90, 40, 78, 92, 68, 76, 37, 19, 25]


def quick(nums,start,end):
    if start<end:
        pivot = sorting(nums,start,end)

        quick(nums,start,pivot-1)
        quick(nums,pivot+1,end)



def sorting(nums,start,end):

    p_index = ( start + end ) // 2
    pivot = nums[p_index]

    temp = nums[p_index]
    nums[p_index] = nums[end]
    nums[end] = temp

    i = start - 1

    for j in range(start,end):
        if nums[j] < pivot:
            i = i + 1

            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

    temp = nums[i+1]
    nums[i+1] = nums[end]
    nums[end] = temp
    return i+1


quick(numbers,0,len(numbers)-1)
print(numbers)


