from dbhelper import DBHelper
import sys
class Database:
    def __init__(self) -> None:
        self.db=DBHelper()
        self.interface()
        
    def interface(self):
        print('\n')
        user_input=input('''\t\t\t Press 1 to Enter Student Details\n
                         Press 2 to view Student details\n
                         Press 3 to update Student details\n
                         Press 4 to Delete a Student from the database\n
                         Press anything else to quit\n''')
        if user_input=='1':
            self.createStudent()
        
        elif user_input=='2':
            self.getStudentDetails()
            
        elif user_input=='3':
            self.updateStudentDetails()
            
        elif user_input=='4':
            self.removeStudent()
        
        else:
            sys.exit(0)
            
        
        
        
    def createStudent(self):
        Aid=input("Enter Admission number: ")
        Uid=input("Enter Roll number: ")
        name=input("Enter name of the student: ")
        father_name=input("Enter father's name: ")
        mother_name=input("Enter mother's name: ")
        branch=input("Enter Branch: ")
        contact_number=input("Enter Contact number of the student: ")
        address=input("Enter Address of the student: ")
        response=self.db.createStudent(Aid,Uid,name,father_name,mother_name,branch,contact_number,address)
        
        if response:
            print('\nSuccessfully Registered student')
            self.interface()
            
        else:
            print("An error occured, returning to main menu\n\n")
            self.interface()
            
    def getStudentDetails(self):
        Uid=input('Enter Roll number of the student: ')
        data=self.db.getStudentDetails(Uid)
        if data:
            print('\n\n')
            details={"Admission Number":data[0][0],
                     "Roll Number":data[0][1],
                     "Name":data[0][2],
                     "Father's name":data[0][3],
                     "Mother's name": data[0][4],
                     "Branch":data[0][5],
                     "Contact number":data[0][6],
                     "Address":data[0][7],
                     "Enrollment Year":data[0][0][0:4]}
            for key in details:
                print(key+':'+details[key])
            menu=input('press 1 to go to main menu')
            if menu=='1':
                self.interface()
        
        else:
            print('Student not found,returning to main menu\n\n')
            self.interface()
            
    def removeStudent(self):
        Uid=input("Enter roll number of Student: ")
        response=self.db.removeStudent(Uid)
        if response:
            print("\nStudent removed from database")
            self.interface()
            
    def updateStudentDetails(self):
        updateval=input('Press the corresponding key to update:\n b: branch\nc: Contact number\na: Address\n')
        if updateval not in ('a','b','c','A','B','C'):
            print("Invalid input")
            self.updateStudentDetails()
        else:
            Uid=input('Enter the roll number of the student: ')
            if updateval=='a' or updateval=='A':
                address=input('\nEnter new Address: ')
        
                response=self.db.updateStudentDetails(updateval,address,Uid)
            elif updateval=='b' or updateval=='B':
                branch=input('\nEnter new Branch: ')
                
                response=self.db.updateStudentDetails(updateval,branch,Uid)
            elif updateval=='c' or updateval=='C':
                contact=input('\nEnter new Contact number: ')
                
                response=self.db.updateStudentDetails(updateval,contact,Uid)
        if response:
            print("Updated Successfully\n")
            self.interface()
        else:
            print("An error occured")
            self.updateStudentDetails()
        
            
StudentDataBase=Database()