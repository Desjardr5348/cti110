#CTI-110
#P2HW2 - Lists and Sets
#Ronald Desjardins
#11 OCT 2021 
#
#Ask the user to enter a series of 6 numbers
num_1 = float(input("Enter num 1:"))
num_2 = float(input("Enter num 2:"))
num_3 = float(input("Enter num 3:"))
num_4 = float(input("Enter num 4:"))
num_5 = float(input("Enter num 5:"))
num_6 = float(input("Enter num 6:"))

#Space in output
print()

#numList
numList = [num_1,num_2,num_3,num_4,num_5,num_6]

#Output lowest number in the list
print("Smallest number in list:", min(numList))

#Output highest number in the list
print("Highest number in list:", max(numList))

#Output sum of all numbers in the list
print("Sum of numbers", sum(numList))

#Output average of all numbers in the list
print("Average of numbers in list", sum(numList) / len(numList))

#Space in output
print()

#Define numSet and output said numSet
numSet = set(numList)
print("Create Set")
print(numSet)