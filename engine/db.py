import sqlite3
import csv

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

# write a query to create a table
query  = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# one note included
# query = "INSERT INTO sys_command VALUES (null,'one note','c:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\OneNote 2013.lnk')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'ms word','c:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013.lnk')"
# cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null,'excel','c:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Excel 2013.lnk')"
# cursor.execute(query)

# vs code included
# query = "INSERT INTO sys_command VALUES (null,'vs code','c:\\Users\\USER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk')"
# cursor.execute(query)

# spyder included
# query = "INSERT INTO sys_command VALUES (null,'spyder','c:\\Users\\USER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Spyder (anaconda3).lnk')"
# cursor.execute(query)
# conn.commit()

query  = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), urls VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'youtube','www.youtube.com')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'figma','https://www.figma.com/files/recents-and-sharing/recently-viewed?fuid=1219362679571028097')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'canva','https://www.canva.com/')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'netflix','https://www.netflix.com/login')"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'college','https://makaut1.ucanapply.com/smartexam/public/')"
# cursor.execute(query)
# conn.commit() 

'''..........whatsApp automation..........'''
# Create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# Export Google Contacts

# Import CSV file into database

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 31]

# Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# conn.commit()
# conn.close()


#                  --------Insert Single contacts (Optional)--------

# query = "INSERT INTO contacts VALUES (null,'pawan', '1234567890')"
# cursor.execute(query)
# conn.commit()


#                       ------Search Contacts from database-----------

# query = 'maa'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])



#                           ------ Adding email of contacts ---------
cursor.execute('''CREATE TABLE IF NOT EXISTS email_contacts (id integer primary key, name VARCHAR(200), email VARCHAR(255) NULL)''')
# query = "INSERT INTO email_contacts VALUES (null,'joyitree','joyitree2022@gmail.com')"
# cursor.execute(query)
# conn.commit()

# query = "INSERT INTO email_contacts VALUES (null,'maa','joyitree2022@gmail.com')"
# cursor.execute(query)
# conn.commit()
