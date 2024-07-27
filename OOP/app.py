class Student():
    def __init__(self,name,surname,number):
        self.name = name
        self.surname = surname
        self.number = number
    
    def full_info(self):
        return f"Name: {self.name}, Surname: {self.surname}, Number: {self.number}"

    @classmethod
    def from_full_info(cls,full_info):
        parts = full_info.split(",")
        obj = cls(parts[0],parts[1],parts[2])
        return obj
    
student1 = Student("Shahzod","Shavkatov","33-022-07-51")
student2 = Student("Jaloliddin","Ruzikulov","99-929-2392-9")
