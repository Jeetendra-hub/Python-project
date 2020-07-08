

import sqlite3 as lite

#functionality goes here


class DatabaseManage(object):

    def __init__(self):
        global Dbcon
        try:
            Dbcon = lite.connect('new_born_pro')
            with Dbcon:
                cur =  Dbcon.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS new_born_pro(Id INTEGER PRIMARY KEY AUTOINCREMENT, "
                            "name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create a DB!")

    #TODO create data
    def insert_data(self,data):
        try:
            with Dbcon:
                cur = Dbcon.cursor()
                cur.execute("INSERT INTO new_born_pro(name, description, price, is_private)VALUES (?,?,?,?)", data)
                return True
        except Exception:
            print("Unable to create a DB !")

    #fethc data
    def fetch_data(self):
        try:
            with Dbcon:
                cur = Dbcon.cursor()
                cur.execute("SELECT * FROM new_born_pro")
                return cur.fetchall()
        except Exception:
            return False

    #delete data
    def delete_date(self, id):
        try:
            with Dbcon:
                cur = Dbcon.cursor()
                sql = "DELETE FROM new_born_pro WHERE id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            print("can't able to delete your previous data")


# TODO: provide interface to user

def main():
    print("\n")
    print("$"*45)
    print("\n:: NEW_BORN_PRO MANAGEMENT :: \n")
    print("$" * 45)
    print("\n")

    database=DatabaseManage()
    print("$" * 45)
    print("\n :: User Manual :: \n")
    print("$" * 45)

    print('Press 1. Insert a new course')
    print('Press 2. Show all course')
    print('Press 3. Delete a course (NEED ID OF COURSE)\n')
    print("$" * 45)
    print("\n")

    choice = input("Enter a choice: ")

    if choice == "1":
        course_name=input("\n Enter course name: ")
        description = input("\n Enter course description: ")
        price = input("\n Enter course price: ")
        private = input("\n Enter course private (0/1): ")


        if database.insert_data([course_name,description,price,private]):
            print("Course was inserted successfully")
        else:
            print("OOPS something is wrong")

    elif choice == "2":
        print("\n:: Course List ::")

        for index, item in enumerate(database.fetch_data()):
            print("\n sl no : "+ str(index + 1))
            print("Course ID : " + str(item[0]))
            print("Course Name : " + str(item[1]))
            print("Course Description : " + str(item[2]))
            print("Course Price : " + str(item[3]))
            private = 'Yes' if item[4] else 'No'
            print("Is Private : " + private)
            print("\n")

    elif choice == "3":
        record_id = input("Enter the course ID:")

        if database.delete_date(record_id):
            print("Course was deleted with a success")
        else:
            print("OOPS SOMETHING WENT WRONG")

    else:
        print("\n BAD CHOICE")

    restart=input("Do you want to restart press y to yes or n to no:")
    if restart=="y":
        main()
    else:
        print("OK see you next time...")
main()



