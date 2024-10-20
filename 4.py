import random

def generate_random_array(length):
    return [random.randint(0, 9) for _ in range(length)]

def duplicate_zeros(arr):
    i = 0
    length = len(arr)

    while i < length:
        if arr[i] == 0:
            # Вставляємо 0 і зсуваємо решту елементів вправо
            arr.insert(i, 0)
            arr.pop()  # Видаляємо останній елемент, щоб зберегти розмір масиву
            i += 2  # Пропускаємо вставлений 0
        else:
            i += 1

# Введення довжини масиву від користувача
length = int(input("Введіть довжину масиву: "))

# Генеруємо випадковий масив чисел
random_array = generate_random_array(length)

# Виводимо масив перед змінами
print("Згенерований масив:", random_array)

# Дублюємо нулі в масиві
duplicate_zeros(random_array)

# Виводимо масив після змін
print("Масив після дублювання нулів:", random_array)
