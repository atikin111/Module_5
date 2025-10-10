import csv
from dataclasses import field


#
# # Открываем файл для чтения
# with open('csv_example.csv') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)  # Выводим каждую строку файла
#
# with open('csv_example.csv') as f:
#     reader = csv.reader(f)
#     print(list(reader))
#
# import csv
#
# data = [
#     {'Имя': 'Анна', 'Возраст': '25', 'Город': 'Москва'},
#     {'Имя': 'Петр', 'Возраст': '30', 'Город': 'Санкт-Петербург'},
#     {'Имя': 'Мария', 'Возраст': '28', 'Город': 'Киев'}
# ]
#
# # Записываем данные в CSV файл с использованием словаря
# with open('данные_с_заголовками.csv', 'w') as csvfile:
#     fieldnames = ['Имя', 'Возраст', 'Город']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()  # Записываем заголовки
#     writer.writerows(data)  # Записываем данные
#
# # Чтение данных из CSV файла с использованием словаря
# with open('данные_с_заголовками.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['Имя'], row['Возраст'], row['Город'])
#
# with open('данные_с_заголовками.csv') as f:
#     reader = csv.reader(f, delimiter=',')
#     for row in reader:
#         print(row)

# TASK_1

# import csv
#
# def convert_txt_to_csv(file_txt, file_csv):
#     with open(file_txt, 'r', encoding='utf-8') as f_txt:
#         stripped = (line.strip().split() for line in f_txt)
#         with open(file_csv, 'w', encoding='utf-8', newline='') as f_csv:
#             csv_writer = csv.writer(f_csv)
#             headers = ['Наименование товара', 'Количество товара','Цена (руб.)']
#             csv_writer.writerow(headers)
#             csv_writer.writerows(stripped)
#
# if __name__ == '__main__':
#     file_txt = 'prices.txt'
#     file_csv = 'prices.csv'
#     convert_txt_to_csv(file_txt, file_csv)


# TASK_2

import csv

def the_order(file_csv):
    with open(file_csv, 'r', encoding='utf-8') as f_csv:
        sum_order_cost = 0
        reader = csv.reader(f_csv)
        next(f_csv, None)
        for line in reader:
            quantity = int(line[1])
            price = int(line[2])
            sum_order_cost += quantity * price
        print(f'Общая стоимость заказа: {sum_order_cost} рублей')

if __name__ == '__main__':
    file_csv = 'prices.csv'
    the_order(file_csv)


