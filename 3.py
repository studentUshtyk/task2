import random

def generate_random_sorted_array(length, min_value=-10000, max_value=10000):
    array = [random.randint(min_value, max_value) for _ in range(length)]
    return sorted(array)

def sorted_squares(nums):
    n = len(nums)
    result = [0] * n  # масив для збереження результату
    left, right = 0, n - 1  # два вказівники
    index = n - 1  # заповнюємо масив з кінця

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        if left_square > right_square:
            result[index] = left_square
            left += 1
        else:
            result[index] = right_square
            right -= 1
        index -= 1

    return result

# Введення довжини масиву від користувача
length = int(input("Введіть довжину масиву: "))

# Генеруємо випадковий відсортований масив
random_array = generate_random_sorted_array(length)

# Виводимо масив на екран
print("Згенерований масив:", random_array)

# Обчислюємо та виводимо відсортовані квадрати чисел
squared_array = sorted_squares(random_array)
print("Відсортовані квадрати:", squared_array)
