class ValidationError(Exception):
    pass


class Student:

    def __init__(self, surname, name, group_number, marks):
        self.surname = surname
        self.name = name
        self.group_number = group_number
        self.marks = marks

    def __repr__(self):
        return self.surname, self.name, self.group_number, self.marks

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise ValidationError('Family name must be "str"')
        self._surname = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValidationError('Name must be "str"')
        self._name = value

    @property
    def info(self):

        return [self.surname, self.name, self.group_number, self.marks]


class School:
    def __init__(self):
        self.book_of_students = []

    def add_student(self, student):
        if student not in self.book_of_students:
            self.book_of_students.append(student.__repr__())
        else:
            pass

        return self.book_of_students

    def get_best_students(self):
        best_students = []
        for student in self.book_of_students:
            count = 0
            for marks in student[3]:
                if marks == 5 or marks == 6:
                    count += 1
                    if count == 5:
                        best_students.append(student.__str__())
        return best_students

    def get_students(self, group_number):
        choosen_students_group = []
        for student in self.book_of_students:
            student_group = ''
            for element in student[2]:
                student_group += element
            if student_group == group_number:
                choosen_students_group.append(student)
        return choosen_students_group

    def get_students_without_exams(self):
        students_auto_exams = []
        for student in self.book_of_students:
            if sum(student[3]) / 5 > 7:
                students_auto_exams.append(student)
        return students_auto_exams


st1 = Student('Mogilev', 'Nikita', "122", [5, 5, 6, 5, 6])
st2 = Student('Petrov', 'Ivan', "122", [1, 5, 4, 7, 8])
st3 = Student('Losev', 'Valera', "1242", [10, 9, 9, 7, 8])

school1 = School()
school1.add_student(st1)
school1.add_student(st2)
school1.add_student(st3)


print(school1.book_of_students)
print(school1.get_best_students())
print(school1.get_students("122"))
print(school1.get_students_without_exams())
