from db_utils import db_connect, customer_entry, product_entry, query, product_query, inner_join, update, product_update,delete_mexico

db_connect()


def customer_info():
    print("Do you want to compare tables?")
    choice = input()
    if choice == 'y':
        inner_join()
    print("Do you want to see all the users?")
    choice = input()
    if choice == 'y':
        query()
    print("Do you want to update entry?")
    choice = input()
    if choice == 'y':
        print("Specify entry")
        entry = input()
        update(entry)
    elif choice == 'q':
        quit()

    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    customer_entry(first_name, last_name)


def product_info():
    print("Do you want to see all the products?")
    choice = input()
    if choice == 'y':
        product_query()
    print("Do you want to update entry?")
    choice = input()
    if choice == 'y':
        print("Specify entry")
        entry = input()
        product_update(entry)
    elif choice == 'q':
        quit()

    name = input("Product: ")
    price = input("Price: ")

    product_entry(name, price)


def menu():
    print("Welcome To Kyrat")
    print("Please choose an option below to get started:")
    print("\1. Show Users")
    print("\2. Show Products")
    print("\3. Compare Tables")
    print("\4. Update Customer Entry ")
    print("\5. Update Product Entry")
    print("\6. Delete Entry")

    choice = int(input())
    if choice == 1:
        query()
    elif choice == 2:
        product_query()
    elif choice == 3:
        inner_join()
    elif choice == 4:
        update()
    elif choice == 5:
        product_update()
    elif choice == 6:
        delete_mexico()
    else:
        print("Invalid Input!")

menu()
# customer_info()
# product_info()


