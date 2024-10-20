def check_if_double_exists(arr):
    seen = set()  # Створюємо множину для зберігання елементів масиву

    for num in arr:
        # Перевіряємо, чи є подвійник для поточного елемента
        if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)  # Додаємо поточний елемент у множину

    return False  # Якщо не знайдено, повертаємо False

arr1 = [10, 2, 5, 3]
print(check_if_double_exists(arr1))  # Виведе: True

arr2 = [3, 1, 7, 11]
print(check_if_double_exists(arr2))  # Виведе: False
