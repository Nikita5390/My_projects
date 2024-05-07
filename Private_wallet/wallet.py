import json
import datetime
from typing import List, Set

WALLET_DATA = []


def write_json(data: List, filename: str) -> None:
    """Функция записи JSON файла"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def read_json(filename: str) -> List:
    """Функция чтения JSON файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


class ServiceFun:

    def add_notes() -> None:
        """Функция добавления записи"""
        cost = int(input("Введите сумму ('-' - расход, '+' - доход): "))
        if cost >= 0:
            category = 'Income'
        else:
            category = 'Expenses'
        description = input("Описание: ")
        new_data = {
            "date": datetime.date.today().isoformat(),
            "category": category,
            "cost": cost,
            "description": description
        }
        data = read_json('wallet.json')
        data.append(new_data)
        write_json(data, 'wallet.json')
        return print("Записано успешно!")

    def change_notes() -> None:
        """Функция изменения записи"""
        ServiceFun.del_data()
        cost = int(input("Введите сумму ('-' - расход, '+' - доход): "))
        if cost >= 0:
            category = 'Income'
        else:
            category = 'Expenses'
        description = input("Описание: ")
        description = input("Новое описание покупки: ")
        change_data = {
            "date": datetime.date.today().isoformat(),
            "category": category,
            "cost": cost,
            "description": description
        }
        data = read_json('wallet.json')
        data.append(change_data)
        write_json(data, 'wallet.json')
        return print("Записано успешно!")

    def del_data() -> None:
        """Функция удаления записи"""
        data = read_json('wallet.json')
        choice_data = input("Введите описание записи: ")
        count = 0
        for item in data:
            if item['description'] == choice_data:
                data.pop(count)
            else:
                count += 1
        write_json(data, 'wallet.json')
        print('Deleted!')

    def find_data() -> Set:
        """Функция поиска записи"""
        data = read_json('wallet.json')
        choice_data = input("Введите категорию (Income/Expenses)\n"
                            "дату в формате YYYY-MM-DD\n"
                            "или сумму: ")
        count = 0
        for item in data:
            if item['category'] == choice_data or str(item['date']) == choice_data or str(item['cost']) == choice_data:
                print(data[count])
            count += 1


class CountFun:

    def balance() -> str:
        """Функция подсчета баланса"""
        data = read_json('wallet.json')
        count = 0
        for item in data:
            count += item['cost']
        return print(f'Баланс = {count}')

    def income() -> str:
        """Функция подсчета дохода"""
        data = read_json('wallet.json')
        count = 0
        for item in data:
            if item['cost'] >= 0:
                count += item['cost']
        return print(f'Доход = {count}')

    def expenses() -> str:
        """Функция подсчета расхода"""
        data = read_json('wallet.json')
        count = 0
        for item in data:
            if item['cost'] < 0:
                count += item['cost']
        return print(f'Расход = {count}')


class SHOP:
    def __init__(self, choice):
        self.choice = choice

    def menu() -> str:
        """Функция меню"""
        return (
                '<>' * 80 + '\n'
                            '1 - посмотреть баланс\n' +
                '2 - добавить запись\n' +
                '3 - редактировать запись\n' +
                '4 - удалить запись\n' +
                '5 - поиск по записям (Категория, дата, сумма)\n' +
                '6 - общий Доход\n' +
                '7 - общий Расход\n' +
                '8 - завершить.'
        )

    def make_choice(choice: int):
        """Функция выбора необходимого действия"""
        if choice == 1:
            result = CountFun.balance()
        elif choice == 2:
            result = ServiceFun.add_notes()
        elif choice == 3:
            result = ServiceFun.change_notes()
        elif choice == 4:
            result = ServiceFun.del_data()
        elif choice == 5:
            find = ServiceFun.find_data()
            if find == None:
                result = "Записей не найдено"
            else:
                result = find
        elif choice == 6:
            result = CountFun.income()
        elif choice == 7:
            result = CountFun.expenses()
        elif choice == 8:
            result = "Спасибо!"
        return result


def run() -> None:
    """Функция запуска приложения"""
    write_json(WALLET_DATA, 'wallet.json')
    choice = None
    while choice != 8:
        print(SHOP.menu())
        try:
            choice = int(input('Введите пункт меню: '))
            message = SHOP.make_choice(choice)
            print(message)
        except ValueError:
            print("Введите целое число от 1 до 8!")


run()
