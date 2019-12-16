# База судебной практики (REST API)
API к консолидированной legacy БД (Firebird)

## Скриншоты
UI (php, bootstrap)
![screenshot here](/screenshots/screenshot_ui_sm.png)
Map (php, leaflet.js)
![screenshot here](/screenshots/screenshot_map_sm.png)

## Установка (Flask в docker контейнере)

### Сборка docker image

```sh
$ docker build -t flask-fbird .
```

### Запуск контейнера с volume

```sh
$ docker run -d --name flask-bsp32 -p 2088:80 -v $(pwd)/app:/app flask-fbird
```

Пример: `http://server_name:2088/bsp32/api/v1/32RS0000/ucases`