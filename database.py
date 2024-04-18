import sqlite3 as sq
from typing import List

conn = sq.connect("phonebook.db")

database = conn.cursor()
# Phone_Num INTEGER/
def create_table():
    database.execute(f"CREATE TABLE {table_name}(Name TEXT, phoneNum INTERGER)")
    print("Data Table Create Succesfully>>!!!")
    print("")
    
def upload(*arg: List, **kwargs):
    if "Name" and "PhoneNum" in kwargs:
        database.execute("INSERT INTO phone_book VALUES (Name, PhoneNum)")
        print(f"{kwargs['Name']} and {kwargs['PhoneNum']}...Were upploaded succsesfully!")

    try:
        if type(arg) == List:
            database.executemany("INSERT INTO phone_book VALUES (?, ?)", arg)
            print(f"{arg} was uploaded succesfull!!")
    except ValueError:
        print("improper ARG passed in upload func>>>!!! it should be a list...")
        
    
def datafetcher(index=False, *num):
    database.execute("SELECT * FROM phone_book")
    if index is False:
        return database.fetchall()
    else:
        print(database.fetchall()[num])

    print("DataFetched Succesfully....:)")
        
try:
    conn.commit()
    conn.close()

    print("==================================")
    print("DataBase is functioning succesfuly...")
except SyntaxError:
    print(SyntaxError)