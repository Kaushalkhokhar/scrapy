import sqlite3

constant = sqlite3.connect('quotes.db')

curser = constant.cursor()

# to create database only executed once. 
'''curser.execute("""create table quotes_tb(
                text text,
                authers text,
                tag text
                )""")'''

curser.execute("""insert into quotes_tb value(
    
)""")

constant.commit()
constant.close()