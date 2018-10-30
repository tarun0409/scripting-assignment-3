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

    def remove(self):
        database.remove_admin(self.id)

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



# a = Admin("admin1")
# b = Admin("admin2")
# c = Admin("admin3")

a = Admin.get_admin_object(1)
# a.view_all_products()
# a.add_product("nescafe", "110.10", "groceries", "misc")
# a.delete_product(3)
# a.modify_product(0, "price", 50.50)
# a.view_all_products()
# a.make_shipment(1, 2, 3, 4)
# a.make_shipment(2, 3, 4, 5)
# a.make_shipment(4, 5, 6, 7)
# a.confirm_shipment(2)
# a.view_all_shipments()
