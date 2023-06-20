# Проект Foodgram (foodgram-project-react)

![example workflow](https://github.com/akimmatvienko/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

«Продуктовый помощник», онлайн-сервис и API для него. На этом сервисе пользователи смогут публиковать
рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед
походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных
блюд.

## Стек технологий

* Python 3.9
* Django 3.2
* Django REST framework
* Djoser
* Postgres

## Документация

## Описание функционала

### Главная страница

Содержимое главной страницы — список первых шести рецептов, отсортированных по дате публикации (от новых к старым).
Остальные рецепты доступны на следующих страницах: внизу страницы есть пагинация.

### Страница рецепта

На странице — полное описание рецепта. Для авторизованных пользователей — возможность добавить рецепт в избранное и в
список покупок, возможность подписаться на автора рецепта.

### Страница пользователя

На странице — имя пользователя, все рецепты, опубликованные пользователем и возможность подписаться на пользователя.

### Подписка на авторов

Подписка на публикации доступна только авторизованному пользователю. Страница подписок доступна только владельцу.

Сценарий поведения пользователя:

* Пользователь переходит на страницу другого пользователя или на страницу рецепта и подписывается на публикации автора
  кликом по кнопке «Подписаться на автора».
* Пользователь переходит на страницу «Мои подписки» и просматривает список рецептов, опубликованных теми авторами, на
  которых он подписался. Сортировка записей — по дате публикации (от новых к старым).
* При необходимости пользователь может отказаться от подписки на автора: переходит на страницу автора или на страницу
  его рецепта и нажимает «Отписаться от автора».

### Список избранного

Работа со списком избранного доступна только авторизованному пользователю. Список избранного может просматривать только
его владелец.

Сценарий поведения пользователя:

* Пользователь отмечает один или несколько рецептов кликом по кнопке «Добавить в избранное».
* Пользователь переходит на страницу «Список избранного» и просматривает персональный список избранных рецептов.
* При необходимости пользователь может удалить рецепт из избранного.

### Список покупок

Работа со списком покупок доступна авторизованным пользователям. Список покупок может просматривать только его владелец.

Сценарий поведения пользователя:

* Пользователь отмечает один или несколько рецептов кликом по кнопке «Добавить в покупки».
* Пользователь переходит на страницу Список покупок, там доступны все добавленные в список рецепты. Пользователь
  нажимает кнопку Скачать список и получает файл с суммированным перечнем и количеством необходимых ингредиентов для
  всех рецептов, сохранённых в «Списке покупок».
* При необходимости пользователь может удалить рецепт из списка покупок.

Список покупок скачивается в формате .txt.

При скачивании списка покупок ингредиенты в результирующем списке не должны дублироваться; если в двух рецептах есть
сахар (в одном рецепте 5 г, в другом — 10 г), то в списке должен быть один пункт: Сахар — 15 г.

В результате список покупок может выглядеть так:

* Фарш (баранина и говядина) (г) — 600
* Сыр плавленый (г) — 200
* Лук репчатый (г) — 50
* Картофель (г) — 1000
* Молоко (мл) — 250
* Яйцо куриное (шт) — 5
* Соевый соус (ст. л.) — 8
* Сахар (г) — 230
* Растительное масло рафинированное (ст. л.) — 2
* Соль (по вкусу) — 4
* Перец черный (щепотка) — 3

### Фильтрация по тегам

При нажатии на название тега выводится список рецептов, отмеченных этим тегом. Фильтрация может проводится по нескольким
тегам в комбинации «или»: если выбраны несколько тегов — в результате должны быть показаны рецепты, которые отмечены
хотя бы одним из этих тегов.

При фильтрации на странице пользователя должны фильтроваться только рецепты выбранного пользователя. Такой же принцип
должен соблюдаться при фильтрации списка избранного.

### Регистрация и авторизация

В проекте доступна система регистрации и авторизации пользователей.

Обязательные поля для пользователя:

* Логин
* Пароль
* Email
* Имя
* Фамилия

Уровни доступа пользователей:

* Гость (неавторизованный пользователь)
* Авторизованный пользователь
* Администратор

Что могут делать неавторизованные пользователи:

* Создать аккаунт.
* Просматривать рецепты на главной.
* Просматривать отдельные страницы рецептов.
* Просматривать страницы пользователей.
* Фильтровать рецепты по тегам.

Что могут делать авторизованные пользователи:

* Входить в систему под своим логином и паролем.
* Выходить из системы (разлогиниваться).
* Менять свой пароль.
* Создавать/редактировать/удалять собственные рецепты
* Просматривать рецепты на главной.
* Просматривать страницы пользователей.
* Просматривать отдельные страницы рецептов.
* Фильтровать рецепты по тегам.
* Работать с персональным списком избранного: добавлять в него рецепты или удалять их, просматривать свою страницу
  избранных рецептов.
* Работать с персональным списком покупок: добавлять/удалять любые рецепты, выгружать файл с количеством необходимых
  ингредиентов для рецептов из списка покупок.
* Подписываться на публикации авторов рецептов и отменять подписку, просматривать свою страницу подписок.

Что может делать администратор:

Администратор обладает всеми правами авторизованного пользователя.

Плюс к этому он может:

* изменять пароль любого пользователя,
* создавать/блокировать/удалять аккаунты пользователей,
* редактировать/удалять любые рецепты,
* добавлять/удалять/редактировать ингредиенты.
* добавлять/удалять/редактировать теги.

### Получение проекта:

Форк репозитория с GitHab:

```commandline
https://github.com/akimmatvienko/foodgram-project-react.git
```

### Запуск проекта на сервере:

#### Подготовка GitHub Actions:

После создания репозитория в своем аккаунте GitHub во вкладке настроек
репозитория проекта, в меню выбрать `Secrets and variables` выбрать `Actions`,
нажать кнопку `New repository secret`, создать переменные окружения:

| Секрет               | Значение                                                                               |
|----------------------|----------------------------------------------------------------------------------------|
| SECRET_KEY           | "секретный ключ джанго-проекта" в кавычках                                             |
| ALLOWED_HOSTS        | *, хост сервера                                                                        |
| CSRF_TRUSTED_ORIGINS | доверенные хосты для проверки CSRF (http://... https://...)                            |
| DOCKER_USERNAME      | имя пользователя в DockerHub                                                           |
| DOCKER_PASSWORD      | пароль доступа в DockerHub                                                             |
| DB_ENGINE            | django.db.backends.postgresql                                                          |
| DB_NAME              | имя базы данных                                                                        |
| POSTGRES_USER        | логин для подключения к базе данных                                                    |
| POSTGRES_PASSWORD    | пароль для подключения к БД                                                            |
| DB_HOST              | db                                                                                     |
| DB_PORT              | 5432                                                                                   |
| USER                 | логин сервера                                                                          |
| HOST                 | ip сервера                                                                             |
| SSH_KEY              | приватный ключ локальной машины, по которому происходит вход на сервер (~/.ssh/id_rsa) |
| PASSPHRASE           | фраза-пароль ключа ssh (если установлена)                                              |
| TELEGRAM_TO          | id телеграм-чата (@userinfobot)                                                        |
| TELEGRAM_TOKEN       | токен телеграм-бота (@BotFather - /mybots - Choose a bot - API Token)                  |


#### Подготовка сервера:

Войти на свой удаленный сервер.
Установить Docker и docker-compose.

```commandline
sudo apt install docker.io
```

```commandline
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

```commandline
sudo chmod +x /usr/local/bin/docker-compose
```

Из паки `infra` локального проекта cкопировать на сервер в домашнюю дирректорию
файлы настроек nginx и docker-compose

```commandline
scp docker-compose.yaml <USER>@<HOST>:/home/<USER>
```

```commandline
scp nginx.conf <USER>@<HOST>:/home/<USER>
```

Запуск при любом `push` на GitHub проект:
- тестируется на соответствие PEP8,
- обновляются и сохраняются на DockerHub образы `backend` и `frontend`,
- в домашней директории сервера автоматически создается файл `.env`
- проект автоматически разворачивается на сервере,
- о чем приходит сообщение на telegram.

Для запуска сервиса на сервере вручную:
- на сервере в домашней директории создать файл `.env` с настройками
по образцу выше с учетом данных хоста.

```commandline
nano .env
```

- запуск

```commandline
sudo docker-compose up -d
```

---
После успешного развертывания проекта на сервере или локально:
Выполнить миграции, создать суперпользователя, собрать статику

```commandline
sudo docker-compose exec backend python manage.py migrate
```

```commandline
sudo docker-compose exec backend python manage.py createsuperuser
```

```commandline
sudo docker-compose exec backend python manage.py collectstatic --no-input
```

Для подгрузки в базу данных ингредиентов:

```commandline
sudo docker-compose exec backend python manage.py loaddata data/ingredients.json
```

В админ-зоне проекта создать необходимые теги (без тегов рецепт создать не удастся)

---

### Работа с сервисом:

Сервис будет доступен:

при локальном развертывании - http://localhost/

При развертывании на сервере - http://51.250.29.141/

Доступ к административной части: http://51.250.29.141/admin/

Спецификация API: http://51.250.29.141/api/docs/redoc.html
