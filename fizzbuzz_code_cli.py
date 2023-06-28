# Напишите CLI-утилиту, которая при запуске будет запрашивать число у пользователя
# и давать ответ - Fizz, Buzz, FizzBuzz или число.
# Запуск приложения выводит приветствие и спрашивает число,
# на каждый ввод числа (ввод чисел происходит, пока пользователь не завершит процесс) .
#
# При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»,
# а вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»"
# В остальных случаях - само число

import click


@click.command()
@click.option('--boll-click', default=True, help='Флажок ввода number через опцию')
@click.option('--number', prompt="Welcome to Fizz Buzz ! "
                                 "\nSubmit a number and get an answer! Number 0 - Stop process!"
                                 "\nPlease enter a Number", type=str,
              help='Your Number to analyse, Number 0 - Stop process!')
def run_and_stop(number, boll_click):                        # Главная функция запускает и остановки программы
    """
    Args:
        number:     - вводимое число с консоля
        boll_click: - Флажок ввода number True - непосредствено через опцию
    Returns:
    """
    while True:                                              # Цикл по вводу значения, выход если значение число 0
        n, boll_click = enter_number(number, boll_click)
        if n != 0:
            click.echo(fizzbuzz(n))
        else:
            break
    click.echo(f"Stop, as Number:{n}")
    return


def enter_number(number, boll_click):                          # Функция ввода значения
    """
    Args:
        number:     - вводимое число с консоля
        boll_click: - Флажок ввода number True - непосредствено через опцию
    Returns: number, boll_click
    """
    while True:                                                # Цикл по вводу значения и проверка на число
        try:
            if not boll_click: number = input("Please enter a Number: ")
            boll_click = False
            number = int(number)
            break
        except (ValueError, TypeError):
            print('Error! Need enter a number!')
    return number, boll_click


def fizzbuzz(number):                                           # Функция реализации алгоритма FizzBuzz
    """
    Args:
        number:     - вводимое число с консоля
    Returns:
        string      - результат анализа числа: "Fizz", "Buzz", "FizzBuzz" или число
    """
    string = ""
    if number != 0:
        if number % 15 == 0:
            string = "FizzBuzz"
        elif number % 3 == 0 and number % 5 != 0:
            string = "Fizz"
        elif number % 5 == 0 and number % 3 != 0:
            string = "Buzz"
        else:
            string = number
    return string


if __name__ == '__main__':
    run_and_stop()
