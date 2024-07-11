import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(0, 102)

    while number != predict:
        count += 1
        if number > predict:
            predict = round((number + predict)/2) # Для сокращения числа попыток при поиске решения применим алгоритм бинарного поиска
        elif number < predict:
            predict = round((predict + number)/2)

    return count

print(game_core_v3(20))