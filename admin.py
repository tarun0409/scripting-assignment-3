import database
from product import Product
from shipment import Shipment


class Admin:
    id = 0
    name = "unknown"

    def __init__(self, name):
        self.name = name
        id_list = database.get_admin_ids()
        if not id_list:
            self.id = 0
            id_list.append(0)
            database.save_admin_ids(id_list)
        else:
            list_len = len(id_list)
            last_id = id_list[list_len - 1]
            next_id = last_id + 1
            self.id = next_id
            id_list.append(next_id)
            database.save_admin_ids(id_list)
        database.save_admin(self)
        database.map_admin_name_to_id(self.name, self.id)

    def remove(self):
        database.remove_admin(self.id)

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

    def add_product(self, prod_name, prod_price, prod_group, prod_subgroup):
        prod_obj = Product(prod_name, prod_price, prod_group, prod_subgroup)
        database.save_product(prod_obj)

    def delete_product(self, prod_id):
        database.remove_product(prod_id)

    def modify_product(self, prod_id, attribute_name, modified_value):
        prod_obj = database.get_product(prod_id)
        prod_obj.modify_product(attribute_name, modified_value)

    def make_shipment(self, customer_id, product_id, quantity, payment_id):
        shipment_obj = Shipment(customer_id, product_id, quantity, payment_id)
        database.save_shipment(shipment_obj)

    def confirm_delivery(self, shipment_id):
        shipment_obj = database.get_shipment(shipment_id)
        shipment_obj.confirm_delivery()

    def view_all_shipments(self):
        shipment_ids = database.get_shipment_ids()
        for i in shipment_ids:
            shipment_obj = database.get_shipment(i)
            print(shipment_obj.get_string())

    @staticmethod
    def get_admin_object(admin_id):
        return database.get_admin(admin_id)

