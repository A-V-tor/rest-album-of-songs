# Соберите с помощью Django Rest Framework каталог исполнителей и их альбомов с песнями такой структуры:

- Исполнитель
  - Название
- Альбом
  - Исполнитель
  - Год выпуска
- Песня
  - Название
  - Порядковый номер в альбоме

Одна и та же песня может быть включена в несколько альбомов, но под разными порядковыми номерами.

<h1 align="center">Развертывание проекта</h1>

<h2>Скачать проект</h2>

```
  git clone https://github.com/A-V-tor/rest-album-of-songs.git
```

```
  cd rest-album-of-songs/rest_album_of_songs
```

Сборка образа
```
  docker-compose build
```

Запуск
```
  docker-compose up
```

## URL
  `http://0.0.0.0:8000/admin/` - Login: `admin` Password: `admin`  </br></br>
  `http://0.0.0.0:8000/api/all-songs/` - все песни </br>
  `http://0.0.0.0:8000/api/all-singer/` - все исполнители </br>
  `http://0.0.0.0:8000/api/song/<int:id>/` - конкретная песня </br>
  `http://0.0.0.0:8000/api/album/<int:id>/` - конкретный альбом </br></br>
  
  `http://0.0.0.0:8000/api/album-song/<int:id>/` - конкретная песня с отображением альбомов в которых она присутствует </br></br>
  <img src="https://github.com/A-V-tor/rest-album-of-songs/blob/main/example.png">

  `http://0.0.0.0:8000/api/schema/swagger-ui/` - swagger документация
