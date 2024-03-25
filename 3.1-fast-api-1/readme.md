Написать и докеризировать сервис на fastapi объявлений купли/продажи

У объявлений должна быть следующие поля:

заголовок

описание

цена

автор

Должны быть реализованы следующе методы:

Создание: POST /advertisement 

Обновление: PATCH /advertisement/{advertisement_id}

Удаление: DELETE /advertisement/{advertisement_id}

Получение по id GET  /advertisement/{advertisement_id}

Поиск по полям GET /advertisement?{query_string}

