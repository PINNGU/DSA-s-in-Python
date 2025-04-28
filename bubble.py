#the algorithm of bubble sort,in python
#pretty easy sorting algorithm , and also not as efficient , with a time complexity of O(n^2)
#goes through an array and compares the two adjacent elements , rearranging them in ascending or descending order
#every iteration , we get one sorted element ,and the rest unsorted , gets its name from the bubble effect , of bubbles rising to the end of the array
#inplace algorithm , pretty common for practices


numbers = [2, 7, 54, 17, 29, 64, 43, 33, 47, 4, 82, 90, 40, 78, 92, 68, 76, 37, 19, 25]


for i in range(0,len(numbers)-1):
    for j in range(i+1,len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

    print(numbers)

print("Sorted array: ",numbers)

