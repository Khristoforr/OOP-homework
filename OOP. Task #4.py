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


def calculate_student_average_grade(list_of_students, course_name):
    total_grades = 0
    count_grades = 0
    for i in list_of_students:
        total_grades += sum(i.grades[course_name])
        count_grades += len(i.grades[course_name])
    average = total_grades/len(list_of_students)
    return f'Cредняя оценка студентов по курсу {course_name} ' \
           f'составляет {average}'

def calculate_lector_average_grade(list_of_lectors, course_name):
    total_grades = 0
    count_grades = 0
    for i in list_of_lectors:
        total_grades += sum(i.lector_grade[course_name])
        count_grades += len(i.lector_grade[course_name])
    average = total_grades/count_grades
    return f'Cредняя оценка лекторов по курсу {course_name} ' \
           f'составляет {average}'

petya = Student("Petya", "Ivanov", "male")
petya.finished_courses.append('history')
petya.courses_in_progress.append('programming')

viktoria = Student("Viktoria", "Petrova", "female")
viktoria.finished_courses.append('history')
viktoria.courses_in_progress.append('programming')
viktoria.courses_in_progress.append('chemistry')

ivan_bobrov = Lector("Ivan", "Bobrov")
ivan_bobrov.courses_attached.append("programming")

egor_ignatov = Lector("Egor", "Ignatov")
egor_ignatov.courses_attached.append('chemistry')
egor_ignatov.courses_attached.append('programming')

igor_smirnov = Reviewer("Igor", "Smirnov")
igor_smirnov.courses_attached.append("programming")

anton_gorshkov = Reviewer("Anton", "Gorshkov")
anton_gorshkov.courses_attached.append('chemistry')

#Поставим оценки за домашнюю работу
igor_smirnov.rate_hw(petya,'programming',9)
igor_smirnov.rate_hw(viktoria,'programming',9)
anton_gorshkov.rate_hw(petya, 'chemistry', 7)
anton_gorshkov.rate_hw(viktoria, 'chemistry', 8)

# оценка лекторов студентами
petya.rate_a_lector(egor_ignatov,'chemistry', 10)
viktoria.rate_a_lector(egor_ignatov, 'chemistry', 5)
petya.rate_a_lector(ivan_bobrov,'programming', 2)
viktoria.rate_a_lector(ivan_bobrov,'programming', 5)
viktoria.rate_a_lector(egor_ignatov, 'programming', 5)

print(petya)
print()
print(viktoria)
print()
print(egor_ignatov)
print()
print(ivan_bobrov)
print()
print(anton_gorshkov)
print()
print(igor_smirnov)
print(viktoria < petya)
print(ivan_bobrov < egor_ignatov)

print(calculate_student_average_grade([petya,viktoria],'programming'))
print(calculate_lector_average_grade([ivan_bobrov,egor_ignatov],'programming'))
