import sqlite3


def db_connect():
    con = sqlite3.connect('new_db.sqlite')
    cur = con.cursor()

    try:
        cur.execute("""
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            first_name text NOT NULL,
            last_name text NOT NULL);""")
        cur.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name text NOT NULL,
            price real NOT NULL,
            FOREIGN KEY (id) REFERENCES customers(id));""")
        con.commit()
    except sqlite3.Error as error:
        print(error)
    finally:
        if con:
            con.close()


def customer_entry(first_name, last_name):
    f = first_name
    l = last_name

    con = sqlite3.connect('new_db.sqlite')
    cur = con.cursor()

    try:
        customer_entry = """INSERT INTO customers (first_name, last_name) VALUES (?,?);"""
        data_tuple = (f, l)
        cur.execute(customer_entry, data_tuple)
        con.commit()
        print("Data entered.")
        con.close()
    except sqlite3.Error:
        print("Unable to insert data.")
    finally:
        if con:
            con.close()


def product_entry(name, price):

    n = name
    p = price

    con = sqlite3.connect('new_db.sqlite')
    cur = con.cursor()

    try:
        product_entry = """INSERT INTO products (name, price) VALUES (?,?);"""
        data_tuple = (n, p)
        cur.execute(product_entry, data_tuple)
        con.commit()
        print("Data entered.")
        con.close()
    except sqlite3.Error:
        print("Unable to insert data.")
    finally:
        if con:
            con.close()


def query():
    con = sqlite3.connect('new_db.sqlite')
    cur = con.cursor()
    try:
        query = """SELECT * FROM customers;"""
        data = cur.execute(query)





        print("Data Output", data.fetchall())
    except sqlite3.Error:
        print("Unable to select customer.")
    finally:
        if con:
            con.close()


def product_query():
    con = sqlite3.connect("new_db.sqlite")
    cur = con.cursor()
    try:
        x = """SELECT * FROM products;"""
        data = cur.execute(x)
        print("Data Output", data.fetchall())
    except sqlite3.Error:
        print("Unable to select product")
    finally:
        if con:
            con.close()

def inner_join():
    con = sqlite3.connect("new_db.sqlite")
    cur = con.cursor()
    try:
        query = """SELECT first_name, name FROM customers AS a INNER
         JOIN products AS b ON a.id = b.id ORDER BY first_name;"""
        data = cur.execute(query)
        print("Data Output", data.fetchall())
    except sqlite3.Error:
        print("Unable to create adjoined table")
    finally:
        if con:
            con.close()


def update():
    entry = input("Define entry")
    print("What do you want to change to? ")
    choice = input("Provide new entry name:")
    con = sqlite3.connect("new_db.sqlite")
    cur = con.cursor()
    try:
        query = """UPDATE customers SET first_name = (?) where first_name = (?);"""
        data_tuple = (choice, entry)
        data = cur.execute(query, data_tuple)
        con.commit()
        print("Data has been updated!")
    except sqlite3.Error:
        print("Unable to update entry")
    finally:
        if con:
            con.close()


def product_update():
    entry = input("Define entry")
    print("What do you want to change to? ")
    choice = input("Provide new entry name:")
    con = sqlite3.connect("new_db.sqlite")
    cur = con.cursor()
    try:
        query = """UPDATE products SET name = (?) where name = (?);"""
        data_tuple = (choice, entry)
        data = cur.execute(query, data_tuple)
        con.commit()
        print("Data has been updated!")
    except sqlite3.Error:
        print("Unable to update entry")
    finally:
        if con:
            con.close()


def delete_mexico():

    table = input("TABLE (c/p): ")
    entry = input("ENTRY: ")

    con = sqlite3.connect('new_db.sqlite')
    cur = con.cursor()

    try:
        if table == 'c':
            query = f"""DELETE FROM customers WHERE first_name = '{entry}';"""
            cur.execute(query)
        else:
            query = f"""DELETE FROM products WHERE name = '{entry}';"""
            cur.execute(query)
        con.commit()
        print("Entry deleted.")
    except sqlite3.Error:
        print("Unable to delete entry.")
    finally:
        if con:
            con.close()









