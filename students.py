# students.py
# Gelson Cardoso

# This program handles some basic functions in a small student database,
# such as searching for student personal records, courses taken and its letter grades plus GPA,
# student accounts balance, number of students and total balance for all student accounts.

filename = "filename.txt"

class Students:
    def __init__(self, sid, name, last, dob, phone, address):  
        self.sid = sid
        self.name = name
        self.last = last       
        self.dob = dob
        self.phone = phone
        self.address = address
        self.courses = []
        self.accounts = []

        # Input = "I"
    def student_display(self):
        print("\nID:", self.sid, "\nName:", self.name, self.last, "\nDOB:", self.dob,
              "\nPhone#:", self.phone, "\nAddress:", self.address)

    def set_courses(self, course1, course2, course3, course4):
        self.courses.append(course1)
        self.courses.append(course2)
        self.courses.append(course3)
        self.courses.append(course4)
        
        # Input = "C"
    def courses_display(self):
        c_join = ' '.join(self.courses)
        c_clean = c_join.replace("C*", "")
        c_split = c_clean.split()
        print("Courses Taken:", c_split[0] + ",", c_split[12] + ",", c_split[24]
              + ",", c_split[36])

        # Input = "G"
    def grades_display(self):
        c_join = ' '.join(self.courses)
        c_clean = c_join.replace("C*", "")
        c_split = c_clean.split()

        # individual courses (1-4)
        c1 =  self.courses[0]
        c2 =  self.courses[1]
        c3 =  self.courses[2]
        c4 =  self.courses[3]

        avg_score1 = get_average(c1)
        avg_score2 = get_average(c2)
        avg_score3 = get_average(c3)
        avg_score4 = get_average(c4)
        avg_all = avg_score1 + avg_score2 + avg_score3 + avg_score4
        avg_total = avg_all / 4

        print("Course #1:", c_split[0], "| Grade:", get_grade(avg_score1),
              "\nCourse #2:", c_split[12], "| Grade:", get_grade(avg_score2),
              "\nCourse #3:", c_split[24], "| Grade:", get_grade(avg_score3),
              "\nCourse #4:", c_split[36], "| Grade:", get_grade(avg_score4),
              "\n\nStudent average score:", avg_total, "\nStudent GPA:",
              gpa_score(avg_total))

    def set_accounts(self, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
        self.accounts.append(a1)
        self.accounts.append(a2)
        self.accounts.append(a3)
        self.accounts.append(a4)
        self.accounts.append(a5)
        self.accounts.append(a6)
        self.accounts.append(a7)
        self.accounts.append(a8)
        self.accounts.append(a9)
        self.accounts.append(a10)

        # Input = "B"
    def account_display(self):                      
        # Account 1 (Registration)
        a1_join = ' '.join(self.accounts[0:2])
        a1_clean = a1_join.replace("A*", "")
        a1_split = a1_clean.split()
        print("Registration\nDate:", a1_split[1], "\nAmount: $", end = "")
        print(a1_split[2], "\n")

        # Account 2 (Tuition)
        a2_join = ' '.join(self.accounts[2:4])
        a2_clean = a2_join.replace("A*", "")
        a2_split = a2_clean.split()
        print("Tuition\nDate:", a2_split[2], "\nAmount: $", end = "")
        print(a2_split[3], "\n")

        # Account 3 (Books)
        a3_join = ' '.join(self.accounts[4:6])
        a3_clean = a3_join.replace("A*", "")
        a3_split = a3_clean.split()
        print("Books\nDate:", a3_split[1], "\nAmount: $", end = "")
        print(a3_split[2], "\n")

        # Account 4 (Housing)
        a4_join = ' '.join(self.accounts[6:8])
        a4_clean = a4_join.replace("A*", "")
        a4_split = a4_clean.split()
        print("Housing\nDate:", a4_split[1], "\nAmount: $", end = "")
        print(a4_split[2], "\n")

        # Account 5 (Payments)
        a5_join = ' '.join(self.accounts[8:10])
        a5_clean = a5_join.replace("A*", "")
        a5_split = a5_clean.split()
        print("Payments\nDate:", a5_split[1], "\nAmount: $", end = "")
        print(a5_split[2], "\n")

    def balance_display(self):
        # Account balance
        a1_total = float(self.accounts[1][11:])
        a2_total = float(self.accounts[3][11:])
        a3_total = float(self.accounts[5][11:])
        a4_total = float(self.accounts[7][11:])
        a5_total = float(self.accounts[9][11:])
        a_balance = a1_total + a2_total + a3_total + a4_total - a5_total

        return a_balance      

def get_average(course_info):
    total = 0
    score_list = course_info.split()
    scores_ = score_list[2:]
    count = len(scores_)
    for i in range(len(scores_)):
        total += int(scores_[i])
    return int(round(total/count,0))

def get_grade(points):
    if points>=90: return "A"
    if points>=80: return "B"
    if points>=70: return "C"
    if points>=60: return "D"
    return "F"

def gpa_score(points):
    if points>=93: return "4.0"
    if points>=90: return "3.7"
    if points>=87: return "3.3"
    if points>=83: return "3.0"
    if points>=80: return "2.7"
    if points>=77: return "2.3"
    if points>=73: return "2.0"
    if points>=70: return "1.7"
    if points>=67: return "1.3"
    if points>=65: return "1.0"
    return "0.0"

# To search student_list
def id_search(student_list, input_id):	
    for i in range(len(student_list)):
        if student_list[i].sid == "S*" + input_id:
            return i	
    return -999    

def main():
    
    f = open(filename, "r")

    # reads the file and split the lines removing the "\n"
    file_line = f.read().splitlines()
    
    # create Students objects using data from file
    # format = Students(sid0, name1, last2, dob3, phone4, address5)
    student_a = Students(file_line[0], file_line[1], file_line[2], file_line[3],
                         file_line[4], file_line[5])
    student_b = Students(file_line[20], file_line[21], file_line[22], file_line[23],
                         file_line[24], file_line[25])
    student_c = Students(file_line[40], file_line[41], file_line[42], file_line[43],
                         file_line[44], file_line[45])
    student_d = Students(file_line[60], file_line[61], file_line[62], file_line[63],
                         file_line[64], file_line[65])

    # set student courses
    student_a.set_courses(file_line[6], file_line[7], file_line[8], file_line[9])
    student_b.set_courses(file_line[26], file_line[27], file_line[28], file_line[29])    
    student_c.set_courses(file_line[46], file_line[47], file_line[48], file_line[49])   
    student_d.set_courses(file_line[66], file_line[67], file_line[68], file_line[69])

    # set student accounts
    student_a.set_accounts(file_line[10], file_line[11], file_line[12], file_line[13],
                           file_line[14], file_line[15], file_line[16], file_line[17],
                           file_line[18], file_line[19])
    student_b.set_accounts(file_line[30], file_line[31], file_line[32], file_line[33],
                           file_line[34], file_line[35], file_line[36], file_line[37],
                           file_line[38], file_line[39])   
    student_c.set_accounts(file_line[50], file_line[51], file_line[52], file_line[53],
                           file_line[54], file_line[55], file_line[56], file_line[57],
                           file_line[58], file_line[59])
    student_d.set_accounts(file_line[70], file_line[71], file_line[72], file_line[73],
                           file_line[74], file_line[75], file_line[76], file_line[77],
                           file_line[78], file_line[79])    
    

    # append students to student_list
    student_list = []
    student_list.append(student_a)
    student_list.append(student_b)
    student_list.append(student_c)
    student_list.append(student_d)

    while True:

        print("\n                -- Welcome -- \n\n"
              "I - display student personal info *\n"
              "C - display courses taken *\n"
              "G - display letter grades for courses taken and GPA *\n"
              "B - account balance *\n"
              "T - total # of students \n"
              "A - account balance of all students \n"
              "Q - quit program \n\n"
              "* Student ID required: (0110110, 0110220, 0110330 or 0110440)\n")
        
        s = input("Please enter a command: ")

        if s == "I" or s == "i":
            # Student info search        
            id_input = input("Please enter Student ID: ")
            ix = id_search(student_list, id_input)
 
            print("\n                -- Student Info --") 
            student_list[ix].student_display()

            again = input("\nWould you like to perform another search? (Y/N): ")            
            if again == "Y" or again == "y":
                continue
            else:
                break

        elif s == "C" or s == "c":
            # Courses taken search
            id_input = input("Please enter Student ID: ")
            ix = id_search(student_list, id_input)

            print("\n                -- Courses --\n")
            print(student_list[ix].name, student_list[ix].last, "\n")   
            student_list[ix].courses_display()

            again = input("\nWould you like to perform another search? (Y/N): ")            
            if again == "Y" or again == "y":
                continue
            else:
                break

        elif s == "G" or s == "g":
            # To display student grade letters & GPA
            id_input = input("Please enter Student ID: ")
            ix = id_search(student_list, id_input)            

            print("\n                -- Grades & GPA --\n")
            print(student_list[ix].name, student_list[ix].last, "\n")
            student_list[ix].grades_display()

            again = input("\nWould you like to perform another search? (Y/N): ")            
            if again == "Y" or again == "y":
                continue
            else:
                break

        elif s == "B" or s == "b":
            # To get individual student accounts & balance
            id_input = input("Please enter Student ID: ")
            ix = id_search(student_list, id_input)

            print("\n                -- Accounts & Balance --\n")
            print(student_list[ix].name, student_list[ix].last, "\n")
            student_list[ix].account_display()
            print("Account Balance: $", student_list[ix].balance_display())
    
            again = input("\nWould you like to perform another search? (Y/N): ")            
            if again == "Y" or again == "y":
                continue
            else:
                break

        elif s == "T" or s == "t":
            print("\n                -- Number of Students --\n")
            print("There are currently", len(student_list),
                  "students in this database. \n")                

            again = input("\nWould you like to perform another search? (Y/N): ")
            if again == "Y" or again == "y":
                continue
            else:
                break  

        elif s == "A" or s == "a":
            # To get total balance of all student accounts
            t_balance = 0
            t_balance = (student_a.balance_display() + student_b.balance_display()
                         + student_c.balance_display() + student_d.balance_display())

            print("\n                -- Total Balance --\n")
            print("The total balance of all student accounts is: $", end="")
            print(t_balance)

            again = input("\nWould you like to perform another search? (Y/N): ")
            if again == "Y" or again == "y":
                continue
            else:
                break  

        elif s == "Q" or s == "q":
            # To quit loop
            break
        
        else:
            print("\nInvalid input - try again.\n")
            
        # End of loop
    
    f.close()
        
main()
