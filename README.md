# project-FizzBuzz
Тестовое задание для ментора (Hexlet)

## __Задача FizzBuzz на Python__
При запуске программы запрашивать число у пользователя
и выдается ответ - Fizz, Buzz, FizzBuzz или число.
Запуск приложения выводит приветствие и спрашивает число:

_Welcome to Fizz Buzz !_

_Submit a number and get an answer!_

_Number 0 - Stop process!_

Please enter a Number:_
На каждый ввод числа ( ввод чисел происходит, пока пользователь не введет число 0 ) вместо чисел, кратных трем, программа выводить слово «Fizz»,
а вместо чисел, кратных пяти — слово «Buzz».
Если число кратно и 3, и 5, то программа выводить слово «FizzBuzz»"
В остальных случаях - само число.
![image](https://github.com/tr2023GitHub/project-FizzBuzz/assets/130790937/68a32b86-e80f-490b-b876-1e01ae648b2d)

Эта задача реализована на Python 3.11.2 в виде консольной утилиты CLI с помощью Click.

Также реализованы тесты на базе Unittest и Click.testing
## __Как установить__
Репозиторий GitHub следует клонировать и перейти в директорий:
`$ git clone https://github.com/tr2023GitHub/project-FizzBuzz.git`
`$ cd project-FizzBuzz`

## __Запуск утилиты__
Откройте командную строку и выполните следующее:

`$ python fizzbuzz_code_cli.py`

### Программа начнётся с приветсвия и предложит ввести значение: ###
![image](https://github.com/tr2023GitHub/project-FizzBuzz/assets/130790937/0157a30d-0e49-43f9-9713-6a6540700e94)


`$ python fizzbuzz_code_cli.py --number=5`

### Программа выдаст сразу результат и предложит вводить следующее значение: ###
![image](https://github.com/tr2023GitHub/project-FizzBuzz/assets/130790937/40ca1f49-06b9-495f-9d1a-c84eb4d4a07f)

### При вводе символов, программ выдаст ERROR: ###
![image](https://github.com/tr2023GitHub/project-FizzBuzz/assets/130790937/d4c42845-9a8c-4a8d-8283-c56bc34b5c9b)

### При вводе 0 (ноль), программ прервется, предварительно выдав сообщение: ###
![image](https://github.com/tr2023GitHub/project-FizzBuzz/assets/130790937/51219a77-6e06-49e9-bde1-506741ef0195)

## __Вывод справки утилиты CLI__
`$ python fizzbuzz_code_cli.py –help`

![image](https://github.com/tr2023GitHub/project-FizzBuzz/assets/130790937/6431c179-19fd-4b03-8634-48f0f09e4a5c)

## __Тестирование__
Откройте командную строку и выполните следующее:

`$ pytest -v test_fizzbuzz_cli.py` 

### При успешном тестирование выводиться: ###
![image](https://github.com/tr2023GitHub/project-FizzBuzz/assets/130790937/8e7ce829-c9fd-4546-b139-0fcfee50510c)

### Автор ###
Рева Татьяна

https://github.com/tr2023GitHub











 

 
