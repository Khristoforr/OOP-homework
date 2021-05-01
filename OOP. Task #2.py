class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_a_lector(self, lector, course, grade):
        if isinstance(lector,Lector) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.lector_grade.keys():
                lector.lector_grade.get(course).append(grade)
            else:
                lector.lector_grade[course] = [grade]
        else:
            return (f'Ошибка! Студент {self.name} и лектор {lector.name} {lector.surname} не участвуют в обучении '
                  f'в рамках одного курса')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lector_grade = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


