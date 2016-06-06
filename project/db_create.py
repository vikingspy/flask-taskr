# project/db_create.py

"""sets up and creates the database"""

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    # get a cursor object for operating on db
    c = connection.cursor()
    
    # create database.
    # we need one table, with fields "task_id", "name", "due_date",
    # "priority", and "status". Values of "status" will be boolean,
    # representing open (1) or closed (0).
    c.execute("""CREATE TABLE tasks
            (task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            due_date TEXT NOT NULL, 
            priority INTEGER NOT NULL,
            status INTEGER NOT NULL)""")
    
    # insert dummy data into the table
    c.execute(
              "INSERT INTO tasks \
              (name, due_date, priority, status) \
              VALUES \
              ('Finish this tutorial', '06/25/2016', 10, 1)"
              )
    
    c.execute(
              "INSERT INTO tasks \
              (name, due_date, priority, status) \
              VALUES \
              ('Finish Real Python Course 2', '06/25/2016', 10, 1)"
              )
    