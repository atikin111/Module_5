# JSON
import json

# import json
#
# with open('students.json', 'r', encoding='utf-8') as j_file:
#     data = json.load(j_file)
#
# # Общее количество студентов
# total_students = len(data)
# print(f'Общее количество студентов: {total_students}')
#
# # Студенты, изучающие Python
# python_students = [student for student in data if 'Python' in student['предметы']]
# print(f'Количество студентов, изучающих Python: {len(python_students)}')
#
# # Самый старший студент
# max_age = max(student['возраст'] for student in data)
# oldest_students = [student for student in data if student['возраст'] == max_age]
#
# for student in oldest_students:
#     # Создаем копию без предметов для вывода
#     student_data = student.copy()
#     student_data.pop('предметы')
#     print(f'Данные студента с самым высоким возрастом: {student_data}')


# CSV

# import csv
#
# from collections import defaultdict
#
# with open('sales.csv', 'r', encoding='utf-8') as file:
#     data = list(csv.DictReader(file))
#
# # Общая сумма
# total = sum(int(row['Сумма']) for row in data)
# print(f'Общая сумма продаж: {total}')
#
# # Суммы по продуктам
# sales_by_product = defaultdict(int)
# for row in data:
#     sales_by_product[row['Продукт']] += int(row['Сумма'])
#
# # Лучший продукт
# best = max(sales_by_product, key=sales_by_product.get)
# print(f'Лучший продукт: {best} (продажи: {sales_by_product[best]})')
#
# # Вся статистика
# for product, amount in sales_by_product.items():
#     print(f'{product}: {amount}')
#
# # Cтатистика по месяцам
# month_by_product = defaultdict(int)
# for row in data:
#     date = row['Дата']
#     month = date.split('-')[1]
#     amount = int(row['Сумма'])
#     month_by_product[month] += amount
# for month, amount in sorted(month_by_product.items()):
#     print(f'Общая сумма продаж для {month} месяца: {amount}')


# JSON and CSV
import json
import csv
from collections import defaultdict

with open('employees.json', 'r', encoding='utf-8') as file_json, open('performance.csv', 'r', encoding='utf-8') as file_csv:
    # Считываем данные с файлов
    data_json = json.load(file_json)
    data_csv = csv.DictReader(file_csv)

    # Объединяем словари по ID сотрудников
    merged_data = []
    performance_dict = {item['employee_id']: item for item in data_csv}

    for employee in data_json:
        employee_id = str(employee.get('id'))
        performance_info = performance_dict.get(employee_id)
        # print(performance_info)

        if performance_info:
            merged_employee = employee.copy()
            merged_employee.update(performance_info)
            merged_data.append(merged_employee)

    print(f'Сопоставленные данные с файлов:\n{merged_data}')

# Определяем среднюю производительность сотрудников
quality_employees = len([item for item in data_json])
sum_performance = 0
for row in merged_data:
    performance = int(row['performance'])
    sum_performance += performance
mid_sum_performance = float(sum_performance / quality_employees)
print(f'Средняя производительность сотрудников: {mid_sum_performance}')

# Сотрудник с наивысшей производительностью
performance = [int(employee['performance']) for employee in merged_data]
max_perf = max(performance)
best_employee = [employee for employee in merged_data if max_perf == int(employee['performance'])]
for item in best_employee:
    print(f'Сотрудник с наивысшей производительностью:\n{item['имя']} с производительность {item['performance']}')

