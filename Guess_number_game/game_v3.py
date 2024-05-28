
import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Устанавливаем любое random число, потом уменьшаем или 
    увеличиваем его на 2 в зависимости от того, четные числа или нечетные.
       Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number % 2 == 0:
            if predict % 2 == 0:
                if number > predict:
                    predict += 2
                elif number < predict:
                    predict -= 2
            else:
                predict += 1
        else: 
            if predict % 2 != 0:
                if number > predict:
                    predict += 2
                elif number < predict:
                    predict -= 2
            else:
                predict += 1

    # Ваш код заканчивается здесь

    return count

from game_v2 import score_game
score_game(game_core_v3)