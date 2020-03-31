def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return recursive_search_helper(input_list, number, 0 , len(input_list)-1)

def recursive_search_helper(input_list, number, start_index, last_index):
    middle = (start_index + last_index) // 2
    #print(start_index, last_index)
    if start_index > last_index:
        return -1
        
    if input_list[middle] == number:
        return middle

    if input_list[middle] <= input_list[last_index]:
        if number >= input_list[middle] and number <= input_list[last_index]:
            return recursive_search_helper(input_list, number, middle+1, last_index)
        else:
            return recursive_search_helper(input_list, number, start_index, middle-1)
    elif number >= input_list[middle] or number <= input_list[last_index]:
        return recursive_search_helper(input_list, number, middle+1, last_index)
    else:
        return recursive_search_helper(input_list, number, start_index, middle-1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
#expected output: 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
print('-----------------------------')

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
#expected output: 5
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
print('-----------------------------')

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 8))
#expected output: 2
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
print('-----------------------------')

print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
#expected output: 5
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
print('-----------------------------')

print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10))
#expected output: -1
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
print('-----------------------------')

print(rotated_array_search([8,9,10,11,12,0,1,2,3,4,5,6,7], 10))
#expected output: 2
test_function([[8,9,10,11,12,0,1,2,3,4,5,6,7], 10])
print('-----------------------------')

print(rotated_array_search([8,9,10,11,12,0,1,2,3,4,5,6,7], 12))
#expected output: 4
test_function([[8,9,10,11,12,0,1,2,3,4,5,6,7], 12])
print('-----------------------------')

print(rotated_array_search([8,9,10,11,12,0,1,2,3,4,5,6,7], 8))
#expected output: 0
test_function([[8,9,10,11,12,0,1,2,3,4,5,6,7], 8])
print('-----------------------------')

print(rotated_array_search([8,9,10,11,12,0,1,2,3,4,5,6,7], 7))
#expected output: 12
test_function([[8,9,10,11,12,0,1,2,3,4,5,6,7], 7])
print('-----------------------------')

print(rotated_array_search([8,9,10,11,12,0,1,2,3,4,5,6,7], 0))
#expected output: 5
test_function([[8,9,10,11,12,0,1,2,3,4,5,6,7], 0])
print('-----------------------------')

print(rotated_array_search([8,9,10,11,12,0,1,2,3,4,5,6,7], 17))
#expected output: -1
test_function([[8,9,10,11,12,0,1,2,3,4,5,6,7], 17])
print('-----------------------------')

print(rotated_array_search([], 17))
#expected output: -1
test_function([[], 17])
print('-----------------------------')
