import module1


class Student(module1.Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.record_book}'

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) == 10:
            raise Exception('Група уже містить 10 студентів, більше не можна.')
        else:
            self.group.add(student)

    def delete_student(self, last_name):
        for student in list(self.group):
            if student.last_name == last_name.title():
                self.group.discard(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name.title():
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        ...
        return f'Group:{self.number}\n {all_students} '