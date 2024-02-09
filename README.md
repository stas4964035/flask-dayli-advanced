# Простой блог на Flask, PostgreSQL

### Функционал:
- Админка. CRUD пользователей и постов.
- Функционал обработки ошибок.
- Посты. Пользователи могут создават, редактировать и удалять посты. 
  Просмотривать посты других пользователей. В постах можно оставлять 
  комментарии и лайки.
- Пользователи. Реализована регистрация, восстановление пароля, 
  редактирование данных пользователя.
- Механизм миграции.


## !Запуск: 
Для корректной работы отправки писем необходимо добавить данные гугл аккаунта
(для отправки писем с сервера ) в файле dayly/config.py 
\
``` MAIL_USERNAME = "yourmail@gmail.com" ```
\
``` MAIL_PASSWORD = "your password" # нужно создать пароль приложения по ссылке https://myaccount.google.com/apppasswords и использовать сгенерированный пароль ``` 
Файлы репозитория подготовлены для контенеризации
```
  docker compose up --build
```
\
В случае успешного запуска сервер об этом сообщит
```
server-1  |  * Running on all addresses (0.0.0.0)
server-1  |  * Running on http://127.0.0.1:5000
server-1  |  * Running on http://172.18.0.3:5000
server-1  | Press CTRL+C to quit
```

Блог будет доступен по ссылке
```
http://localhost:5000
```
