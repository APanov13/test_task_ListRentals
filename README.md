# test_task_ListRentals
### Тестовое задание. Сервис по работе с балансами

> Пока нет навыков работы с асинхронным пайтоном и его фреймворками,  
> написал сервис на DRF с использованием Django ORM,   
> по этой причине не использую SQLAlcemistry.  

### Порядок запуска проекта.

Клонировать репозиторий  
`git clone git@github.com:APanov13/test_task_ListRentals.git`

создать и запустить контейнеры с проектом и с БД  
`docker-compose up -d --build`

выполнить миграции БД  
`docker-compose exec web python manage.py makemigrations --noinput`  
`docker-compose exec web python manage.py migrate --noinput`

Проект запускается по адресу: `http://127.0.0.1:8000`  

Но т.к. настроена аутентификация по JWT-токену, то сперва надо зарегистрировать пользователя, отправив POST-запрос с username и password по адресу:   `http://127.0.0.1:8000/auth/users/ `
например:  
```json
{
"username": "simple-user", 
"password": "simple-password"
}
```

затем необходимо получить токен, отправив POST-запрос на адрес: `http://127.0.0.1:8000/auth/jwt/create/` передав в запросе username и password зарегистрированного пользователя.

Токен вернётся в поле `"access"`, этот токен необходимо передавть в заголовке каждого запроса перед токеном необходимо поставить ключевое слово Bearer и пробел, например:
`Bearer silple-random-token`

## Примеры запросов и ответов API
### Добавление пользователя
POST-запрос на `http://127.0.0.1:8000/v1/account/` с указанием имени пользователя, баланс нового пользователя создается автоматически и равен нулю.
##### Ответ API:
```json
{
    "name": "test_name",
    "balance": "0.00",
    "transactions": []
}
```

### Добавление транзакции
POST-запрос на `http://127.0.0.1:8000/v1/transaction/` с указанием ID пользователя, типа транзакции (DEPOSIT или WITHDRAW) и суммы транзакции. При указании транзакции типа "DEPOSIT", на счет указанного пользователя будетут начисленны указаные средства. При указании транзакции типа "WITHDRAW", со счета указанного пользователя будут списанны указанные средства. При недостаточном количестве средств на счете пользователя операция будет прервана, транзакция не пройдет, будет выведена ошибка о недостаточном балансе.
##### Ответ API:
```json
{
    "user_id": 1,
    "method": "DEPOSIT",
    "amound": "1000.00",
    "timestamp": "2023-03-12T22:50:37.339145Z"
}
```

### Получение информации о конкретной транзакции
GEТ-запрос на `http://127.0.0.1:8000/v1/transaction/<int:id_transaction>` Будет получена детальная информация о транзакции: Дата и время, пользователь, тип и сумма.
##### Ответ API:
```json
{
    "user_id": 1,
    "method": "DEPOSIT",
    "amound": "1000.00",
    "timestamp": "2023-03-12T22:50:37.339145Z"
}
```
### Получение информации о балансе
GET-запрос на `http://127.0.0.1:8000/v1/account/<int:id_user>` Будет отображена информация о конкретном пользователе с указанием его текущего баланса и перечислением всех его транзакций
##### Ответ API:
```json
{
    "name": "test_name",
    "balance": "1000.00",
    "transactions": [
        "№ 1, 2023-03-12 22:50:37.339145+00:00, DEPOSIT, 1000.00"
    ]
}
```
