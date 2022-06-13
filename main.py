def define_avg_grade(students, course):
    grades_sum, grades_count = 0, 0
    for student in students:
        if course in student.grades:
            grades_sum += sum(student.grades[course])
            grades_count += len(student.grades[course])
    return grades_sum / grades_count if grades_count > 0 else 0


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        res = ''
        res += f'\nprint({self.get_var_names()})\n'
        res += f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}\n'
        res += f'Средняя оценка за домашние задания: {self.define_avg_grade()}\n'
        res += f'Курсы в процессе изучения: {self.show_courses(self.courses_in_progress)}\n'
        res += f'Завершенные курсы: {self.show_courses(self.finished_courses)}'
        return res

    def __lt__(self, other):
        return self.define_avg_grade() < other.define_avg_grade()

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print(f'Ошибка: {self.name} {self.surname} can not rate {lecturer.name} {lecturer.surname} in {course}')
            return 'Ошибка'

    def define_avg_grade(self):
        grades_sum, grades_count = 0, 0
        for grades in self.grades.values():
            grades_sum += sum(grades)
            grades_count += len(grades)
        return grades_sum / grades_count if grades_count > 0 else 0

    def show_courses(self, courses):
        if len(courses) == 0:
            return '-'
        text = ''
        for course in courses:
            text += ', ' if len(text) > 0 else ''
            text += course
        return text

    def get_var_names(self):
        for k, v in globals().items():
            if v is self:
                return k

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def get_var_names(self):
        for k, v in globals().items():
            if v is self:
                return k

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = ''
        res += f'\nprint({self.get_var_names()})\n'
        res += f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}\n'
        res += f'Средняя оценка за лекции: {self.define_avg_grade()}'
        return res

    def __lt__(self, other):
        return self.define_avg_grade() < other.define_avg_grade()

    def define_avg_grade(self):
        grades_sum, grades_count = 0, 0
        for grades in self.grades.values():
            grades_sum += sum(grades)
            grades_count += len(grades)
        return grades_sum / grades_count if grades_count > 0 else 0


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print(f'Ошибка: {self.name} {self.surname} can not rate {student.name} {student.surname} in {course}')
            return 'Ошибка'

    def __str__(self):
        res = ''
        res += f'\nprint({self.get_var_names()})\n'
        res += f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Math']

bad_student = Student('Pupkin', 'Vasya', 'your_gender')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['Math']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Math']

bad_reviewer = Reviewer('Any', 'Buddy')
bad_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(bad_student, 'Python', 5)
cool_reviewer.rate_hw(bad_student, 'Python', 6)
cool_reviewer.rate_hw(bad_student, 'Math', 4)

cool_lecturer = Lecturer('Adam', 'Smith')
cool_lecturer.courses_attached += ['Python']

bad_lecturer = Lecturer('Adam', 'Sandler')
bad_lecturer.courses_attached += ['Python']

best_student.rate_hw(cool_lecturer, 'Python', 9)
best_student.rate_hw(cool_lecturer, 'Python', 8)
bad_student.rate_hw(cool_lecturer, 'Python', 10)
best_student.rate_hw(bad_lecturer, 'Python', 7)
best_student.rate_hw(bad_lecturer, 'Python', 6)
bad_student.rate_hw(bad_lecturer, 'Python', 8)
# best_student.rate_hw(cool_lecturer, 'Economy', 1)  # error

print(best_student)
print(bad_student)
print(cool_lecturer)
print(bad_lecturer)
print(cool_reviewer)
print(bad_reviewer)

print()
print(f'best_student.grades: {best_student.grades}')
print(f'bad_student.grades: {bad_student.grades}')
print(f'cool_lecturer.grades: {cool_lecturer.grades}')
print(f'bad_lecturer.grades: {bad_lecturer.grades}')

print()
print(f'best_student > bad_student: {best_student > bad_student}')
print(f'cool_lecturer < bad_lecturer: {cool_lecturer < bad_lecturer}')

print()
print("Средняя оценка за домашние задания по всем студентам в рамках конкретного курса: ", end='')
print(define_avg_grade([best_student, bad_student], 'Python'))

print("Средняя оценка за лекции всех лекторов в рамках курса: ", end='')
print(define_avg_grade([cool_lecturer, bad_lecturer], 'Python'))