# Group 12
# Dani Ghanie U83713490
# Aaron Acevedo U89664173

#reads the file to use as input
def read(name):
    file = open(name, "r") 
    line = file.readline()
    values = []
    for value in line.split(' '):
        values.append(int(value))
    return values

def BinarySearch(numbers, low, high, key):
    if low > high: # base condition
        return -1

    mid = (low + high) // 2 #calculates mid point of array

    # check to see where the numbers are
    if numbers[mid] < key:
        return BinarySearch(numbers, mid + 1, high, key) #searches right half of array
    elif numbers[mid] > key:
        return BinarySearch(numbers, low, mid - 1, key) #searches left half of array

    return mid


nums = read("test1.txt")#reads test file
target = int(input("Enter the target number: ")) #asks for target number
key = BinarySearch(nums, 0, len(nums) - 1, target)

if key == -1:
   print(f"Cannot find {target} in array.")
else:
   print(f"{target} is in {key + 1}th place in array")