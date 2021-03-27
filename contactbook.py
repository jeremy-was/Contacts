import sqlite3
import pandas as pd 

connection = sqlite3.connect("contacts.db")
cursor = connection.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts(ID_Number INTEGER PRIMARY KEY, Name TEXT, Phone INTEGER, Email TEXT)")

def add_contact():
    name = input("\nEnter name:  ")
    print(f"Name {name.title()} successfully added")
    number = input("\nEnter phone number:  ")
    print("Phone number successfully added")
    email = input("\nEnter email address:  ")
    print("Email address successfully added")
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name.title(), number, email))
    print(f"\n     New record added for {name.title()}")
    connection.commit()
    number_of_rows()
    print("\n1. Add another")
    print("2. Main Menu")
    print("3. Quit app\n")
    while True:
        try:
            inny = int(input("Please enter 1/2/3  "))
            if inny == 1:
                add_contact()
                break
            elif inny == 2:
                choices()
                break
            elif inny == 3:
                print("\n     Thanks for using the contacts app\n")
                cursor.close()
                break
        except:
            print("Bad input, try again")
            continue
        else:
            print("Bad input, try again")
            continue

def display_contacts():
    print("\n"*25)
    print(pd.read_sql_query("SELECT * FROM contacts ORDER BY name", connection))
    number_of_rows()
    choices()

def delete_contact():
    num_rows = cursor.execute("SELECT * FROM contacts")
    total_records = len(num_rows.fetchall())
    total_number_check = total_records
    while True:
        try:
            name = input("\nPlease enter name of contact to delete (% is wildcard):  ")
            search_it = f"SELECT * FROM contacts WHERE name LIKE '{name}'"
            cursor.execute(search_it)
            rows = cursor.fetchall()
            number_of = 0
            for row in rows:
                number_of += 1
            print(f"\n     Found {number_of} match(es)\n")
            # for row in rows:
            #     print(row)
            if number_of > 0:
                print(pd.read_sql_query(f"SELECT * FROM contacts WHERE name LIKE '{name}' ORDER BY name", connection))
                break
            else:
                continue
        except:
            print("No contacts found, try again")
            continue
    if number_of > 1:
        name2 = input("\nMore than 1 match. Now type fully, as above, the contact name to delete:  ")
    else:
        name2 = input("\nNow type name fully, as above, to confirm delete:  ")
    sql = f"DELETE FROM contacts WHERE name LIKE '{name2}'"
    cursor.execute(sql)
    connection.commit()
    num_rows = cursor.execute("SELECT * FROM contacts")
    total_records = len(num_rows.fetchall())
    if total_number_check > total_records:
        print(f"\n     {name2.title()} has been deleted from contacts")
    else:
        print("\n     name not found, Delete unsuccessful")
    number_of_rows()
    print("\n1. Delete another")
    print("2. Main Menu")
    print("3. Quit app\n")
    while True:
        try:
            inny = int(input("Please enter 1/2/3  "))
            if inny == 1:
                delete_contact()
                break
            elif inny == 2:
                choices()
                break
            elif inny == 3:
                print("\n     Thanks for using the contacts app\n")
                cursor.close()
                break
        except:
            print("Bad input, try again")
            continue
        else:
            print("Bad input, try again")
            continue
    
def number_of_rows():
    num_rows = cursor.execute("SELECT * FROM contacts")
    total_records = len(num_rows.fetchall())
    print(f"\nNumber of contacts {total_records}\n")

def search_contacts():
    search_it = input("\nEnter a name to search (% is wildcard):   ")
    sql = f"SELECT * FROM contacts WHERE name LIKE '{search_it}'"
    cursor.execute(sql)
    rows = cursor.fetchall()
    number_of_rows = 0
    for row in rows:
        number_of_rows += 1
    print(f"\n     Search found {number_of_rows} contacts\n")
    for row in rows:
        print(row)
    print("\n1. Search again")
    print("2. Main Menu")
    print("3. Quit app\n")
    while True:
        try:
            inny = int(input("Please enter 1/2/3  "))
            if inny == 1:
                search_contacts()
                break
            elif inny == 2:
                choices()
                break
            elif inny == 3:
                print("\n     Thanks for using the contacts app\n")
                cursor.close()
                break
        except:
            print("Bad input, try again")
            continue
        else:
            print("Bad input, try again")
            continue

def choices():
    print("\n** Main Menu **")
    print("1. Add new contact")
    print("2. DELETE contact")
    print("3. Display contacts")
    print("4. Search contacts")
    print("5. Quit contacts app\n")
    while True:
        try:
            user_input = int(input("Please choose an option 1-5:  "))
            if user_input == 1:
                add_contact()
                break
            elif user_input == 2:
                delete_contact()
                break
            elif user_input == 3:
                display_contacts()
                break
            elif user_input == 4:
                search_contacts()
                break
            elif user_input == 5:
                print("\n     Thanks for using the contacts app\n")
                cursor.close()
                break
        except:
            print("bad choice :-) please enter 1-5")
            continue

create_table()
print("\n"*25)
print("******************")
print("   Contacts App")
print("******************")
choices()