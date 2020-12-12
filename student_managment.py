import mysql.connector 
from mysql.connector import Error
from tabulate import tabulate

print("=======!!!! welcome !!!!======")

username = input("Enter your username :\t")
# username = "administrator"
password = input(f"Enter your password {username} :\t")
# password = "administrator"

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
    return create_db_connection

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

def show_data_of_subject(id_of_stu):
    cursor.execute(f"SELECT * FROM test.student_master WHERE ID = '{id_of_stu}'")
    row = cursor.fetchall()
    print(tabulate(row, headers=cursor.column_names),"\n")
    
def options():
    print('''
  ====!!! APPASAHEB BIRNALE PUBLIC SCHOOL !!! ====

    ============================================
    |   1. Insert student details              |
    |   2. Search student details              |
    |   3. Update student details              |
    |   4. Delete student details              |
    |   5. Enter 'q' to exit                   |
    ============================================
    ''')
    choice = input("Enter the option you want from 1-4 :\t")

    if choice == "1":
        no_of_entries = int(input("Enter the number of entries you want to do :\t"))

        for _ in range(no_of_entries):
            ID = int(input("Enter the id of the student :\t"))
            Name = input("Enter the name of the student :\t")
            Age = input("Enter the age of the student :\t")
            Gender = input("Enter the gender of the student (m/f/o) :\t")
            Address = input("Enter the address of the student :\t")
            Phone_number = input("Enter the contact number of the student (eg: 9567896522) :\t")
            Email_address = input("Enter the email address of the student :\t")
        
            cursor.execute('''INSERT INTO test.student_master (ID, Name, Age, Gender, Address, Phone_number, Email_address) VALUES (
                %s, %s, %s, %s, %s, %s, %s 
                ) ''', params = (ID, Name, Age, Gender, Address, Phone_number, Email_address))
            mysqldb.commit()
        cursor.execute("SELECT * FROM test.student_master")
        rows = cursor.fetchall()
        print("\n",tabulate(rows, headers=cursor.column_names),"\n")

    elif choice == "2":
        print('''
        How do you want to search for the student details ?
        You can choose the options from the list given below :-

        =====================================================
        |   1. ID                                           |
        |   2. Name                                         |
        |   3. Age                                          |
        |   4. Gender                                       |
        |   5. Address(city)                                |
        =====================================================
        ''')

        def options(option):
            if option == "1":
                stu_id = int(input("Enter the id of the student you want to search :\t"))
                cursor.execute(f"SELECT * FROM test.student_master WHERE ID = '{stu_id}';")
                rows = cursor.fetchall()
                print("\n",tabulate(rows, headers=cursor.column_names),"\n")
        
            elif option == "2":
                stu_name = input("Enter the name of the student you want to search :\t")
                cursor.execute(f"SELECT * FROM test.student_master WHERE Name = '{stu_name}';")
                rows = cursor.fetchall()
                print("\n",tabulate(rows, headers=cursor.column_names),"\n")

            elif option == "3":
                stu_age = input("Enter the age of the student you want to search :\t")
                cursor.execute(f"SELECT * FROM test.student_master WHERE Age = '{stu_age}';")
                rows = cursor.fetchall()
                print("\n",tabulate(rows, headers=cursor.column_names),"\n")

            elif option == "4":
                stu_gender = input("Enter the gender of the student you want to search :\t")
                cursor.execute(f"SELECT * FROM test.student_master WHERE Gender = '{stu_gender}';")
                rows = cursor.fetchall()
                print("\n",tabulate(rows, headers=cursor.column_names),"\n")

            elif option == "5":
                stu_address = input("Enter the address of the student you want to search :\t")
                cursor.execute(f"SELECT * FROM test.student_master WHERE Address = '{stu_address}';")
                rows = cursor.fetchall()
                print("\n",tabulate(rows, headers=cursor.column_names),"\n")

        try:
            option = input("Enter your option here :\t")
            options(option)
        except Error as err:
            print("You entered a invalid option, try again !!!")
            print(err)
    elif choice == "3":            
        id_of_stu = input("Enter the id of the student who's details you want to update :\t")
        show_data_of_subject(id_of_stu)
        column_name = input("Enter the column name you want to update :\t")
        new_data = input("Enter the new data you want to insert :\t")
        cursor.execute(f"SELECT {column_name} FROM test.student_master WHERE ID = '{id_of_stu}'")
        old_data = cursor.fetchall()
        for _ in range(2):
            old_data = old_data[0]
        cursor.execute(f"UPDATE student_master SET {column_name} = '{new_data}' where {column_name} = '{old_data}'")
        mysqldb.commit()
        show_data_of_subject(id_of_stu)

    elif choice == "4":
        id_of_stu = int(input("Enter the id of the student who's details you want to delete from the database :\t"))
        show_data_of_subject(id_of_stu)
        answer = input("Do you want to delete the data of the particular student ('y'/'n') :\t")
        if answer == "y":
            cursor.execute(f"DELETE FROM test.student_master WHERE ID = '{id_of_stu}'")
            mysqldb.commit()
            cursor.execute(f"SELECT * FROM test.student_master")
            rows = cursor.fetchall()
            print("\n",tabulate(rows, headers=cursor.column_names),"\n")
        else:
            print("Countinue ....")            

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
        ID int Primary Key NOT NULL,
        Name varchar(30) NOT NULL,
        Age int NOT NULL,
        Gender char(1) NOT NULL,
        Address varchar(50) NOT NULL, 
        Phone_number char(10) ,
        Email_address varchar(20) ,
        CONSTRAINT chk_stu CHECK (Age<=20 AND Gender in ('m','f','o'))
        )
        '''
    create_db(connection, query0)
    execute_query(connection, query1)
    while True:
        options()
