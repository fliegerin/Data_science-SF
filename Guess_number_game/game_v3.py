
import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Устанавливаем число - середину диапазона, затем в зависимости от того, больше или меньше загаданное число, сдвигаем диапазон и снова предполагаем его середину - до тех пор, пока диапазон не сузится до загаданного числа.
       Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    minimum = 1
    maximum = 100
    predict = (minimum+maximum) // 2
    
    if predict == number:
        count = 1

    while number != predict:
        count += 1
        if predict < number:
            minimum = predict + 1
            predict = (minimum + maximum) // 2 

        elif predict > number:
            maximum = predict - 1
            predict = (minimum + maximum) // 2


    # Ваш код заканчивается здесь

    return count

from game_v2 import score_game
score_game(game_core_v3)