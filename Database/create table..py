import sqlite3

# conn=sqlite3.connect('data.db')
# c=conn.cursor()
# c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name Text,age INTEGER,email TEXT)' )
# conn.commit()
# conn.close()


# conn=sqlite3.connect('data.db')
# c=conn.cursor()
# name=(input("enter the name"))
# age=int(input("Enter the age"))
# email=input("enter the email")
# c.execute('INSERT INTO users(name,age,email) VALUES(?,?,?)',(name,age,email))
# conn.commit()
# conn.close()

# conn=sqlite3.connect('data.db')
# c=conn.cursor()
# c.execute('Select * From users')
# rows=c.fetchall()
# conn.close()
# for x,r in enumerate(rows):
#     print(r)

# conn=sqlite3.connect('data.db')
# c=conn.cursor()
# c.execute('UPDATE users SET age=30 WHERE name="aashik"')
# conn.commit()
# conn.close()



conn=sqlite3.connect('data.db')
c=conn.cursor()
c.execute('DELETE FROM users WHERE name="aashik"')
conn.commit()
conn.close()

