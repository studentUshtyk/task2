import random

def generate_random_sorted_array(length, min_value=-10, max_value=10):
    array = [random.randint(min_value, max_value) for _ in range(length)]
    return sorted(array)

def merge(nums1, m, nums2, n):
    # Вказівники на кінці двох масивів
    i = m - 1  # останній елемент в частині nums1, яку потрібно об’єднати
    j = n - 1  # останній елемент в nums2
    k = m + n - 1  # останній індекс у загальному об'єднаному масиві

    # Порівнюємо елементи та заповнюємо nums1 з кінця
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

# Введення довжин масивів
m = int(input("Введіть кількість елементів у nums1: "))
n = int(input("Введіть кількість елементів у nums2: "))

# Генеруємо випадкові відсортовані масиви
nums1 = generate_random_sorted_array(m) + [0] * n  # Додаткові місця для об’єднання
nums2 = generate_random_sorted_array(n)

# Виводимо масиви перед об’єднанням
print("Масив nums1 перед об’єднанням:", nums1)
print("Масив nums2:", nums2)

# Об’єднуємо масиви
merge(nums1, m, nums2, n)

# Виводимо об’єднаний масив
print("Об’єднаний масив:", nums1)
