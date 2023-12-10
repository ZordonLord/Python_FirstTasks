# phonebook = {"дядя Ваня": {'pnones': [1321231,121212], 
#                            'email': "123@mail.ru", 'birthday': '11.10.2000'},
#             "дядя Вася": {'pnones': [55555]  }
#             }

# print(phonebook["дядя Ваня"]['pnones'])

from random import *
import json

phonebook = {}

# Добавление записи
def addInfo():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    phonebook[last_name] = {
        "Имя": first_name,
        "Отчество": middle_name,
        "Номер телефона": phone_number
    }
    print("Запись успешно добавлена.")

#  Экспорт
def save():
    with open("phonebook.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))
    print("Наш Справочник телефонов успешно сохранен в файле phonebook.json")


#  Импорт
def load():
    with open("phonebook.json", "r", encoding="utf-8") as fh:
        phonebook = json.load(fh)
    print("Наша Справочник телефонов успешно загружен")
    return phonebook

def print_info():
    for k, w in phonebook.items():
        print(k, w)


while True:
    command = input("Введите команду ")
    if command == "/start":
        print("Справочник телефонов")
    elif command == "/stop":
        save()
        print("Бот остановил свою работу. Заходите ещё, будем рады!")
        break
    elif command == "/all":
        print("Ввот текущий список контактов")
        print_info()
    elif command == "/add" :
        addInfo()
        print("Контакт был успешно добавлен в коллекцию")

    elif command == "/help":
        print("Здесь какой-то мануал")
    elif command == "/delete":
        f= input("Введите название фильма, который надо удалить ")
        # if f in films:
        #     films.remove(f)
        #     print("Фильм успешно удалён")
        # else:
        #     print("Такого фильма нет в фильмотеке ")
        try:
            phonebook.remove(f)
            print("Фильм успешно удалён")
        except:
            print("Такого фильма нет в фильмотеке ")
    elif command == "/random":
        print("Слепой жребий показал вам фильм - " + choice(phonebook))
    elif command == "/save" :
        save()
    elif command == "/load":
        phonebook=load()

    else:
        print("Неопознанная команда. Просьба изучить мануал через /help")