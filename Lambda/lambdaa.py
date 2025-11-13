#1
fruits_list = ["apple", "kiwi", "banana", "fig"]
sort_fruits = list(filter(lambda x: len(x) > 4, fruits_list))
print(sort_fruits)


#2
students = [{"name": "John", "grade": 90}, {"name": "Jane", "grade": 85}, {"name": "Dave", "grade": 92}]
sorted_students = max(students, key=lambda student: student['grade'])
print(sorted_students)


#3
numbers = [(1, 5), (3, 2), (2, 8), (4, 3)]
sort_numbers = sorted(numbers, key=lambda x: x[0] + x[1])
print(sort_numbers)


#4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filt_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filt_numbers)


#5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Student(name = {self.name}, age = {self.age}'

persons = [
    Person('Nikita', 28),
    Person('Nadya', 28),
    Person('Viktor', 30),
    Person('Elena', 51),
    Person('Sergey', 52)
]

sorted_person = sorted(persons, key=lambda x: x.age)
print(sorted_person)