from decimal import Decimal, InvalidOperation

menu_dict = {'1': 'Добавить расход',
             '2': 'Показать все расходы',
             '3': 'Показать общую сумму расходов',
             '4': 'Показать расходы по категории',
             '5': 'Показать статистику по категориям',
             '0': 'Выход',
             }

menu_text = '\n'.join([f'{num_task}. {text_task}' for num_task, text_task in menu_dict.items()])
expenses = []


def show_menu():
    print('=== Трекер Расходов ===')
    print()
    print(menu_text)


def add_expense():
    title = input('Введите название: ').strip()

    while True:
        amount = input('Введите сумму: ').strip()
        try:
            amount = Decimal(amount).quantize(Decimal('0.01'))
            if amount <= 0:
                print('Сумма не может быть меньше или равной 0 ☝️')
                continue
            break
        except InvalidOperation:
            print('Неверное значение 😢')

    category = input('Введите категорию: ').strip()

    expenses.append({
        "title": title,
        "amount": amount,
        "category": category
    })
    print('Расход добавлен 👍')


def show_expenses():
    if not expenses:
        print('Расходов пока нет 😎')
        print()
        return
    print('=== Все расходы ===')
    for counter, expense in enumerate(expenses, 1):
        print(f"{counter}. {expense['title']} - {expense['amount']:.2f} руб. - {expense['category']}")


def show_total():
    if not expenses:
        print('Расходов пока нет 😎')
        print()
        return
    total_expenses = sum((expense['amount'] for expense in expenses))
    print(f'Общая сумма расходов: {total_expenses:.2f} руб.')


def show_by_category():
    category = input('Категория: ').strip().lower()
    found_category = False
    total_by_category = 0

    for expense in expenses:
        if expense['category'].lower() == category:
            total_by_category += expense['amount']

            if not found_category:
                found_category = True
                print(f'=== Категория: {category.capitalize()} ===')
                print()

            print(f"{expense['title']} - {expense['amount']:.2f} руб.")
    if found_category:
        print(f'Всего: {total_by_category:.2f} руб.')
    else:
        print()
        print(f'Расходов в категории "{category.capitalize()}" не найдено.')


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
    elif task == '1':
        print(f'Вы выбрали: {menu_dict[task]}')
        add_expense()
    elif task == '2':
        print(f'Вы выбрали: {menu_dict[task]}')
        show_expenses()
    elif task == '3':
        print(f'Вы выбрали: {menu_dict[task]}')
        show_total()
    elif task == '4':
        print(f'Вы выбрали: {menu_dict[task]}')
        show_by_category()
