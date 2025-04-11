class Student_database:
    def __init__(self):
        self.student_list=[]
    
    def add_student(self,student):
        self.student_list.append(student)
    
    def find_student(self,student_id):
        for s in self.student_list:
            if s.student_id()==student_id:
                return s
        return None
    
    def view_all_students(self):
        for s in self.student_list:
            s.view_student_info()

class Student:
    def __init__(self,student_id,name,depertment):
        self.__student_id=student_id
        self.name=name
        self._depertment=depertment
        self.__is_enrolled=False

    def enroll_student(self):
        if self.__is_enrolled:
            print('This student is already enrolled')
        else:
            self.__is_enrolled=True
            print('Enrollment has done successfully')
    def drop_student(self):
        if not self.__is_enrolled:
            print('This student is not currently enrolled')
        else:
            self.__is_enrolled=False
            print('Student dropped has done succesfully')
    
    def view_student_info(self):
        print(f'Student id: {self.__student_id} Name: {self.name} Depertment: {self._depertment} Enrollment status: {"Enrolled" if self.__is_enrolled else "Not enrolled"}')

    def student_id(self):
        return self.__student_id
    
    def is_enrolled(self):
        return self.__is_enrolled

database=Student_database()

s1=Student('101','Sabbir','Computer Science')
s2=Student('102','Ahmed','Computer Science')
s3=Student('103','Mehran','Management')
s4=Student('104','Shazid','Software Developer')

database.add_student(s1)
database.add_student(s2)
database.add_student(s3)
database.add_student(s4)

while True:
    print('-'*50)
    print('\-----Student Enrollment System-----')
    print('1. View All Students')
    print('2. Enroll Student')
    print('3. Drop Students')
    print('4. Exit')

    command=input('Enter your choice: ')

    if command=='1':
        database.view_all_students()

    elif command=='2':
        st_id=input('Enter Student Id to Enroll: ')
        student=database.find_student(st_id)
        if student:
            student.enroll_student()
        else:
            print('Invalid Student Id')

    elif command=='3':
        st_id=input('Enter a Student Id to Drop: ')
        student=database.find_student(st_id)
        if student:
            student.drop_student()
        else:
            print('Invalid Student Id')
        
    elif command=='4':
        print('Exiting the Student System')
        break

    else:
        print('Invalid choice. PLease enter a number between 1 to 4')
