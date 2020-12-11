print("=======!!!! welcome !!!!======")

username = input("Enter your username :\t")
password = input(f"Enter your password {username} :\t")

def options():
    print('''
  ====!!! APPASAHEB BIRNALE PUBLIC SCHOOL !!! ====

    ============================================
    |   1. Insert student details              |
    |   2. Search student details              |
    |   3. Update student details              |
    |   4. Delete student details              |
    ============================================
    ''')
    choice = input("Enter the option you want from 1-4 :\t")
    if choice == "1":
        stu_id = int(input("enter the id of the student :\t"))
        stu_name = input("Enter the name of the student :\t")
        stu_age = input("Enter the age of the student :\t")
        stu_gender = input("Enter the gender of the student (m/f/other) :\t")
        stu_ph_no = input("Enter the contact number of the student (eg: 91 956-789-6522) :\t")
        stu_email_add = input("Enter the email address of the student :\t")

    elif choice == "2":
        student_name1 = input("Enter the name of the student you want to search :\t")
        
    elif choice == "3":
        id_of_students = int(input("Enter the id of the student who's details you want to update :\t"))

    elif choice == "4":
        id_for_deleting = int(input("Enter the id of the student who's details you want to delete from the database :\t"))

    else:
        print("The option you choosed is invalid . Plz choose a number from 1-4.")

if username == "administrator" and password == "administrator":
    options()
