"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def users_age(age):
    if 1 <= age <= 3:
        return "Тебе нет еще и 4-х лет, как ты можешь что-либо написать сюда?"
    elif 4 <= age <= 6:
        return "Поздравляю ты еще не научился писать, ты в детсаду"
    elif 7 <= age <=18:
        return "Настало время стаданий, ведь ты в ШКОЛЕ"
    elif 19 <= age <= 27:
        return "Возможно ты закончишь институт аспирантом, а может и нет..."
    elif 28 <= age <= 60:
        return "Возможно ты доживешь до пенсии работая на заводе"
    elif 61 <= age <= 80:
        return "Поздровляю ты слишком стар, чтобы работать, насладись одиночеством на заслуженной пенсии"
    elif 81 <= age < 120:
        return "Скорее всего ты труп"
         
    return "Я разговариваю с призраком?"


def main():
    age = int(input('Введите ваш возраст, гадальный шар определит вашу судьбу: '))

    result = users_age(age)
    print(result)


if __name__ == '__main__':
    main()