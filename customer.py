import database
from payment import Payment
from shipment import Shipment
from cart import Cart
from product import Product


class Customer:
    id = 0
    name = "unknown"
    address = "location unknown"
    phone_number = 100

    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        id_list = database.get_customer_ids()
        if not id_list:
            self.id = 0
            id_list.append(0)
            database.save_customer_ids(id_list)
        else:
            list_len = len(id_list)
            last_id = id_list[list_len - 1]
            next_id = last_id + 1
            self.id = next_id
            id_list.append(next_id)
            database.save_customer_ids(id_list)
        database.save_customer(self)
        database.map_customer_name_to_id(self.name, self.id)

    def remove(self):
        database.remove_customer(self.id)

    def get_id(self):
        return self.id

    def buy_product(self, product_obj, payment_obj, quantity):
        total_price = product_obj.get_price() * quantity
        if payment_obj.get_price() >= total_price:
            shipment_obj = Shipment(self.id, product_obj.get_id(), quantity, payment_obj.get_id())
            database.save_shipment(shipment_obj)
            return True
        return False

    def buy_products_in_bulk(self, product_list, payment_obj):
        total_price = 0
        i = 0
        for prod in product_list:
            total_price += prod.get_price()
            i += 1
        if payment_obj.get_price() >= total_price:
            i = 0
            for prod in product_list:
                shipment_obj = Shipment(self.id, prod.get_id(), 99, payment_obj.get_id())
                database.save_shipment(shipment_obj)
                i += 1
            return True
        return False

    def make_payment(self, price, card_type, card_number):
        payment_obj = Payment(self.id, price, card_type, card_number)
        return payment_obj

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

    def get_products_details(self, product_list):
        results = []
        for product_obj in product_list:
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

    def add_to_cart(self, cart_obj, prod_obj):
        cart_obj.add_product(prod_obj)

    def delete_from_cart(self, cart_obj, prod_obj):
        cart_obj.remove_product(prod_obj)

    def get_products_from_cart(self, cart_obj):
        prods = cart_obj.get_cart_items()
        return prods


