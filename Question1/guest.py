import database
from customer import Customer
from product import Product


class Guest:
    id = 0

    def __init__(self):
        id_list = database.get_guest_ids()
        if not id_list:
            self.id = 0
            id_list.append(0)
            database.save_guest_ids(id_list)
        else:
            list_len = len(id_list)
            last_id = id_list[list_len - 1]
            next_id = last_id + 1
            self.id = next_id
            id_list.append(next_id)
            database.save_guest_ids(id_list)
        database.save_guest(self)

    def get_all_products_details(self):
        product_ids = database.get_product_ids()
        results = []
        for i in product_ids:
            product_obj = database.get_product(i)
            result_obj = dict()
            result_obj["ID"] = product_obj.get_id()
            result_obj["NAME"] = product_obj.get_name()
            result_obj["PRICE"] = product_obj.get_price()
            result_obj["GROUP"] = product_obj.get_group()
            result_obj["SUBGROUP"] = product_obj.get_subgroup()
            results.append(result_obj)
        return results

    def view_all_products(self):
        product_ids = database.get_product_ids()
        for i in product_ids:
            product_obj = database.get_product(i)
            print(product_obj.get_string())

    def register(self, name, address, ph_no):
        customer_obj = Customer(name, address, ph_no)
        database.save_customer(customer_obj)

    def remove(self):
        database.remove_guest(self.id)


# a = Guest()
# b = Guest()
# c = Guest()
