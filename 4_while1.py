"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
    a = input ('Как дела? ')
    if a != "Хорошо":
      return hello_user ()
    elif a == "хорошо":
      print ("Молодец, съешь пирожок! ")

    
if __name__ == "__main__":
    hello_user()
