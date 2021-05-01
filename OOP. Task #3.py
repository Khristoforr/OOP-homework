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

    def average_grade(self):
        total_sum_of_all_grades = 0
        count_of_all_grades = 0
        for i in self.grades.values():
            for j in i:
                total_sum_of_all_grades += j
                count_of_all_grades += 1
        if count_of_all_grades == 0:
            return "Ошибка"
        else:
            return total_sum_of_all_grades/count_of_all_grades

    def __str__(self):
        student_presentation = (f'Имя: {self.name} \n'
              f'Фамилия: {self.surname} \n'
              f'Средняя оценка за домашние задания: {self.average_grade()} \n'
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
              f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return student_presentation

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a student!")
            return
        return self.average_grade() < other.average_grade()




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lector_grade = {}

    def average_grade(self):
        total_sum_of_all_grades = 0
        count_of_all_grades = 0
        for i in self.lector_grade.values():
            for j in i:
                total_sum_of_all_grades += j
                count_of_all_grades += 1
        if count_of_all_grades == 0:
            return "Ошибка"
        else:
            return total_sum_of_all_grades / count_of_all_grades

    def __str__(self):
        lector_presentation = (f'Имя: {self.name} \n'
              f'Фамилия: {self.surname} \n'
              f'Средняя оценка за лекции: {self.average_grade()} \n')
        return lector_presentation

    def __lt__(self, other):
        if not isinstance(other, Lector):
            print("Not a lector!")
            return
        return self.average_grade() < other.average_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        reviewer_presentation = (f'Имя: {self.name} \n'
              f'Фамилия: {self.surname}')
        return reviewer_presentation



