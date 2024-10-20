def sort_array_by_parity(nums):
    
    evens = [num for num in nums if num % 2 == 0]
    odds = [num for num in nums if num % 2 != 0]
    

    return evens + odds

print(sort_array_by_parity([3, 1, 2, 4]))
print(sort_array_by_parity([0]))    
print(sort_array_by_parity([1, 3, 5]))      
print(sort_array_by_parity([2, 4, 6]))
