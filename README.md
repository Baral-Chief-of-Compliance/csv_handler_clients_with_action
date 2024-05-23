## 1 Создание виртуального окружения
<code>py -m venv env</code>
## 2 Активация виртуального окуржения
<code>env\Scripts\activate.bat</code>
## 3 Установка зависимостей
<code>pip install -r requirements.txt</code>
## 4 Указание расположение входного и выходного файла
необходимо в .env в  IN_FILE_PATH указать путь на файл с входными данными. в OUT_FILE_PATH на файл с выходными данными
## 5 использование функции для Агрегации данных по клиентам, подсчета числа действий каждого клиента.
для этого необходимо в файле main.py вызвать у ch метод count_client_action(client_id:int) на вход указать client_id - это id клиента в таблице.
Если не обходимо вывести в консоль результат можно просто обернуть в print, но если необходимо вывести результат в выходной файлик,
то можно сделать так ch.save_processed_data(ch.count_client_action(1), os.getenv('OUT_FILE_PATH))
## 6 использование функции Фильтрации данных по определенным критериям (например, только действия оформления заказа).
для этого необходимо в файле main.py вызвать у ch.filter_crireria(criteria_name: str, value)
criteria_name - название колонки в таблице
value - значение по которому не обходимо отфильтрровать
Вывод резульатат:
- print(ch.filter_crireria('action', 'purchase))
- ch.save_processed_data(ch.filter_crireria('action', 'purchase), os.getenv('OUT_FILE_PATH))
## 7 использование функции analyze_client_behavior
ch.analyze_client_behavior()
Вывод резульатат:
- print(ch.analyze_client_behavior())
- ch.save_processed_data(ch.analyze_client_behavior())

## 8 Запуск
<code>py main.py</code>

