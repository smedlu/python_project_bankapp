from typing import Any, Dict, List

from project_bankapp.processing import process_bank_search
from project_bankapp.utils import get_transactions_data
from project_bankapp.widget import get_date, mask_account_card


def main() -> None:
    """
    Основная функция программы для работы с банковскими транзакциями.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input().strip()

    if choice == "1":
        file_path = "data/operations.json"
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        file_path = "data/transactions.csv"
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        file_path = "data/transactions_excel.xlsx"
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор.")
        return

    data = get_transactions_data(file_path)
    if not data:
        print("Не удалось загрузить данные.")
        return

    # Фильтрация по статусу
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input().strip().upper()
        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            filtered_data = [t for t in data if t.get('state', '').upper() == status]
            print(f"Операции отфильтрованы по статусу \"{status}\"")
            break
        else:
            print(f"Статус операции \"{status}\" недоступен.")

    # Сортировка по дате
    sort_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
    if sort_choice == "да":
        order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        reverse = order == "по убыванию"
        filtered_data.sort(key=lambda x: x.get('date', ''), reverse=reverse)

    # Только рублевые
    ruble_choice = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
    if ruble_choice == "да":
        filtered_data = [t for t in filtered_data if t.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB']

    # Поиск по слову
    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
    if search_choice == "да":
        search_word = input("Введите слово для поиска:\n").strip()
        filtered_data = process_bank_search(filtered_data, search_word)

    # Вывод
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(filtered_data)}")

    if not filtered_data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    for transaction in filtered_data:
        date = get_date(transaction.get('date', ''))
        description = transaction.get('description', '')
        amount = transaction.get('operationAmount', {}).get('amount', 0)
        currency = transaction.get('operationAmount', {}).get('currency', {}).get('code', '')
        from_acc = transaction.get('from', '')
        to_acc = transaction.get('to', '')

        masked_from = mask_account_card(from_acc) if from_acc else ''
        masked_to = mask_account_card(to_acc) if to_acc else ''

        print(f"{date} {description}")
        if masked_from and masked_to:
            print(f"{masked_from} -> {masked_to}")
        elif masked_from:
            print(f"{masked_from}")
        elif masked_to:
            print(f"{masked_to}")
        print(f"Сумма: {amount} {currency}")
        print()


if __name__ == "__main__":
    main()
