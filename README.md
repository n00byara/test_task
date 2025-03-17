Для сборки проекта нужно ввести команду "docker-compose build"
Для запуска "docker-compose up". Для запуска в фоне "docker-compose up -d"

Конфигурационный файл .env должен находится в папке config.

Файл должен содержать в себе следующие поля(значения по усмотрению):
 - DEBUG=true
 - HOST=0.0.0.0 
 - PORT=3000

 - POSTGRES_USER=test_user 
 - POSTGRES_DB=test_db
 - POSTGRES_PASSWORD=password
 - POSTGRES_HOST=database (database путь контейнера для postgresql)
 - POSTGRES_PORT=5432

Для просмотра и сохранения информации о пользователе в бд нужно перейти по адресу http://localhost:3000/get_user_info
методом POST и отправить email и пароль ползователя ({ "email": "", "password": "" }). Сначала перейти по указаному пути, иначе данные не будут сохранятся в бд.

Ответ придет в виде json обьекта

![пример получения данных о пользователе](https://github.com/user-attachments/assets/85a578eb-404c-49cb-b915-f9adb818db19)
![данные сохраняются в бд](https://github.com/user-attachments/assets/c282cfd7-72d7-4f77-aa91-4b300e730cc7)

Для получения информации о избранных товарах нужно отправть такой же запрос, по адресу http://localhost:3000/get_grid_list
![информация о товарах из избранного](https://github.com/user-attachments/assets/655d07ef-d0f1-4b69-9c68-21c7a917c372)
![таблица товаров](https://github.com/user-attachments/assets/16d3eb4f-d656-4dc2-9165-7489e76a2447)
![таблица комментариев](https://github.com/user-attachments/assets/1df29a0d-d9e1-4b0d-8a71-892a95a4519f)

некоторые поля были добавлены для связи таблиц и предотвращения дублирования данных(такие как sku и post_id)

Т.К в тз не было указано, должны ли удаляться данные, они будут храниться. Т.е при обновлении корзины, старые данные из бд удаляться не будут, но отображаться в новом запросе не будут.
