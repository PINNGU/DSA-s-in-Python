#similar to selection as it also separates into unsorted and sorted as its happening , we start from the second element
#each element compares itself to the sub array before it , until it finds its sorted place inbetween , and then switches places
#its time complexity is also O(n^2)

numbers = [2, 7, 54, 17, 29, 64, 43, 33, 47, 4, 82, 90, 40, 78, 92, 68, 76, 37, 19, 25]

for i in range(1,len(numbers)):
    for j in range(i-1,-1,-1):
        if numbers[j+1] < numbers[j]:
            temp = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = temp


    print(numbers)

print("Sorted array: ",numbers)

