Репозиторий интернет-магазина на Django 3.

Установка:

1. Открыть терминал или консоль и перейти в нужную Вам директорию
2. Прописать `git clone https://github.com/mukovozovb/shop.git`
3. Прописать следующие команды:
- `python3 -m venv ДиректорияВиртуальногоОкружения`
- `source ДиректорияВиртуальногоОкружения/bin/activate`
-  Перейти в директорию **shop**
- `pip install -r requirements.txt`
- `python manage.py migrate`
4. Запустить сервер - `python manage.py runserver`
5. Не забудьте создать директорию **media**, куда будут сохраняться изображения для товара