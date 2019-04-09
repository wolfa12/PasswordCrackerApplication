#tutorial from http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/

import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return rows: all of the password words
    """

    #CHANGE TASKS!!! NOT CORRECT TABLE##
    cur = conn.cursor()
    cur.execute("SELECT * FROM passwords")
 
    rows = cur.fetchall()

def combine_dictionary(rows):
    """
    Combine dictionary words with the intention user applied two words together  
    :param rows: all of the password words
    :return #######
    """
    combo_password = []

    for password in rows:
        for password_next in rows: ##Need a way to set this to start at second password
            new_password = password + password_next
            combo_password.append(new_password)

    return combo_password

def replace_certain_letters(rows):
    for password in rows:
        if 's' in password:
            password.replace('s', '$')

def main():

    #CHANGE DATABASE !!!!
    database = "C:\\sqlite\db\pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        select_all_tasks(conn)
 
 
if __name__ == '__main__':
    main()
