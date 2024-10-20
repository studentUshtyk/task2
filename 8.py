def valid_mountain_array(arr):
    n = len(arr)
    if n < 3:
        return False

    i = 0
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    # Перевіряємо, чи досягли піку (i не може бути 0 або n-1)
    if i == 0 or i == n - 1:
        return False

    # Перевіряємо спадання
    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    # Якщо досягли кінця масиву, то це дійсний гірський масив
    return i == n - 1

print(valid_mountain_array([2, 1]))           # Виведе: False
print(valid_mountain_array([3, 5, 5]))         # Виведе: False
print(valid_mountain_array([0, 3, 2, 1]))      # Виведе: True
print(valid_mountain_array([0, 1, 2, 3, 4, 2, 1]))  # Виведе: True
print(valid_mountain_array([0, 2, 3, 3, 5, 2, 1]))  # Виведе: False
