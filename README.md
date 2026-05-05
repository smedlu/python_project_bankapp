# BankApp

## Описание проекта
**BankApp** — это Python-приложение, предназначенное для безопасной обработки и отображения банковских транзакций. Проект помогает автоматизировать повседневные задачи по управлению финансовыми данными, обеспечивая конфиденциальность пользователей.

## Функциональность
- **Маскировка данных**: скрытие номеров карт (`XXXX XX** **** XXXX`) и счетов (`**XXXX`).
- **Фильтрация**: поиск транзакций по статусу (например, `EXECUTED`).
- **Сортировка**: упорядочивание операций по дате (от новых к старым).
- **Чтение данных**: поддержка загрузки транзакций из JSON, CSV и Excel файлов.

## Установка и настройка

### 1. Системные требования
- Python 3.12 или выше.
- [Poetry](https://python-poetry.org/) 2.0+ для управления зависимостями.

### 2. Клонирование и инсталляция
Клонируйте репозиторий и установите все пакеты (включая зависимости для тестирования):
```bash
git clone [https://github.com/smedlu/python_project_bankapp.git](https://github.com/smedlu/python_project_bankapp.git)
cd project_BankAPP
poetry install
## Использование

Проект предоставляет набор инструментов (виджетов и масок), которые можно использовать в своем коде:

```python
from project_bankapp.widget import mask_account_card, get_date

# Маскировка карты
print(mask_account_card("Visa Platinum 7000792289606361")) 
# Вывод: Visa Platinum 7000 79** **** 6361

# Преобразование даты
print(get_date("2024-03-11T02:26:18.671407")) 
# Вывод: 11.03.2024
# Запуск тестов
poetry run pytest

# Проверка покрытия
poetry run pytest --cov=src --cov-report term-missing
## Модуль generators

Модуль содержит функции-генераторы для эффективной фильтрации и обработки данных транзакций.

### Примеры использования

1. **Фильтрация по валюте:**
```python
usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)
descriptions = transaction_descriptions(transactions)
for desc in descriptions:
    print(desc)
for card_number in card_number_generator(1, 5):
    print(card_number) # Выведет: 0000 0000 0000 0001 и т.д.
### Модуль generators
Содержит функции для обработки транзакций с помощью генераторов:
- `filter_by_currency`: фильтрует данные по валюте.
- `transaction_descriptions`: извлекает описания операций.
- `card_number_generator`: генерирует номера карт в формате XXXX XXXX XXXX XXXX.