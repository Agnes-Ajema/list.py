#write a python program to remove duplicates from a list
x = [1,2,3,4,1,2,5,6,3,7,8,1]

duplicates = set()
uniqueArray = []
for i in x:
    if i  not in duplicates:
        uniqueArray.append(i)
        duplicates.add(i)

        print(uniqueArray)


#write a python program to print the numbers of a specified list after removing even numbers from it.
numbers = [2,5,7,8,10,7,42]  

numbers = [x for x in numbers if x % 2 !=0]
print(numbers)

#write a python program to get the largest number from a list

def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a 
            return max
            print(max_num_in_list([3,6,9,-1]))


