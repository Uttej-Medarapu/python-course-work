class Person:
    def __init__(self, name, department):
        self.name = name  # Encapsulation
        self.department = department

    def display(self):
        print(f"Name: {self.name}, Department: {self.department.name}")


class Student(Person):   #inheritance
    def __init__(self, student_id, name, department):
        super().__init__(name, department)
        self.student_id = student_id
        self.courses = []
        self.__grades = {}

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.students.append(self)
            print(f"{self.name} enrolled in {course.name}")

    def set_grade(self, course, grade):
        self.__grades[course] = grade

    def calculate_gpa(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades.values()) / len(self.__grades)

    def display(self):
        super().display()
        print("Courses Enrolled:", [course.name for course in self.courses])
        print("GPA:", self.calculate_gpa())


class Professor(Person):
    def __init__(self, professor_id, name, department, salary):
        super().__init__(name, department)
        self.professor_id = professor_id
        self.__salary = salary
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)
        course.professor = self
        print(f"{self.name} is now teaching {course.name}")

    def get_salary(self):
        return self.__salary

    def display(self):
        super().display()  #Polymorphism
        print("Courses Taught:", [course.name for course in self.courses])
        print("Salary:", self.__salary)


class Course:
    def __init__(self, course_id, name, department, credits):
        self.course_id = course_id
        self.name = name
        self.department = department
        self.credits = credits
        self.students = []
        self.professor = None

    def display(self):
        print(f"Course ID: {self.course_id}, Name: {self.name}, Credits: {self.credits}, Department: {self.department.name}")
        print(f"Professor: {self.professor.name if self.professor else 'Not Assigned'}")
        print("Students Enrolled:", [student.name for student in self.students])


class Department:
    def __init__(self, department_id, name):
        self.department_id = department_id
        self.name = name
        self.courses = []
        self.faculty = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_faculty(self, faculty):
        self.faculty.append(faculty)

    def add_student(self, student):
        self.students.append(student)

    def display(self):
        print(f"Department ID: {self.department_id}, Name: {self.name}")
        print("Courses Offered:", [course.name for course in self.courses])
        print("Faculty:", [fac.name for fac in self.faculty])
        print("Students:", [stu.name for stu in self.students])


class University:  #abstraction
    instance = None

    def __new__(cls, name):
        if cls.instance is None:
            cls.instance = super(University, cls).__new__(cls)
        return cls.instance

    def __init__(self, name):
        self.name = name
        self.departments = []
        self.students = []
        self.faculty = []
        self.total_revenue = 0
        self.total_expenses = 0

    def add_department(self, department):
        self.departments.append(department)

    def register_student(self, student):
        self.students.append(student)

    def register_faculty(self, faculty): 
        self.faculty.append(faculty)
        self.total_expenses += faculty.get_salary()

    def calculate_finances(self): #abstracrtion is used here for not showing details to the students,facaulty
        return self.total_revenue - self.total_expenses

    def display(self):
        print(f"University Name: {self.name}")
        print("Departments:", [dept.name for dept in self.departments])
        print("Total Finances:", self.calculate_finances())

# here, i am taking one example

university = University("Codegnan Destination University")
department = Department(1, "Computer Science")
university.add_department(department)

course1 = Course(101, "Python", department, 4)
department.add_course(course1)

student1 = Student(1001, "Uttej", department)
department.add_student(student1)
university.register_student(student1)

professor1 = Professor(2001, "Sowmya Madam", department, 70000)
department.add_faculty(professor1)
university.register_faculty(professor1)

professor1.assign_course(course1)
student1.enroll(course1)
student1.set_grade(course1, 90)

# displaying all values

university.display()
department.display()
student1.display()
professor1.display()
course1.display()
