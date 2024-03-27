# Домашнее задание к лекции «Создание REST API на FastApi» часть 1

Инструкцию по сдаче домашнего задания вы найдете на главной странице репозитория.

# Задание 
Вам нужно написать и декодезировать сервис на fastapi объявлений купли/продажи.

У объявлений должна быть следующие поля:

-заголовок

-описание

-цена

-автор

Должны быть реализованы следующе методы:

Создание: POST /advertisement 

Обновление: PATCH /advertisement/{advertisement_id}

Удаление: DELETE /advertisement/{advertisement_id}

Получение по id GET  /advertisement/{advertisement_id}

Поиск по полям GET /advertisement?{query_string}

