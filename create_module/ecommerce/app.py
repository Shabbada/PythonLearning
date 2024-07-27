import os
import time

while_bool = True
process = None
subprocces = None


class Applicant:
    number_of_ablicants = 0
    idenfication_number = 0
    applicants = []

    def __init__(self, first_name, last_name, middle_name, direction_id, grades):
        self.idenfication_number = self.create_id()
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.direction_id = direction_id
        self.grades = grades

    def full_info(self):
        return f"#{self.idenfication_number} | {self.first_name} {self.last_name} - {self.direction_id} {self.grades}"

    @classmethod
    def create_id(cls):
        cls.idenfication_number += 1
        return cls.idenfication_number

    @classmethod
    def string_initializer(cls, string):
        splitted = string.split(",")
        if len(splitted) != 5:
            raise ValueError("The information is incomplete")
        first_name, last_name, middle_name, direction_id, grades = splitted
        return cls(first_name, last_name, middle_name, direction_id, grades)

    @classmethod
    def add_applicant(cls, obj):
        pass
        cls.applicants.append(obj)

    @classmethod
    def __repr__(self) -> str:
        return self.full_info()


class Student(Applicant):
    limit = 3000
    number_of_students = 0

    def __init__(self, given_name, surname):
        self.given_name = given_name
        self.surname = surname

    def create_id(cls):
        cls.number_of_students += 1
        return cls.number_of_students


student1 = Student("Ali", "Valiyev")
student2 = Student("Vali", "Aliyev")
while while_bool:
    os.system("cls")
    if process == 1:
        applicant = input("Enter applicant information: ")
        try:
            applicant_obj = Applicant.string_initializer(applicant)
        except ValueError:
            print("Please enter complete information and your grades    ")
            continue
        Applicant.add_applicant(applicant_obj)
        print(f"\nInformation entered\n{applicant}\n")
    if process == 2:
        for applicant in Applicant.applicants:
            print(applicant)

    while while_bool:
        if subprocces == 1:
            print(Student.number_of_students)
        if process == 3:
            print(subprocces)
        if subprocces == 0:
            break

        if subprocces == 2:
            pr
        if subprocces == 3:
            full_name = input("Enter your fullname:      ")
            print(full_name)
        try:
            subprocces = int(
                input(
                    f" \n1-See list of Students\n2-Set Quotas \n3-Add Student\n0-Exit   "
                )
            )
        except ValueError:
            print("Please enter a number!")
            time.sleep(2)

    if process == 0:
        break
    try:
        process = int(
            input(
                f"\n1-Applicant create \n2-Applicant lists \n3-See list of \n0-Exit    "
            )
        )
    except ValueError:
        print("Please enter a number!")
        time.sleep(1)
