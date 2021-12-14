print('Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# программа находит наибольшее по сумме цифр.
# Это число и сумма его цифр выводятся на экран.

numbers = int(input('Введите количество чисел: '))

summa_large = 0

for i in range(1, numbers + 1):
  number = int(input('Введите число: '))
  factor = 10
  divider = 1
  digit = 10
  summa = 0
  while digit != 0:
    digit = number % factor // divider
    summa += digit
    factor *= 10
    divider *= 10
  if summa > summa_large:
    summa_large = summa
    number_large = number

print('Из введённых чисел наибольшее по сумме цифр — '
      + str(number_large) + '. Сумма цифр этого числа равняется '
      + str(summa_large))
