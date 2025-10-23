binvalue = [1,2,3,4,5,6,7]

def bin(sortedArr,target):
    left = 0
    right = len(sortedArr)-1
    while left <= right:
        middle_index = (left+right) // 2 
        value = sortedArr[middle_index]
        if value == target:
            return middle_index 
        elif value > target:
            right = middle_index -1
        else:
            left = middle_index +1
    return None

data = bin(binvalue,7)
if data is None:
    print('Not founf')
else:
    print('Yes i am here ',data)