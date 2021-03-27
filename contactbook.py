import sqlite3

# connection = sqlite3.connect("contacts.db")
connection = sqlite3.connect("contacts_v2.db")
cursor = connection.cursor()

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)")

def create_table_2():
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts_v2(id INTEGER PRIMARY KEY, name TEXT, phone INTEGER, email TEXT)")

def add_contact():
    #################################################################
    # AUTO CAPITALIZE NAME FIRST LETTER
    #################################################################
    name = input("\nEnter name:  ")
    print("Name successfully entered")
    number = input("\nEnter phone number:  ")
    print("Phone number successfully entered")
    email = input("\nEnter email address:  ")
    print("Email address successfully entered")
    # cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, number, email))
    cursor.execute("INSERT INTO contacts_v2 (name, phone, email) VALUES (?, ?, ?)", (name, number, email))
    print(f"\n     {connection.total_changes} new record added for {name}")
    #################################################################
    # CHECK THIS BECAUSE IT INCREMENTS EVERY CHANGE, e.g. ADD/DELETE ETC
    #################################################################
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
    # rows = cursor.execute("SELECT name, phone, email FROM contacts").fetchall()
    # rows = cursor.execute("SELECT * FROM contacts").fetchall()
    # rows = cursor.execute("SELECT * FROM contacts ORDER BY name").fetchall()
    # rows = cursor.execute("SELECT name, phone, email FROM contacts_v2").fetchall()
    rows = cursor.execute("SELECT * FROM contacts_v2 ORDER BY name")
    print("\n"*25)
    # for row in rows:
    #     if row == None:
    #         print("no contacts")
    #     else:
    #         print(row)

    # if rows == None:
    #     print("there are currently no contacts")
    # else:
    #     for row in rows:
    #         print(row)

    for row in rows:
        print(row)
    number_of_rows()
    choices()

def delete_contact():
    # num_rows = cursor.execute("SELECT * FROM contacts")
    num_rows = cursor.execute("SELECT * FROM contacts_v2")
    total_records = len(num_rows.fetchall())
    total_number_check = total_records

    name = input("Please enter name of contact to delete:  ")

    # search_it = f"SELECT * FROM contacts WHERE name LIKE '{name}'"
    search_it = f"SELECT * FROM contacts_v2 WHERE name LIKE '{name}'"
    cursor.execute(search_it)
    rows = cursor.fetchall()
    number_of = 0
    for row in rows:
        number_of += 1
    print(f"\n     Found {number_of} match(es)\n")
    for row in rows:
        print(row)

    #################################################################
    # FOUND THIS NAME - ARE YO SURE YOU WANT TO DELETE?
    # FOUND THREE MATCHES - WHICH DO YOU WANT TO DELETE? TYPE EXACTLY
    #################################################################
    
    name2 = input("\nPlease type name fully to confirm delete:  ")
    
    # sql = f"DELETE FROM contacts WHERE name LIKE '{name2}'"
    sql = f"DELETE FROM contacts_v2 WHERE name LIKE '{name2}'"
    cursor.execute(sql)
    connection.commit()

    # num_rows = cursor.execute("SELECT * FROM contacts")
    num_rows = cursor.execute("SELECT * FROM contacts_v2")
    total_records = len(num_rows.fetchall())
    if total_number_check > total_records:
        print(f"\n     {name2} has been deleted from contacts")
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
    # num_rows = cursor.execute("SELECT * FROM contacts")
    num_rows = cursor.execute("SELECT * FROM contacts_v2")
    total_records = len(num_rows.fetchall())
    print(f"\nNumber of contacts {total_records}\n")

def search_contacts():
    search_it = input("\nEnter a name to search (% is wildcard):   ")
    # sql = f"SELECT * FROM contacts WHERE name LIKE '{search_it}'"
    sql = f"SELECT * FROM contacts_v2 WHERE name LIKE '{search_it}'"
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
            # elif user_input == 7:
            #     rowid()
            #     break
            
        except:
            print("bad choice :-) please enter 1-5")
            continue

create_table_2()
print("\n"*25)
print("******************")
print("   Contacts App")
print("******************")
choices()

# LOOK INTO THE ROWID AS PRIMARY KEY, WHERE IT'S CREATED AUTOMATICALLY