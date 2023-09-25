"""Алгоритм угадывания числа, улучшенная версия """
import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return count

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count

def game_core_v3(number: int = 1) -> int:
    """Сначала случайным образом устанавливаем число в середине данного нам диапазона,
    то есть 50 или 51, а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного. Величина коррекции начинается с 25 и с
    каждой новой итерацией уменьшаем её значение вдвое с округлением до целых. По 
    сути используем метод половинного деления. Если в какой-то момент величина 
    коррекции доходит до 0, приравниваем её к 1. Таким образом решаем проблему краевого
    эффекта, который случается, если загадано число 100, а алгоритм начал работу с числа
    50, или если загадано число 1, а алгоритм начал работу с числа 51.
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(50, 52)
    # Начальная величина коррекции
    predict_corr = 25
    while number != predict:
        count += 1
        if number > predict:
            predict += predict_corr
        elif number < predict:
            predict -= predict_corr
        # Величина коррекции в следующей итерации
        predict_corr = round(predict_corr/2)
        if predict_corr == 0:
            predict_corr = 1
    return count

def score_game(random_pred) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000) # загадали список чисел

    for number in random_array:
        count_ls.append(random_pred(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)
    score_game(game_core_v2)
    score_game(game_core_v3)
    