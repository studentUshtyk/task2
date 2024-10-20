import random

def replace_with_largest_right(arr):
    n = len(arr)
    
    if n == 0:
        return arr

    max_right = arr[-1]
    
    arr[-1] = -1

    for i in range(n - 2, -1, -1):
        current = arr[i]
        arr[i] = max_right
        
        if current > max_right:
            max_right = current

    return arr

def generate_random_array(size, low, high):
    """Генерує масив випадкових цілих чисел."""
    return [random.randint(low, high) for _ in range(size)]

random_arr1 = generate_random_array(6, 1, 100)
print("Згенерований масив:", random_arr1)
result1 = replace_with_largest_right(random_arr1)
print("Результат:", result1)

random_arr2 = generate_random_array(1, 1, 100)
print("Згенерований масив:", random_arr2)
result2 = replace_with_largest_right(random_arr2)
print("Результат:", result2)
