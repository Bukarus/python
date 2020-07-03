# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом

# TODO В этом задании лучше использовать словарь, в котором номер месяца − ключ,
#  а количество дней в нём − значение. Это позволит уменьшить объём кода,
#  а количество проверок до одной, с использованием оператора in.
user_input = input("Введите, пожалуйста, номер месяца: ")
while (user_input != 'exit'):
    month = int(user_input)
    print('Вы ввели', month)

    if month == 1:
        print('В этом месяце', 31, 'день!')
    elif month == 2:
        print('В этом месяце', 28, 'день!')
    elif month == 3:
        print('В этом месяце', 31, 'день!')
    elif month == 4:
        print('В этом месяце', 30, 'день!')
    elif month == 5:
        print('В этом месяце', 31, 'день!')
    elif month == 6:
        print('В этом месяце', 30, 'день!')
    elif month == 7:
        print('В этом месяце', 31, 'день!')
    elif month == 8:
        print('В этом месяце', 31, 'день!')
    elif month == 9:
        print('В этом месяце', 30, 'день!')
    elif month == 10:
        print('В этом месяце', 31, 'день!')
    elif month == 11:
        print('В этом месяце', 30, 'день!')
    elif month == 12:
        print('В этом месяце', 31, 'день!')
    else:
        print('Такого месяца не существует!')
    user_input = input("Введите, пожалуйста, номер месяца: ")
