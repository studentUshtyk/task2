import random

def generate_random_binary_array(length):
    return [random.randint(0, 1) for _ in range(length)]

def findMaxConsecutiveOnes(nums):
    max_count = 0  # максимальна кількість одиниць підряд
    current_count = 0  # лічильник поточного відрізка одиниць

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0  # обнуляємо, якщо зустріли 0

    return max_count

# Введення довжини масиву від користувача
length = int(input("Введіть довжину масиву: "))

# Генерація випадкового бінарного масиву
random_array = generate_random_binary_array(length)

# Виведення згенерованого масиву
print("Згенерований масив:", random_array)

# Пошук і виведення максимального відрізка одиниць
max_ones = findMaxConsecutiveOnes(random_array)
print("Максимальна кількість послідовних одиниць:", max_ones)
