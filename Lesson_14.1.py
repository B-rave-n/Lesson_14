class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Student(Human):

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

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

st3 = Student('Male', 17, 'John', 'Cloud', 'AN-13')
st4 = Student('Male', 21, 'Jo', 'Biden', 'AN-14')
st5 = Student('Male', 20, 'Her', 'Son', 'AN-15')
st6 = Student('Male', 16, 'Johny', 'Buzz', 'AN-16')
st7 = Student('Male', 34, 'Luk', 'Skywalker', 'AN-17')
st8 = Student('Female', 17, "Wo", 'Man', 'AN-18')
st9 = Student('Male', 78, 'Jo', 'Nin', 'AN-19')
st10 = Student('Male', 300, 'Ka', 'Non', 'AN-20')
st11 = Student('Male', 1981, 'Lon', 'Don', 'AN-21')
st12 = Student('Female', 1200, 'Pol', 'Tava', 'AN-22')

gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
try:
    gr.add_student(st11)
except Exception as error:
    print(f'{error}') # Видасть помилку

gr.delete_student('Cloud') # Видалить студента Cloud

try:
    gr.add_student(st11)
    print(f'Студента {st11} успішно додано')
except Exception as error:
    print(f'{error}') # Помилки не буде, бо з'явилося вільне місце
try:
    gr.add_student(st12)
except Exception as error:
    print(f'{error}') # Видасть помилку
