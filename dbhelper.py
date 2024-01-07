import mysql.connector
import sys
class DBHelper:
    def __init__(self) -> None:
        try:
            self.CollegeDB=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="collegedb")
            self.mycursor=self.CollegeDB.cursor()
        except:
            print("An error occured while connecting to Server")  
            sys.exit(0)
              
        else:
            print("Connected to database")

    def createStudent(self,Aid,Uid,name,father_name,mother_name,branch,contact_number,address):
        try:
            self.mycursor.execute('''
                                  INSERT INTO students(Admission_number,
                                  Roll_number,
                                  Name,Father_name,
                                  Mother_name,
                                  Branch,
                                  Contact_number,Address) 
                                  VALUES('{}','{}','{}','{}','{}','{}','{}','{}')'''
                                  .format(Aid,Uid,name,father_name,mother_name,branch,contact_number,address))
            self.CollegeDB.commit()
        except:
            return -1
        else:
            return 1
        
    def getStudentDetails(self,Uid):
        self.mycursor.execute('''
                              SELECT * FROM students WHERE Roll_number='{}'
                              '''.format(Uid))
        student_data=self.mycursor.fetchall()
        
        return student_data
    
    def removeStudent(self,Uid):
        try:
            self.mycursor.execute('''
                              DELETE FROM students WHERE Roll_number='{}'
                              '''.format(Uid))
            self.CollegeDB.commit()
        except:
            return -1
        else:
            return 1
        
    def updateStudentDetails(self,updateval,value,Uid):
            try:
                if updateval=='a' or updateval=='A':
                    self.mycursor.execute('''
                              UPDATE students SET Address='{}' WHERE Roll_number='{}'
                              '''.format(value,Uid))
                elif updateval=='b' or updateval=='B':
                    self.mycursor.execute('''
                              UPDATE students SET Branch='{}' WHERE Roll_number='{}'
                              '''.format(value,Uid))
                elif updateval=='c' or updateval=='C':
                    self.mycursor.execute('''
                              UPDATE students SET Contact_number='{}' WHERE Roll_number='{}'
                              '''.format(value,Uid))
                self.CollegeDB.commit()    
            except:
                return -1
            else:
                return 1
        