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

    def remove(self):
        database.remove_customer(self.id)

    def buy_product(self, product_obj, payment_obj, quantity):
        total_price = product_obj.get_price() * quantity
        if payment_obj.price() >= total_price:
            shipment_obj = Shipment(self.id, product_obj.get_id(), quantity, payment_obj.get_id())
            database.save_shipment(shipment_obj)
            return True
        return False

    def make_payment(self, price, card_type, card_number):
        payment_obj = Payment(self.id, price, card_type, card_number)
        return payment_obj

    def view_all_products(self):
        product_ids = database.get_product_ids()
        for i in product_ids:
            product_obj = database.get_product(i)
            print(product_obj.get_string())

    def add_to_cart(self, cart_id, product_id):
        cart_obj = database.get_cart(cart_id)
        cart_obj.add_product(product_id)

    def delete_from_cart(self, cart_id, product_id):
        cart_obj = database.get_cart(cart_id)
        cart_obj.remove_product(product_id)

    def view_cart(self, cart_id):
        cart_obj = database.get_cart(cart_id)
        cart_products = cart_obj.get_cart_items()
        for name in cart_products:
            print(name)

