"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
slovo = str(input('Введите первое слово: '))
slovo2 = str(input('Введите второе слово: '))
def main (slovo, slovo2):
    
    if not isinstance(slovo, str) or not isinstance(slovo2, str):
      return print ('0')
    if slovo==slovo2:
      return print ('1')
    else:
      if len(slovo)>len(slovo2):
          return print ('2')
      elif slovo != (slovo2 == 'learn'):
         return print ('3')
 
result = main(slovo, slovo2)
print(result)


if __name__ == '__main__':
    main(slovo,slovo2)
    