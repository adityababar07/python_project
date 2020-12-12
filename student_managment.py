import mysql.connector 
from mysql.connector import Error

print("=======!!!! welcome !!!!======")

# username = input("Enter your username :\t")
username = "administrator"
# password = input(f"Enter your password {username} :\t")
password = "administrator"

def create_db_connection(host_name, user_name, password, database):
    try:
        global mysqldb
        mysqldb = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=password,
            db = database
        )
        print("Database connection succesfull.")
    except Error as err:
        print(f"Error :\t'{err}'")

def create_db(connection, query0):
    cur = mysqldb.cursor()
    try:
        cur.execute(query0)
        mysqldb.commit()
        print("Database created successfully.")
    except Error as err:
        print(f"Error : '{err}")

def execute_query(connection, query1):
    global cursor
    cursor = mysqldb.cursor()
    try:
        cursor.execute(query1)
        mysqldb.commit()
        print("Table created successfully.")
    except Error as err:
        print(f"Error : '{err}")
    
def options():
    print('''
  ====!!! APPASAHEB BIRNALE PUBLIC SCHOOL !!! ====

    ============================================
    |   1. Insert student details              |
    |   2. Search student details              |
    |   3. Update student details              |
    |   4. Delete student details              |
    |   5. Enter 'q' to exit         |
    ============================================
    ''')
    choice = input("Enter the option you want from 1-4 :\t")
    if choice == "1":
        no_of_entries = int(input("Enter the number of entries you want to do :\t"))
        ID = int(input("enter the id of the student :\t"))
        Name = input("Enter the name of the student :\t")
        Age = input("Enter the age of the student :\t")
        Gender = input("Enter the gender of the student (m/f/o) :\t")
        Address = input("Enter the address of the student :\t")
        Phone_number = input("Enter the contact number of the student (eg: 9567896522) :\t")
        Email_address = input("Enter the email address of the student :\t")
        for _ in range(no_of_entries):
            cursor.execute('''INSERT INTO test.student_master (ID, Name, Age, Gender, Address, Phone_number, Email_address) VALUES (
                %s, %s, %s, %s, %s, %s, %s 
                ) ''', params = (ID, Name, Age, Gender, Address, Phone_number, Email_address))
            mysqldb.commit()

    elif choice == "2":
        student_name1 = input("Enter the name of the student you want to search :\t")

    elif choice == "3":
        id_of_students = int(input("Enter the id of the student who's details you want to update :\t"))

    elif choice == "4":
        id_for_deleting = int(input("Enter the id of the student who's details you want to delete from the database :\t"))

    elif choice == "q":
        exit()
            
    else:
        print("The option you choosed is invalid . Plz choose a number from 1-4.")
        return options()

if username == "administrator" and password == "administrator":
    connection = create_db_connection("localhost", "hacker07", "admin1234", "test")
    query0 = "CREATE DATABASE if not exists test;"
    query1 = '''
        CREATE TABLE if not exists student_master(
        ID integer Primary Key NOT NULL,
        Name varchar(30) NOT NULL,
        Age integer NOT NULL,
        Gender char(1) NOT NULL,
        Address varchar(50) NOT NULL, 
        Phone_number char(10) ,
        Email_address varchar(20) ,
        check(Gender in ('m','f','o'))
        )
        '''
    create_db(connection, query0)
    execute_query(connection, query1)
    while True:
        options()
