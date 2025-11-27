import json
import csv


FILE = 'student_list.json'

with open(FILE, 'r', encoding='UTF-8') as file:
    students = json.load(file)


def get_average_score_student():
    for name, info in students.items():
        average_score_student = get_average_score(info['grades'])
        name_student = name
        print(f'Средний балл студента {name_student}: {average_score_student}')



def get_average_score(grades):
    list_grades = grades.values()

    return sum(list_grades) / len(list_grades)


def get_best_student():
    best_student = None
    best_score = 0

    for name, info in students.items():
        average_score = get_average_score(info['grades'])

        if average_score > best_score:
            best_score = average_score
            best_student = name

    return best_student, best_score


def get_worst_student():
    worst_student = None
    worst_score = 101

    for name, info in students.items():
        average_score = get_average_score(info['grades'])

        if average_score < worst_score:
            worst_score = average_score
            worst_student = name

    return worst_student, worst_score


def find_student():

    name = input('Введите имя студента для получения информации: ')

    if name in students:
        student_info = students[name]
        print(f'Имя: {name}'
              f'\nВозраст: {student_info['age']}'
              f'\nПредметы: {student_info['subjects']}'
              f'\nОценки: {student_info['grades']}')
    else:
        print('Студента с таким именем не существует')


def sorted_students():
    student_averages = {}

    for name, info in students.items():
        student_averages[name] = get_average_score(info['grades'])

    sorted_students = sorted(student_averages.items(), key=lambda x: x[1], reverse=True)
    print('Студенты отсортированы по среднему баллу (убывание):')

    for name, avg_score in sorted_students:
        print(f'{name}: {avg_score}')


def students_listdict():
    students_list = []

    for name, info in students.items():
        student_dict = {
            'name': name,
            'age': info['age'],
            'subjects': info['subjects'],
            'grades': info['grades']
        }
        students_list.append(student_dict)

    return students_list


def write_in_csv():
    with open('student_list.csv', 'w') as csvfile:
        headers = ['name', 'age', 'grade']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()

        for name, info in students.items():
            avg_grade = get_average_score(info['grades'])
            writer.writerow({
                'name': name,
                'age': info['age'],
                'grade': avg_grade
            })


if __name__ == '__main__':
    get_average_score_student()
    get_best_student()
    get_worst_student()
    find_student()
    sorted_students()
    students_listdict()
    write_in_csv()