# Poetry

## установка

```sh
$ pip install --user poetry
```

## Основные возможности

- Управление зависимостями через toml файл (прощай, `requirements.txt`)

- Автоматическое создание изолированного виртуального окружения Python (теперь не нужно для этого вызывать virtualenv)

- Удобное создание пакетов (отныне не нужно ~~копипастить~~ создавать setup.py каждый раз)

- `poetry.lock` файл для фиксирования версий зависимостей

- **pyproject.toml** - надежная замена `setup.py`, `requirements.txt`, `setup.cfg`, `MANIFEST.in` и `Pipfile`

- Прекрасный тандем с **pyenv**

- Сделает за вас всю "грязную" работу.

## Использование

### Создание проекта

#### Ручное создание проекта

```properties
# Конфигурим новый проект
$ poetry init
# Poetry задаст несколько вопросов и по итогу напишет файл pyproject.toml, в котором пропишет все настройки проекта

# Добавим пару пакетов в проект. Пакеты будут доступны только в виртуальное среде, которая сейчас активна в текущей папке.
$ poetry add flask celery
# Poetry все поставит и пропишет зависимости в pyproject.toml

# Если у вас есть пакеты, которые не поставить через PIP (например, кусок кода от другого подразделения вашей конторы), можно добавить зависимость вручную
$ poetry add my-package --path ../my-package/

```

#### Создание проекта с помощью poetry

**poetry new** создаст новый проект

```properties
$ poetry new poetry-demo
Created package poetry_demo in poetry-demo
```

с такой структурой:

```properties
poetry-demo
├── pyproject.toml
├── README.rst
├── poetry_demo
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_poetry_demo.py
```

Вот что лежит в `pyproject.toml`:

```toml
[tool.poetry]
name = "my-demo-project"
version = "0.1.0"
description = ""
authors = ["Author <user@mail.cam>"]

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"

```

Но что всё это значит?
**Разделы pyproject.toml:**

- `[tool.poetry]` предназначен для описания проекта: название, версия, краткая информация о проекте и т.д.

- в `[tool.poetry.dependencies]` указаны все production зависимости. Их можно указать вручную (привет, requirements.txt), но мы так делать не будем (привет, npm!).

- `[tool.poetry.dev-dependencies]` предназначен для зависимостей во время разработки (привет, pytest, tox!)
  _(Для зависимостей, которые не нужны в рантайме (Тесты, прекрммит хуки и тп) )_

### управление зависимостями

#### Добавление зависимостей

**poetry add** справится с этим

```properties
$ poetry add requests
Using version ^2.24.0 for requests

Updating dependencies
Resolving dependencies... (9.9s)

Writing lock file


Package operations: 16 installs, 0 updates, 0 removals

  - Installing pyparsing (2.4.7)
  - Installing six (1.15.0)
  - Installing atomicwrites (1.4.0)
  - Installing attrs (19.3.0)
  - Installing certifi (2020.6.20)
  - Installing chardet (3.0.4)
  - Installing colorama (0.4.3)
  - Installing idna (2.9)
  - Installing more-itertools (8.4.0)
  - Installing packaging (20.4)
  - Installing pluggy (0.13.1)
  - Installing py (1.9.0)
  - Installing urllib3 (1.25.9)
  - Installing wcwidth (0.2.5)
  - Installing pytest (5.4.3)
  - Installing requests (2.24.0)
```

после этого в проекте появится файл `poetry.lock` и в `pyproject.toml` изменится `[tool.poetry.dependencies]`:

```toml
[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.24.0"
```

Если вам хочется изменить `[tool.poetry.dev-dependencies]`,
то добавьте флаг **--dev**:

```properties
$ poetry add requests --dev
```

Для установки конкретной версии зависимости используем **pack==version**:

```properties
$ poetry add requests==2.0.0
```

#### Удаление зависимостей

```properties
$ poetry remove requests
```

#### Список установленных зависимостей

```properties
$ poetry show
```

### О venv

Стоит отметить, что по этому поводу париться не стоит - _poetry_ всё сделает.

А найти путь к venv-у можно так:

```properties
$ poetry config virtualenvs.path
```

Не нравится путь? Измените!

```properties
$ poetry config virtualenvs.path /path/to/cache/directory/virtualenvs
```

