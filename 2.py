import random

def generate_random_array(length, min_value=1, max_value=100000):
    return [random.randint(min_value, max_value) for _ in range(length)]
def count_even_digit_numbers(nums):
    count = 0
    for num in nums:
        if len(str(num)) % 2 == 0:  # Перевіряємо кількість цифр
            count += 1
    return count

# Введення довжини масиву від користувача
length = int(input("Введіть довжину масиву: "))

# Генеруємо випадковий масив чисел
random_array = generate_random_array(length)

# Виводимо масив на екран
print("Згенерований масив:", random_array)

# Знаходимо кількість чисел з парною кількістю цифр
result = count_even_digit_numbers(random_array)
print("Кількість чисел з парною кількістю цифр:", result)
