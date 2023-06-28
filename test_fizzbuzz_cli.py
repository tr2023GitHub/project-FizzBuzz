import unittest
from unittest.mock import patch
from unittest import TestCase, main

import click
from fizzbuzz_code_cli import fizzbuzz, enter_number, run_and_stop

from click.testing import CliRunner

class FizzBuzzTestCase(unittest.TestCase):
    """
    Проверем, что fizzbuzz(int) возвращает значение int,
    если оно не кратно 3 (затем возвращает 'fizz'),
    не кратно 5 (затем возвращает 'buzz')
    не кратно обоим (затем возвращает 'fizzbuzz')
    """
    def test_usual(self):
        """
        проверям, что целое число не деляться без остатка
        на 3 или 5 или 3,5, возвращает то же самое число
        """
        for i in [1, 2, 4, 7, 8, 11]:
            self.assertEqual(fizzbuzz(i), i)

    def test_fizz(self):
        """кратное 3 возвращает Fizz"""
        for i in [3, 6, 9, 111, 999]:
            self.assertEqual(fizzbuzz(i), 'Fizz')

    def test_buzz(self):
        """кратное 5 возвращает Buzz"""
        for i in [5, 10, 20, 55, 500]:
            self.assertEqual(fizzbuzz(i), 'Buzz')

    def test_fizz_buzz(self):
        """кратное  3 и 5 возвращает FizzBuzz"""
        for i in [15, 30, 45, 90, 600]:
            self.assertEqual(fizzbuzz(i), 'FizzBuzz')

def test_simbols():
    """при вводе символо возвращается Error"""
    runner = CliRunner()
    result = runner.invoke(run_and_stop, input="jyy")
    assert result.output == 'Welcome to Fizz Buzz ! \n' \
                            'Submit a number and get an answer! Number 0 - Stop process!\n'\
                            'Please enter a Number: jyy\n' \
                            'Error! Need enter a number!\n' \
                            'Please enter a Number: \n' \
                            'Aborted!\n'


def test_input_number():
    runner = CliRunner()
    result = runner.invoke(run_and_stop, input="7")
    assert result.output == 'Welcome to Fizz Buzz ! \n' \
                            'Submit a number and get an answer! Number 0 - Stop process!\n' \
                            'Please enter a Number: 7\n' \
                            '7\n' \
                            'Please enter a Number: \n' \
                            'Aborted!\n'


def test_input_five():
    """ проверка  на кратность  5 возвращает Buzz"""
    runner = CliRunner()
    result = runner.invoke(run_and_stop, input="5")
    assert result.output == 'Welcome to Fizz Buzz ! \n' \
                            'Submit a number and get an answer! Number 0 - Stop process!\n' \
                            'Please enter a Number: 5\n' \
                            'Buzz\n' \
                            'Please enter a Number: \n' \
                            'Aborted!\n'


def test_input_three():
    """ проверка  на кратность  3 возвращает Fizz"""
    runner = CliRunner()
    result = runner.invoke(run_and_stop, input="3")
    assert result.output == 'Welcome to Fizz Buzz ! \n' \
                            'Submit a number and get an answer! Number 0 - Stop process!\n' \
                            'Please enter a Number: 3\n' \
                            'Fizz\n' \
                            'Please enter a Number: \n' \
                            'Aborted!\n'


def test_input_fifteen():
    """ проверка  на кратность  3 и 5 возвращает FizzBuzz"""
    runner = CliRunner()
    result = runner.invoke(run_and_stop, input="15")
    assert result.output == 'Welcome to Fizz Buzz ! \n' \
                            'Submit a number and get an answer! Number 0 - Stop process!\n' \
                            'Please enter a Number: 15\n' \
                            'FizzBuzz\n' \
                            'Please enter a Number: \n' \
                            'Aborted!\n'


def test_input_zero():
    """ проверка  на 0 возвращает Stop"""
    runner = CliRunner()
    result = runner.invoke(run_and_stop, input="0")
    assert result.output == 'Welcome to Fizz Buzz ! \n' \
                            'Submit a number and get an answer! Number 0 - Stop process!\n' \
                            'Please enter a Number: 0\n' \
                            'Stop, as Number:0\n'


if __name__ == '__main__':
    main()
