import logging
import random

logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s') # Создание и настройка логгера

def get_n(): # Запрашивает у пользователя число N и проверяет его корректность.
    while True:
        try:
            n = int(input("Введите число N: "))
            if n < 1:
                raise ValueError("Число должно быть натуральным и больше 0.")
            return n
        except ValueError as e:
            print(e)
            logging.error(e)

n = get_n() # Запрос входных данных у пользователя

numbers = list(range(1, n+1)) # Создание списка с числами от 1 до N

random.shuffle(numbers) # Перемешивание списка

for num in numbers: # Вывод чисел пользователю
    print(num)
    logging.info(f'Выпало число: {num}')
