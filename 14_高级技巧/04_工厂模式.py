class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class factory:
    def get_person(self,type):
        if type=='w':
            return Worker()
        elif type=='s':
            return Student()
        else:
            return Teacher()


fc = factory()
fc.get_person('w')