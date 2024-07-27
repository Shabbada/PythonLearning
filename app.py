class Student():
    def __init__(self,name,surname,number):
        self.name = name
        self.surname = surname
        self.number = number
    
    def get_name(self):
        return f" Name: {self.name} "
    def get_surname(self):
        return f" Surname: {self.surname}"
    def get_number(self):
        return f"Number: {self.number} "

    def full_info(self):
        return f"Name:{self.name}, Surname:{self.surname},Number:{self.number}"

    @classmethod
    def from_full_info(cls,full_info):
        parts = full_info.split(",")
        obj = cls(parts[0],parts[1],parts[2])
        return obj

student1 = Student("Shahzod","Shavkatov","99-999-99-99")
student2 = Student("Abdurahmon","Shuhratov","88-888-988-9988") 
student3 = Student("Jaloliddin","Ruzikulov","77-777-777--780")
