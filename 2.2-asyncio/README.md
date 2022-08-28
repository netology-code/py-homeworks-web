# Домашнее задание к лекции «Asyncio»

В этом задании мы будем выгружать из API персонажей Start Wars и загружать в базу данных.<br>
Документация по API находится здесь: [SWAPI](https://swapi.dev/documentation#people). <br>
Пример запроса: `https://swapi.dev/api/people/1/` <br>
В результате запроса получаем персонажа с ID 1:
```
{
    "birth_year": "19 BBY",
    "eye_color": "Blue",
    "films": [
        "https://swapi.dev/api/films/1/",
        ...
    ],
    "gender": "Male",
    "hair_color": "Blond",
    "height": "172",
    "homeworld": "https://swapi.dev/api/planets/1/",
    "mass": "77",
    "name": "Luke Skywalker",
    "skin_color": "Fair",
    "created": "2014-12-09T13:50:51.644000Z",
    "edited": "2014-12-10T13:52:43.172000Z",
    "species": [
        "https://swapi.dev/api/species/1/"
    ],
    "starships": [
        "https://swapi.dev/api/starships/12/",
        ...
    ],
    "url": "https://swapi.dev/api/people/1/",
    "vehicles": [
        "https://swapi.dev/api/vehicles/14/"
        ...
    ]
}
```
Необходимо выгрузить cледующие поля:<br>
**id** - ID персонажа <br>
**birth_year** <br>
**eye_color** <br>
**films** - строка с названиями фильмов через запятую <br>
**gender** <br>
**hair_color** <br>
**height** <br>
**homeworld** <br>
**mass** <br>
**name** <br>
**skin_color** <br>
**species** - строка с названиями типов через запятую <br>
**starships** - строка с названиями кораблей через запятую <br>
**vehicles** - строка с названиями транспорта через запятую <br>
Данные по каждому персонажу необходимо загрузить в любую базу данных. <br>
Выгрузка из апи и загрузка в базу должна происходить асинхронно. <br>

Результатом работы будет: <br>
1) скрипт миграции базы данных <br>
2) скрипт загрузки данных из API в базу <br>

В базу должны быть загружены все персонажи
