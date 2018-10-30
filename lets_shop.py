import database
from customer import Customer
from admin import Admin


def get_admin_create_menu():
    admin_name = input("Admin Name : ")
    admin_obj = Admin(admin_name)
    database.save_admin(admin_obj)


def view_products(obj):
    products = obj.get_all_products_details()
    max_len = 0
    first = True
    prod_keys = []
    for prod in products:
        if first:
            prod_keys = list(prod.keys())
            first = False
        for key in prod:
            if len(key) > max_len:
                max_len = len(str(key))
            if len(str(prod[key])) > max_len:
                max_len = len(str(prod[key]))
    format_string = "{:<"+str(max_len+5)+"}"
    print()
    for key in prod_keys:
        print(format_string.format(key), end="")
    print()
    for prod in products:
        for key in prod:
            value = prod[key]
            print(format_string.format(value), end="")
        print()


def add_product_menu(admin_obj):
    prod_name = input("Name : ")
    prod_price = input("Price : ")
    prod_group = input("Group : ")
    prod_subgroup = input("Sub Group : ")
    admin_obj.add_product(prod_name, prod_price, prod_group, prod_subgroup)


def get_admin_menu(admin_obj):
    print("1. View products")
    print("2. Add products")
    print("3. Delete products")
    print("4. Modify products")
    print("5. Make shipment")
    print("6. Confirm Delivery")


def get_admin_login_menu():
    admin_name = input("Admin Name : ")
    admin_id = database.get_admin_id_from_name(admin_name)
    admin_obj = database.get_admin(admin_id)
    view_products(admin_obj)


def get_admin_start_menu():
    print("1. Login as admin")
    print("2. Create admin")
    opt = input("Choose corresponding number: ")


def get_register_menu():
    customer_name = input("Name : ")
    customer_address = input("Address : ")
    phone_number = input("Phone number : ")
    customer_obj = Customer(customer_name, customer_address, phone_number)
    database.save_customer(customer_obj)


def get_first_menu():
    print("How would you like to continue?")
    print("1. Login")
    print("2. Register")
    print("3. Continue as guest")
    print("4. Admin Menu")
    print("5. Exit")
    opt = input("Choose the appropriate number: ")
    # if opt == 1:
    #     get_login_menu()
    # elif opt == 2:
    #     get_register_menu()
    # elif opt== 3:
    #     get_guest_menu()
    # else:
    #     print("Thank you please visit again")


get_admin_login_menu()