
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