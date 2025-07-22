# Домашнее задание к лекции «Asyncio»

В этом задании мы будем выгружать из API персонажей Start Wars и загружать в базу данных.<br>
Документация по API находится здесь: [SWAPI](https://swapi.tech/). <br>
Пример запроса: `https://www.swapi.tech/api/people/1/` <br>
В результате запроса получаем персонажа с ID 1:
```
{
  "message": "ok",
  "result": {
    "properties": {
      "created": "2025-07-22T16:28:46.488Z",
      "edited": "2025-07-22T16:28:46.488Z",
      "name": "Luke Skywalker",
      "gender": "male",
      "skin_color": "fair",
      "hair_color": "blond",
      "height": "172",
      "eye_color": "blue",
      "mass": "77",
      "homeworld": "https://www.swapi.tech/api/planets/1",
      "birth_year": "19BBY",
      "url": "https://www.swapi.tech/api/people/1"
    },
    "_id": "5f63a36eee9fd7000499be42",
    "description": "A person within the Star Wars universe",
    "uid": "1",
    "__v": 2
  },
  "apiVersion": "1.0",
  "timestamp": "2025-07-22T19:39:54.218Z",
  "support": {
...
  },
  "social": {
...
  }
}
```
Необходимо выгрузить cледующие поля:<br>
**id** - ID персонажа <br>
**birth_year** <br>
**eye_color** <br>
**gender** <br>
**hair_color** <br>
**homeworld** <br>
**mass** <br>
**name** <br>
**skin_color** <br>
Данные по каждому персонажу необходимо загрузить в любую базу данных. <br>
Выгрузка из апи и загрузка в базу должна происходить асинхронно. <br>

Результатом работы будет: <br>
1) скрипт миграции базы данных <br>
2) скрипт загрузки данных из API в базу <br>

В базу должны быть загружены все персонажи
