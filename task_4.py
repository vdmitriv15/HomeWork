"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from uuid import uuid4
import hashlib

salt = uuid4().hex
my_cache = set()


def cache_url(url):
    h_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if h_url in my_cache:
        return print(f'{url} уже в кэш')
    else:
        my_cache.add(h_url)


cache_url('google.com')
cache_url('geekbrains.ru')
cache_url('pythonworld.ru')
cache_url('amazon.com')
cache_url('github.com')
cache_url('ebay.com')
cache_url('geekbrains.ru')
cache_url('ebay.com')

print(my_cache)

