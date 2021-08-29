class Student:
    """ class constructor """
    def __init__(self, name, age, usn, course, fee, paid):
        self.name = name.upper()
        self.age = age
        self.usn = usn.upper()
        self.course = course.upper()
        self.fee = fee
        self.paid = paid
    
    # defining a private method can be accessed only inside the class
    def __newForm(self, filename, content):
        try:
            with open(filename, 'w') as f:
                f.write(content)
                
        except FileNotFoundError:
            print("File Not found or doesn't exist")
        
    def registerNewStudent(self):
        courses = {"ECE": "Electronics and Communication Engineering",
                   "CSE": "Computer Science Engineering",
                   "CVE": "Civil Engineering",
                   "MEE": "Mechanical Engineering",
                   "EEE": "Electrical and Electronics Engineering",
                   "DSE": "Data Science Engineering"
                  }
        
        balance = self.fee - self.paid
        
        if balance < 0:
            balance = 0
        
        if self.paid >= self.fee:
            self.paid = self.fee
            reg = "Yes (No fee due)"
            
        else:
            reg = "No (Fee Due)"
            
        self.course = courses[self.course]
        
        f = f"{self.name.replace(' ', '_')}_{self.age}_{self.usn}.txt"
        c = f"Name\t\t\t: {self.name}\nAge\t\t\t: {self.age}\nUSN/ID\t\t: {self.usn}\n"\
            f"Course\t\t: {self.course}\nRegistered\t: {reg}\nTotal Fee\t: Rs.{self.fee}/-\nFee Paid\t\t: Rs.{self.paid}/-\nBalance\t\t: Rs.{balance}/-"
        
        # create student form
        self._Student__newForm(f, c)
        
        print("\n*** Student registration successful ***")
        

if __name__ == "__main__":
    
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    usn = input("Enter student ID/USN: ")
    course = input("Enter student course: ")
    fee = int(input("Enter student total fee: "))
    paid = int(input("Enter student fee paid: "))
    
    s = Student(name, age, usn, course, fee, paid)
    s.registerNewStudent()
