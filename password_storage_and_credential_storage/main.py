#Project Ark
#Vedant Dahake 2020BME036
#Saket Gondane 2020BME047
#Prem Singh Bayas 2020BME027

import random
import array
import sqlite3
import time

from sqlite3 import Error
def sql_connection():
   try:
     conn = sqlite3.connect(r"H:\Btech\Third Year\6th Sem\pythonsqlite.db")
     return conn
   except Error:
     print(Error)
def sql_table(conn):
   cursor = conn.cursor()
   cursor.execute("CREATE TABLE IF NOT EXISTS Vault(website_name char(20) Not NULL,user_name char(40) Not Null,password char(20) Not Null)")
   cursor.execute('''CREATE UNIQUE INDEX IF NOT EXISTS idx_website_name ON Vault (website_name)''')
   conn.commit()
conn = sql_connection()
sql_table(conn)
cursor = conn.cursor()

while True:
    print('\nGreetings, I am Noah. Welcome to Ark.\nHow may I help you?')
    print('1. Generate a random password.')
    print('2. Save credentials.')
    print('3. Show credentials.')
    print('4. Edit credentials.')
    print('5. Delete credentials.')
    print('6. Exit program.')
    opt = int(input())

    #generating password
    if opt == 1:
        name = input('Please enter name of the website/application: ')
        usr_name = input('Please enter your username: ')
        n = int(input('Please enter the length of password you would require: '))
        characs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z',
            '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
        if n >= 5 and n <= 18:
            rand_password = ''
            for i in range(n):
                temp_pass = random.choice(characs)
                rand_password = rand_password + temp_pass
            print(rand_password)
            password = rand_password
            cursor.execute("""INSERT INTO Vault VALUES (?,?,?)""", 
                (name, usr_name, rand_password))
            conn.commit()
            print('New credentials have been saved successfully.')
            time.sleep(2)
        else:
            print('Passwords are usually 5 to 18 characters long. So, please enter a number between 5 and 18.')
            time.sleep(2)

    #storing credentials
    elif opt == 2:
        try:
            name = input('Please enter name of the website/application: ') 
            usr_name = input('Please enter your username: ')
            usr_password = input('Please enter your password: ')
            cursor.execute("""INSERT INTO Vault VALUES (?,?,?)""", 
                (name, usr_name, usr_password))
            conn.commit()
            print('Thank You.Your credentials have been successfully saved.')

        except:
            print('Sorry credentials with', name, 'already exist. Please try again.')
        time.sleep(2)

    #showing credentials
    elif opt == 3:
        temp_name = str(input('Please enter name of the required website/application: '))
        cursor.execute("SELECT * FROM Vault WHERE website_name = '" + temp_name + "'")
        table = cursor.fetchone()
        for row in table:
            print(row)
            time.sleep(0.5)

    #updating credentials
    elif opt == 4:
        usr_inp = str(input('Please enter name of the required website/application you wish to update: '))
        up_inp = str(input('What would you like to update? Website, username or password: '))
        new_inp = str(input('Please enter the new value: '))
        cursor.execute("SELECT * FROM Vault WHERE website_name = '" + usr_inp + "'")
        if up_inp.lower() == 'website':
            cursor.execute("UPDATE Vault SET website_name = '" + new_inp + "'")
            print('Cheers, your data has been saved successfully.')
        elif up_inp.lower() == 'username':
            cursor.execute("UPDATE Vault SET user_name = '" + new_inp + "'")
            print('Cheers, your data has been saved successfully.')
        elif up_inp.lower() == 'password':
            cursor.execute("UPDATE Vault SET password = '" + new_inp + "'")
            print('Cheers, your data has been saved successfully.')
        else:
            print('Sorry, this data does not exist. Please try again.')
        time.sleep(2)
        conn.commit()

    #deleting credentials
    elif opt == 5:
        usr_inp = str(input('Please enter name of the required website/application you wish to delete: '))
        cursor.execute("DELETE FROM Vault WHERE website_name = '" + usr_inp + "'")
        print('Your credentials have been successfully deleted.')
        conn.commit()
        time.sleep(2)

    #exiting the program
    elif opt == 6:
        print('See you later. Thank you for now.')
        time.sleep(2)
        if (conn):
             conn.close()
        break

    else:
        print('Invalid input. Please try again.')

        time.sleep(2)
