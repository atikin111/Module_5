# Задание 1: Анализ списка чисел с помощью Counter
# - Сгенерируйте случайный список чисел.
# - Используйте Counter, чтобы подсчитать количество уникальных элементов в списке.
# - Найдите три наиболее часто встречающихся элемента в списке и выведите их с количеством вхождений.
# from random import randint
# from collections import Counter

# list_numb = [randint(0,50) for i in range(50)]
# counter = Counter(list_numb)
# print(counter)
# often_numbers = counter.most_common(3)
# print(often_numbers)

# Задание 2: Работа с именованными кортежами
# - Создайте именованный кортеж Book с полями title, author, genre.
# - Создайте несколько экземпляров Book.
# - Выведите информацию о книгах, используя атрибуты именованных кортежей.
# from collections import namedtuple
#
# Book = namedtuple('Book', ['tittle', 'author', 'genre'])
#
# book1 = Book(tittle='Приключения Алисы в стране чудес', author='Чарльз Лютвидж Доджсон', genre='Сказка')
# book2 = Book(tittle='Атлант расправил плечи', author='Айн Рэнд', genre='Роман-антиутопия')
# book3 = Book(tittle='Бог всегда путешествует инкогнито', author='Лоран Гунель', genre='Психологический триллер')
#
# print(f'Название книги: {book1.tittle}\n'
#       f'Автор: {book1.author}\n'
#       f'Жанр: {book1.genre}\n')
#
# print(f'Название книги: {book2.tittle}\n'
#       f'Автор: {book2.author}\n'
#       f'Жанр: {book2.genre}\n')
#
# print(f'Название книги: {book3.tittle}\n'
#       f'Автор: {book3.author}\n'
#       f'Жанр: {book3.genre}\n')

# Задание 3: Работа с defaultdict
# - Создайте defaultdict с типом данных list.
# - Добавьте несколько элементов в словарь, используя ключи и значения.
# - Выведите содержимое словаря, где значения - это списки элементов с одинаковыми ключами.

# from collections import defaultdict
#
# my_dict = defaultdict(list)
#
# my_dict['обувь'].extend(['кроссовки', 'ботинки', 'лоферы', 'туфли'])
# my_dict['мебель'].extend(['стол', 'стул', 'диван'])
#
# for key, value in my_dict.items():
#     print(f'{key}: {value}')

# Задание 4: Использование deque для обработки данных
# Создайте deque и добавьте в него элементы.
# Используйте методы append, appendleft, pop и popleft для добавления и удаления элементов из deque.
# Проверьте, как изменяется deque после каждой операции.

# from collections import deque
#
# my_queue = deque(['остров', 'книга', 'письмо', 'протокол'])
# my_queue.append(5)
# print(my_queue)
# my_queue.appendleft(0)
# print(my_queue)
# my_queue.pop()
# print(my_queue)
# my_queue.popleft()
# print(my_queue)

# Задание 5: Реализация простой очереди с помощью deque
# Напишите функции для добавления и извлечения элементов из deque.
# Создайте пустой deque.
# Используйте написанные функции для добавления и извлечения элементов из очереди.

from collections import deque

def deque_append(deque, item):
    deque.append(item)
    print(f'Добавлен элемент: {item}')

def deque_appendleft(deque, item):
    deque.appendleft(item)
    print(f'Добавлен элемент в начало: {item}')

def deque_pop(deque):
    item = deque.pop()
    print(f'Извлечен элемент из конца списка: {item}')

def deque_popleft(deque):
    item = deque.popleft()
    print(f'Извлечен элемент из конца списка: {item}')


my_deque = deque()
deque_append(my_deque, '123')
deque_append(my_deque, 'простыня')
deque_append(my_deque, 'подушка')
print(my_deque)
deque_pop(my_deque)
print(my_deque)
deque_popleft(my_deque)
print(my_deque)