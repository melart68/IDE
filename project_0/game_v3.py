
"""Игра угадай число.
Компютер сам загадывает и угадывает число
"""
import numpy as np
def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число
    
    Args:
        number (int, optional): Загадоное число. Defaults to 1.
        Returns: 
             int: Число попыток 
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break
    return (count)
print(f'Количество попыток: {random_predict()}')


def score_game(random_perdict) -> int:
     """ За какое количество попыток в среднем из 1000 подходов
    угадываем число наш алгаритм
    
    Args:
        random ([type]): Функция угадывания.
        Returns: 
             int: Среднее количество попыток 
    """
    
     count_ls = [] # список для сохранения количества попыток
     np.random.seed(1) # фиксируем сид для воспроизводимости
     random_arry = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
     for number in random_arry:
         count_ls.append(random_perdict(number))
    
     score = int(np.mean(count_ls)) # находим среднее количество попыток
    
     print(f'Ваш алгаритм угадывает число в среднем за: {score} попыток')
     return(score)
if __name__ == '__main__':
     score_game(random_predict)
     
     
def game_core_v3(number: int = 1) -> int:
    """Сначала задаем начальное random число (predict), затем зная диапазон в котором загадано число, определяем его границы start и finish.
    Создаем цикл, условием выхода из цикла будет равенство переданного в функцию числа (number) с подобранным числом (predict).
    В качестве условий сравниваем числа predict и number, и в зависимости от знака равенства < или > сдвигаем границы,
    презаписывая значения переменных start или finish.
    Затем производим расчет нового значения для (predict) и снова сравниваем, до тех пор пока не угадаем (number),
    т.е. когда выполнится условие number == predict

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    predict = np.random.randint(1, 101)
    start = 0
    finish = 101

    while number != predict:
        count += 1
        if predict < number:
            start = predict
        elif predict > number:
            finish = predict
        predict = (start + finish) // 2

    return count
game_core_v3()

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)