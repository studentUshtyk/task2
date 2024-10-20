import random

def generate_random_array(size, low, high):
    nums = [random.randint(low, high) for _ in range(size)]
    nums.sort()  # Сортуємо масив
    return nums

def remove_duplicates(nums):
    if not nums:
        return 0

    k = 1  # Індекс для унікальних елементів

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k

# Приклад використання
# Генеруємо масив розміром 20 з випадковими числами від -10 до 10
random_nums = generate_random_array(20, -10, 10)
print("Згенерований масив:", random_nums)

result = remove_duplicates(random_nums)
print("Кількість унікальних елементів:", result)
print("Унікальні елементи:", random_nums[:result])