[Список других настроек](https://python-poetry.org/docs/configuration/)

Для активации виртуального окружения необходимо выполнить следующую команду:

```properties
$ poetry shell
```

#### Список окружений

```properties
$ poetry env list
Virtual environment already activated: C:\Users\Username\AppData\Local\pypoetry\Cache\virtualenvs\my-demo-project-gk2Ak0kl-py3.8
```

#### Инфа о текущем venv-е

```properties
$ poetry env info
```

#### Переключение между venv-ами

```properties
$ poetry env use /full/path/to/python
$ poetry env use python3.7
$ poetry env use 3.7
$ poetry env use test-O3eWbxRl-py3.7
```

#### Удаление venv-а

**Перед удалением обязательно прописывать `poetry shell` !**
Существует несколько способов удалить окружение (деактивировать его при этом необязательно):

```properties
$ poetry env remove /full/path/to/python
$ poetry env remove python3.7
$ poetry env remove 3.7
$ poetry env remove test-O3eWbxRl-py3.7
```

### Сборка пакета

И радость моя стала полной, а восторг неописуемым:

```properties
$ poetry build
```

Эта команда,по факту, заменяет `setup.py`.

<!--
-Видишь setup.py ?
-Нет
-И я не вижу, а он есть..
-->

В папке **dist** будут сформированы пакеты. Чтобы поделиться своим творением с другими разработчиками, например через _Pypi_, выполните:

```properties
$ poetry publish
```

## Фичи

### Создание зависимости к либе не с Pypi

- **github**
  Для этого делаем следующее:

```toml
[tool.poetry.dependencies]
requests = { git = "https://github.com/requests/requests.git" }
```

Для подключения к конкретной ветке:

```toml
[tool.poetry.dependencies]
requests = { git = "https://github.com/kennethreitz/requests.git", branch = "next" }
```

Для конкретного tag или rev соответственно:

```toml
[tool.poetry.dependencies]
numpy = { git = "https://github.com/numpy/numpy.git", tag = "v0.13.2" }
flask = { git = "https://github.com/pallets/flask.git", rev = "38eb5d3b" }
```

- **Локальный файл\\папка**

```toml
[tool.poetry.dependencies]
# directory
my-package = { path = "../my-package/" }

# file
my-package = { path = "../my-package/dist/my-package-0.1.0.tar.gz" }
```

- Из других мест
  Указываем сразу в файл

```toml
[tool.poetry.dependencies]
# directory
my-package = { url = "https://example.com/my-package-0.1.0.tar.gz" }
```

или делаем

```properties
$ poetry add https://example.com/my-package-0.1.0.tar.gz
```

**Важно!**
Если вы записывали напрямую в `pyproject.toml`, то надо прописать

```properties
$ poetry install
```

[Другие настройки](https://python-poetry.org/docs/dependency-specification/)

### Основные команды

[Тык](https://python-poetry.org/docs/cli/)

<!-- Надо бы в  "Использование" запихать это-->

- **new**

Создаст за вас простую структуру проекта.

- **init**

Создаст файл `pyproject.toml` в текущем каталоге и попросит вас заполнить его.

- **install**

Установит зависимости из `pyproject.toml` и запишет в файл `poetry.lock`.

- **update**

Чтобы получить последние версии зависимостей и обновить `poetry.lock` , вы должны использовать эту команду.

```properties
# для обновления конкретного пака
$ poetry update requests toml
```

- **remove**

Удалит указанный пакет из списка установленных.

- **add**

Добавит зависимость(и).

- **show**

Выведет список установленных пакетов.

- **build**

Выполняет работу `setup.py` - собирает пакет.

- **publish**

Эта команда публикует пакет, ранее созданный с помощью этой `build` команды, в удаленном репозитории.

- **config**

Позволяет редактировать настройки конфигов `poetry` и репозиториев.

- **run**

Выполняет заданную команду внутри venv-а.

- **shell**

Активирует venv (если он еще не создан, то создаёт).

- **check**

Проверяет структуру `pyproject.toml` и возвращает подробный отчет об ошибках.

- **search**

Ищет указанный pack на `Pypi` и выводит результат поиска(Все совпадения).

- **lock**

Блокирует (без установки!) зависимости, указанные в `pyproject.toml`.

- **version**

Показывает текущую версию проекта или записывает новую версию в `pyproject.toml`.

- **export**

Экспортирует `.lock` файл в другой формат(пока что поддерживается `.txt`).

```properties
$ poetry export -f requirements.txt > requirements.txt
```

- **env**

Используется для взаимодействия с `venv` проекта(ов).

### Run file

[Stack](https://stackoverflow.com/questions/59286983/how-to-run-a-script-using-pyproject-toml-settings-and-poetry)

Чтобы запустить файл `my-script.py` в `pyproject.toml` необходимо написать

```toml
[tool.poetry.scripts]
my-script = "my_module:main"
```

после чего мы сможем запустить файл из консоли:

```properties
$ poetry run my-script
```

<!--  -->

Но что если я хочу запустить конкретную команду из файла?

Давайте в `test_poetry_demo.py` запишем следующее:

```py
def start():
    print("Hello")
```

после чего в `pyproject.toml` добавим

```toml
[tool.poetry.scripts]
my-script = "tests.test_poetry_demo:start"
```

В настоящее время [tool.poetry.scripts] эквивалент setuptools console_scripts.

А теперь мы можем запустить всё это в консоли!

```properties
$ poetry run my-script
Hello
```

Для лучшего использования можно использовать [argparse](https://docs.python.org/3/library/argparse.html).

## Что почитать

- [Классная и понятная дока](https://python-poetry.org/docs/)
- [Habr](https://habr.com/ru/post/455335/)
- [Рандомная статья](https://khashtamov.com/ru/python-poetry-dependency-management/)
