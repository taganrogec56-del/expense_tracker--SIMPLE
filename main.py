menu_dict = {'1': 'Добавить расход',
             '2': 'Показать все расходы',
             '3': 'Показать общую сумму расходов',
             '4': 'Показать расходы по категории',
             '5': 'Показать статистику по категориям',
             '0': 'Выход',
             }

menu_text = '\n'.join([f'{num_task}. {text_task}' for num_task, text_task in menu_dict.items()])


def show_menu():
    print('=== Трекер Расходов ===')
    print()
    print(menu_text)


while True:
    show_menu()
    task = input('<_').strip()
    print()
    if task not in menu_dict:
        print('Неверное действие. Такого пункта меню нет. 😢')
        continue
    if task == '0':
        print('До свидания 😀')
        break

    print(f'Вы выбрали: {menu_dict[task]}')
