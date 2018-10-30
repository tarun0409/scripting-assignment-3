import database
from customer import Customer
from admin import Admin
from payment import Payment
from cart import Cart
from guest import Guest


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
    prod_price = float(input("Price : "))
    prod_group = input("Group : ")
    prod_subgroup = input("Sub Group : ")
    admin_obj.add_product(prod_name, prod_price, prod_group, prod_subgroup)


def delete_product_menu(admin_obj):
    view_products(admin_obj)
    print()
    del_id = input("Enter the id of the product to be deleted : ")
    admin_obj.delete_product(int(del_id))


def modify_product_menu(admin_obj):
    view_products(admin_obj)
    print()
    mod_id = int(input("Enter the id of product to be modified : "))
    attribute = input("Enter the attribute that has to be modified : ")
    val_string = input("Enter the modified value : ")
    if attribute == "PRICE":
        value = float(val_string)
        admin_obj.modify_product(mod_id, attribute.lower(), value)
    else:
        admin_obj.modify_product(mod_id, attribute.lower(), val_string)


def get_admin_menu(admin_obj):
    print("1. View products")
    print("2. Add products")
    print("3. Delete products")
    print("4. Modify products")
    print("5. Confirm Delivery")
    opt = int(input("Enter the appropriate number : "))
    while opt != 6:
        if opt == 1:
            view_products(admin_obj)
        elif opt == 2:
            add_product_menu(admin_obj)
        elif opt == 3:
            delete_product_menu(admin_obj)
        elif opt == 4:
            modify_product_menu(admin_obj)
        elif opt == 5:
            shipment_id = int(input("Enter the shipment ID : "))
            admin_obj.confirm_delivery(shipment_id)
        print("1. View products")
        print("2. Add products")
        print("3. Delete products")
        print("4. Modify products")
        print("5. Make shipment")
        print("6. Confirm Delivery")
        opt = int(input("Enter the appropriate number : "))


def get_admin_login_menu():
    admin_name = input("Admin Name : ")
    admin_id = database.get_admin_id_from_name(admin_name)
    admin_obj = database.get_admin(admin_id)
    get_admin_menu(admin_obj)


def get_admin_start_menu():
    print("1. Login as admin")
    print("2. Create admin")
    opt = int(input("Choose corresponding number: "))
    if opt == 1:
        get_admin_login_menu()
    elif opt == 2:
        get_admin_create_menu()
    else:
        print("Invalid option")


def get_register_menu():
    customer_name = input("Name : ")
    customer_address = input("Address : ")
    phone_number = input("Phone number : ")
    customer_obj = Customer(customer_name, customer_address, phone_number)
    database.save_customer(customer_obj)


def get_guest_menu():
    guest_obj = Guest()
    print("1. View products")
    print("2. Register")
    print("3. Exit")
    opt = int(input("Enter the corresponding number : "))
    while opt != 3:
        if opt == 1:
            view_products(guest_obj)
        elif opt == 2:
            get_register_menu()
            break
        print("1. View products")
        print("2. Register")
        print("3. Exit")
        opt = int(input("Enter the corresponding number : "))


def buy_product(customer_obj):
    view_products(customer_obj)
    print()
    product_id = int(input("Enter the id of the product to buy : "))
    quantity = int(input("Enter the quantity : "))
    product_obj = database.get_product(product_id)
    price = product_obj.get_price() * quantity
    print("Total price to be paid "+str(price))
    print("Payment details : ")
    card_type = input("Enter card type : ")
    card_num = input("Enter card number : ")
    payment_obj = Payment(customer_obj.get_id(), price, card_type, card_num)
    success = customer_obj.buy_product(product_obj, payment_obj, quantity)
    if success:
        print("Shipment successfully initiated. Payment reference ID = "+str(payment_obj.get_id()))
    else:
        print("Some problem occurred while transaction")


def buy_cart(customer_obj, cart_obj):
    products = cart_obj.get_cart_items()
    total_price = cart_obj.get_total_price()
    print("Total price to be paid " + str(total_price))
    print("Payment details : ")
    card_type = input("Enter card type : ")
    card_num = input("Enter card number : ")
    payment_obj = Payment(customer_obj.get_id(), total_price, card_type, card_num)
    success = customer_obj.buy_products_in_bulk(products, payment_obj)
    if success:
        print("Shipment successfully initiated. Payment reference ID = "+str(payment_obj.get_id()))
    else:
        print("Some problem occurred while transaction")


def view_cart(customer_obj, cart_obj):
    products = customer_obj.get_products_details(cart_obj.get_cart_items())
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


def get_customer_menu(customer_obj, cart_obj):
    view_products(customer_obj)
    print()
    print("1. Buy product")
    print("2. Add product to cart")
    print("3. Delete product from cart")
    print("4. View cart")
    print("5. Buy products in cart")
    print("6. Exit")
    opt = int(input("Enter the appropriate number : "))
    while opt != 6:
        if opt == 1:
            buy_product(customer_obj)
        elif opt == 2:
            product_id = int(input("Enter the ID of the product to add : "))
            prod_obj = database.get_product(product_id)
            customer_obj.add_to_cart(cart_obj, prod_obj)
        elif opt == 3:
            product_id = int(input("Enter the ID of the product to delete : "))
            prod_obj = database.get_product(product_id)
            customer_obj.delete_from_cart(cart_obj, prod_obj)
        elif opt == 4:
            view_cart(customer_obj, cart_obj)
        elif opt == 5:
            buy_cart(customer_obj, cart_obj)
        view_products(customer_obj)
        print()
        print("1. Buy product")
        print("2. Add product to cart")
        print("3. Delete product from cart")
        print("4. View cart")
        print("5. Buy products in cart")
        print("6. Exit")
        opt = int(input("Enter the appropriate number : "))


def customer_login_menu():
    customer_name = input("Name : ")
    customer_id = database.get_customer_id_from_name(customer_name)
    customer_obj = database.get_customer(customer_id)
    cart_obj = Cart()
    get_customer_menu(customer_obj, cart_obj)


def get_first_menu():
    print("How would you like to continue?")
    print("1. Login")
    print("2. Register")
    print("3. Continue as guest")
    print("4. Admin Menu")
    print("5. Exit")
    opt = int(input("Choose the appropriate number: "))
    if opt == 1:
        customer_login_menu()
    elif opt == 2:
        get_register_menu()
    elif opt == 3:
        get_guest_menu()
    elif opt == 4:
        get_admin_start_menu()
    else:
        print("Thank you please visit again")


customer_login_menu()