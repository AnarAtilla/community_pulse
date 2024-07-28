# Community Pulse

## Описание
Community Pulse - это веб-приложение, разработанное на Python с использованием Flask. Оно предназначено для управления и анализа данных сообщества.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone git@github.com:AnarAtilla/community_pulse.git
    cd community_pulse
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Инициализируйте базу данных:
    ```bash
    flask db_init
    ```

## Запуск

1. Запустите приложение:
    ```bash
    flask run
    ```

2. Приложение будет доступно по адресу `http://127.0.0.1:5000`.

## Структура проекта

- `app/` - Основной модуль приложения
  - `__init__.py` - Инициализация приложения и настройка
  - `models.py` - Определение моделей базы данных
  - `routers/` - Маршруты и обработчики запросов
    - `responses.py` - Обработчики для маршрутов `/api`
- `migrations/` - Миграции базы данных
- `run.py` - Точка входа в приложение

## Используемые технологии

- Python
- Flask
- Flask-Migrate
- SQLAlchemy
- SQLite (или другая база данных по вашему выбору)

## Работа с Postman

### Получение всех данных с базы

1. Откройте Postman.
2. Создайте новый запрос и выберите метод GET.
3. Введите URL:
    ```plaintext
    http://127.0.0.1:5000/api/responses
    ```
4. Нажмите кнопку "Send".

### Добавление вопроса

1. Откройте Postman.
2. Создайте новый запрос и выберите метод POST.
3. Введите URL:
    ```plaintext
    http://127.0.0.1:5000/api/questions
    ```
4. Перейдите на вкладку "Body", выберите raw и JSON.
5. Введите данные для создания вопроса:
    ```json
    {
        "body": "Ваш вопрос здесь",
        "title": "Заголовок вопроса"
    }
    ```
6. Нажмите кнопку "Send".

### Изменение вопроса

1. Откройте Postman.
2. Создайте новый запрос и выберите метод PUT.
3. Введите URL:
    ```plaintext
    http://127.0.0.1:5000/api/questions/<id>
    ```
    Замените `<id>` на ID вопроса, который вы хотите изменить.
4. Перейдите на вкладку "Body", выберите raw и JSON.
5. Введите данные для обновления вопроса:
    ```json
    {
        "body": "Обновленный вопрос",
        "title": "Обновленный заголовок"
    }
    ```
6. Нажмите кнопку "Send".

### Ответ на вопрос

1. Откройте Postman.
2. Создайте новый запрос и выберите метод POST.
3. Введите URL:
    ```plaintext
    http://127.0.0.1:5000/api/responses
    ```
4. Перейдите на вкладку "Body", выберите raw и JSON.
5. Введите данные для создания ответа:
    ```json
    {
        "question_id": "<id>",
        "user_name": "Ваше имя",
        "text": "Ваш ответ"
    }
    ```
    Замените `<id>` на ID вопроса, на который вы отвечаете.
6. Нажмите кнопку "Send".

### Обновление данных ответа

1. Откройте Postman.
2. Создайте новый запрос и выберите метод PUT.
3. Введите URL:
    ```plaintext
    http://127.0.0.1:5000/api/responses/<id>
    ```
    Замените `<id>` на ID ответа, который вы хотите обновить.
4. Перейдите на вкладку "Body", выберите raw и JSON.
5. Введите данные для обновления ответа:
    ```json
    {
        "text": "Обновленный текст ответа"
    }
    ```
6. Нажмите кнопку "Send".

Эти инструкции помогут вам взаимодействовать с API приложения Community Pulse через Postman для выполнения основных операций с данными.
