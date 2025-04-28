#also not that of an efficient algorithm, but a popular one nevertheless , as its simple and splits the array as it progresses in sorted and unsorted
#goes through and finds the smallest or largest element,then it switches the positions with the first one
#then continues to the second and third and so forth
#time compl of O(n^2) , as we loop through everything to find and again to iterate

numbers = [2, 7, 54, 17, 29, 64, 43, 33, 47, 4, 82, 90, 40, 78, 92, 68, 76, 37, 19, 25]



for i in range(0,len(numbers)):
    curr_i = i
    for j in range(i,len(numbers)):
        if numbers[j] < numbers[curr_i]:
            curr_i = j

    temp = numbers[i]
    numbers[i] = numbers[curr_i]
    numbers[curr_i] = temp

    print(numbers)

print("Sorted array: ",numbers)



     