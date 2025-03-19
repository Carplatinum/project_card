# <Card_Bank>

## Описание

Проект предоставляет функции для маскировки номеров банковских карт и счетов.
### Модуль `generators`
Модуль `generators` содержит функции для эффективной обработки данных транзакций с помощью генераторов.
Модуль позволяет быстро и удобно находить нужную информацию о транзакциях и проводить анализ данных. 
#### Функция `filter_by_currency`
Фильтрует транзакции по заданной валюте и возвращает итератор: 
transactions = [...]  # Список транзакций  
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
print(next(usd_transactions))
#### Функция-генератор `transaction_descriptions`
Генерирует описания каждой транзакции по очереди:  
transactions = [...] # Список транзакций  
descriptions = transaction_descriptions(transactions)
for _ in range(5):
print(next(descriptions))  
#### Генератор `card_number_generator`
Генерирует номера банковских карт в заданном диапазоне:  
for card_number in card_number_generator(1, 5):  
print(card_number)
### Модуль `decorators`
Модуль `decorators` содержит функции-декораторы для логирования и анализа работы функций.
#### Декоратор `log`
Декоратор `log` позволяет автоматически регистрировать детали выполнения функций, такие как имя функции, результаты или возникшие ошибки. Он может логировать данные как в файл, так и в консоль.
@log(имя_файла="mylog.txt")  
def my_function(x, y):  
return x + y  

my_function(1, 2)

Декоратор обеспечивает гибкий контроль над логированием и может быть использован для анализа поведения программы в процессе ее выполнения.
## Установка
1.  Клонируйте репозиторий:  
    git clone https://github.com/Carplatinum/project_card.git
2.  Перейдите в директорию проекта:  
    cd C:\Users\ANTAQ\Desktop\PythonProjects\PyCharmProjects\project_card>
3.  Установите зависимости:  
    pip install -r requirements.txt
# Использование 
Проект используется для маскировки номеров банковских карт и счетов.

## Тестирование
В проекте реализовано полное тестирование всех функций с использованием фреймворка `pytest`.

### Запуск тестов
Тесты можно запустить командой:  
pytest --cov=src --cov-report=term --cov-report=html

### Отчет о покрытии тестами
Отчет о покрытии тестами доступен в формате HTML в папке `htmlcov`.

# Лицензия
Этот проект распространяется под лицензией [MIT License](LICENSE)

## Авторы 
[ANTAQ](https://github.com/Carplatinum)