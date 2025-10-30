def sum_negative_between_min_max(arr):
    if len(arr) < 3:
        return 0  # Невозможно быть элементов между минимумом и максимумом

    min_val = min(arr)
    max_val = max(arr)
    
    min_index = arr.index(min_val)
    max_index = arr.index(max_val)
    
    # Определяем границы диапазона (исключая сами min и max)
    left = min(min_index, max_index)
    right = max(min_index, max_index)
    
    # Элементы строго между ними
    segment = arr[left + 1:right]
    
    # Сумма только отрицательных элементов
    return sum(x for x in segment if x < 0)


# Пример использования
if __name__ == "__main__":
    # Можно заменить на ввод с клавиатуры или тестовые данные
    A = list(map(int, input("Введите элементы массива через пробел: ").split()))
    result = sum_negative_between_min_max(A)
    print("Сумма отрицательных элементов между минимумом и максимумом:", result)
