import pickle
import os


def save_admin(admin_obj):
    file_name = "db/admin_objects/admin" + str(admin_obj.id) + ".pickle"
    if os.path.exists(file_name):
        os.remove(file_name)
    p_out = open(file_name, "wb")
    pickle.dump(admin_obj, p_out)
    p_out.close()


def get_admin(admin_id):
    file_name = "db/admin_objects/admin" + str(admin_id) + ".pickle"
    p_in = open(file_name, "rb")
    new_obj = pickle.load(p_in)
    p_in.close()
    return new_obj


def get_admin_ids():
    id_file_name = "db/admin_objects/id_list.pickle"
    id_list = []
    if os.path.exists(id_file_name):
        id_file = open(id_file_name, "rb")
        id_list = pickle.load(id_file)
        id_file.close()
        return id_list
    return id_list


def save_admin_ids(id_list):
    id_file_name = "db/admin_objects/id_list.pickle"
    id_file = open(id_file_name, "wb")
    pickle.dump(id_list, id_file)
    id_file.close()


def remove_admin(admin_id):
    id_list = get_admin_ids()
    id_list.remove(admin_id)
    save_admin_ids(id_list)
    file_name = "db/admin_objects/admin" + str(admin_id) + ".pickle"
    if os.path.exists(file_name):
        os.remove(file_name)


def save_product(product_obj):
    file_name = "db/product_objects/product" + str(product_obj.id) + ".pickle"
    if os.path.exists(file_name):
        os.remove(file_name)
    p_out = open(file_name, "wb")
    pickle.dump(product_obj, p_out)
    p_out.close()


def get_product(product_id):
    file_name = "db/product_objects/product" + str(product_id) + ".pickle"
    p_in = open(file_name, "rb")
    new_obj = pickle.load(p_in)
    p_in.close()
    return new_obj


def get_product_ids():
    id_file_name = "db/product_objects/id_list.pickle"
    id_list = []
    if os.path.exists(id_file_name):
        id_file = open(id_file_name, "rb")
        id_list = pickle.load(id_file)
        id_file.close()
        return id_list
    return id_list


def save_product_ids(id_list):
    id_file_name = "db/product_objects/id_list.pickle"
    id_file = open(id_file_name, "wb")
    pickle.dump(id_list, id_file)
    id_file.close()


def remove_product(product_id):
    id_list = get_product_ids()
    id_list.remove(product_id)
    save_product_ids(id_list)
    file_name = "db/cart_objects/cart" + str(product_id) + ".pickle"
    if os.path.exists(file_name):
        os.remove(file_name)


def save_cart(cart_obj):
    file_name = "db/cart_objects/cart" + str(cart_obj.id) + ".pickle"
    if os.path.exists(file_name):
        os.remove(file_name)
    p_out = open(file_name, "wb")
    pickle.dump(cart_obj, p_out)
    p_out.close()


def get_cart(cart_id):
    file_name = "db/cart_objects/cart" + str(cart_id) + ".pickle"
    p_in = open(file_name, "rb")
    new_obj = pickle.load(p_in)
    p_in.close()
    return new_obj


def get_cart_ids():
    id_file_name = "db/cart_objects/id_list.pickle"
    id_list = []
    if os.path.exists(id_file_name):
        id_file = open(id_file_name, "rb")
        id_list = pickle.load(id_file)
        id_file.close()
        return id_list
    return id_list


def save_cart_ids(id_list):
    id_file_name = "db/cart_objects/id_list.pickle"
    id_file = open(id_file_name, "wb")
    pickle.dump(id_list, id_file)
    id_file.close()


def remove_cart(cart_id):
    id_list = get_cart_ids()
    id_list.remove(cart_id)
    save_cart_ids(id_list)
    file_name = "db/cart_objects/cart" + str(cart_id) + ".pickle"
    if os.path.exists(file_name):
        os.remove(file_name)


def save_customer(customer_obj):
    file_name = "db/customer_objects/customer" + str(customer_obj.id) + ".pickle"
    if os.path.exists(file_name):
        os.remove(file_name)
    p_out = open(file_name, "wb")
    pickle.dump(customer_obj, p_out)
    p_out.close()


def get_customer(customer_id):
    file_name = "db/customer_objects/customer" + str(customer_id) + ".pickle"
    p_in = open(file_name, "rb")
    new_obj = pickle.load(p_in)
    p_in.close()
    return new_obj


def get_customer_ids():
    id_file_name = "db/customer_objects/id_list.pickle"
    id_list = []
    if os.path.exists(id_file_name):
        id_file = open(id_file_name, "rb")
        id_list = pickle.load(id_file)
        id_file.close()
        return id_list
    return id_list


def save_customer_ids(id_list):
    id_file_name = "db/customer_objects/id_list.pickle"
    id_file = open(id_file_name, "wb")
    pickle.dump(id_list, id_file)
    id_file.close()


def remove_customer(customer_id):
    id_list = get_customer_ids()
    id_list.remove(customer_id)
    save_customer_ids(id_list)
    file_name = "db/customer_objects/customer" + str(customer_id) + ".pickle"
    if os.path.exists(file_name):
        os.remove(file_name)


def save_guest(guest_obj):
    file_name = "db/guest_objects/guest" + str(guest_obj.id) + ".pickle"
    if os.path.exists(file_name):
        os.remove(file_name)
    p_out = open(file_name, "wb")
    pickle.dump(guest_obj, p_out)
    p_out.close()


def get_guest(guest_id):
    file_name = "db/guest_objects/guest" + str(guest_id) + ".pickle"
    p_in = open(file_name, "rb")
    new_obj = pickle.load(p_in)
    p_in.close()
    return new_obj


def get_guest_ids():
    id_file_name = "db/guest_objects/id_list.pickle"
    id_list = []
    if os.path.exists(id_file_name):
        id_file = open(id_file_name, "rb")
        id_list = pickle.load(id_file)
        id_file.close()
        return id_list
    return id_list


def save_guest_ids(id_list):
    id_file_name = "db/guest_objects/id_list.pickle"
    id_file = open(id_file_name, "wb")
    pickle.dump(id_list, id_file)
    id_file.close()


def remove_guest(guest_id):
    id_list = get_guest_ids()
    id_list.remove(guest_id)
    save_guest_ids(id_list)
    file_name = "db/guest_objects/guest" + str(guest_id) + ".pickle"
    if os.path.exists(file_name):
        os.remove(file_name)


def save_payments(customer_id, payment_obj):
    file_name = "db/payment_objects/guest" + str(customer_id) + ".pickle"
    if os.path.exists(file_name):
        os.remove(file_name)
    p_out = open(file_name, "wb")
    pickle.dump(payment_obj, p_out)
    p_out.close()


def get_payments(customer_id):
    file_name = "db/payment_objects/customer" + str(customer_id) + ".pickle"
    if not os.path.exists(file_name):
        return []
    p_in = open(file_name, "rb")
    new_obj = pickle.load(p_in)
    p_in.close()
    return new_obj


def remove_payments(customer_id):
    file_name = "db/payment_objects/customer" + str(customer_id) + ".pickle"
    if os.path.exists(file_name):
        os.remove(file_name)
