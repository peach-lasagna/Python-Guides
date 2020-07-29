# Virtualenvwrapper

## установка

Linux:

```sh
$ pip install virtualenvwrapper
```

Windows:

```bash
$ pip install virtualenvwrapper-win
```

Отлично! Установка завершена!

## Использование, основные возможности

**mkvirtualenv:**
Создает и активирует venv

```properties
$ mkvirtualenv venv_name
(venv_name) $
```

или

```properties
$ mkvirtualenv -p $(which python3.9) venv_name
(venv_name) $
```

В каталоге (\*этот путь стоит по умолчанию)

> C:/Users/Username/Envs

должна появиться папка _venv_name_.

Теперь всё готово и мы можем устанавливать зависимости!

```properties
(venv_name) $ pip install requests
(venv_name) $ pip list
requests
```

Можно сохранить все используемые зависимости в файл:

```properties
(venv_name) $ pip freeze > requirements.txt
```

Чтобы установить все необходимые зависимости с файла, используйте

```properties
(venv_name) $ pip install -r requirements.txt
```

Чтобы выйти из venv-а прописываем **deactivate:**

```properties
(venv_name) $ deactivate
$
```

С помощью **workon** вы можете увидеть список установленных venv-ов:

```properties
$ workon
venv_name
```

а также подключиться к существующему:

```properties
$ workon venv_name
(venv_name) $
```

Это очень удобно если вы делаете несколько проектов с одинаковыми подключенными библиотеками и не хотите создавать для каждого свой venv (а также засорять систему).

А если необходимость в venv-е отпадет, то можно прописать **rmvirtualenv**(только перед этим деактивируйте venv)

```properties
(venv_name)$ deactivate
$ rmvirtualenv venv_name
$ workon
$
```

Ссылки:

- [Дока virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)
- [Pypi](https://pypi.org/project/virtualenvwrapper-win/)
- [Статья на русском](https://python-scripts.com/virtualenv)
