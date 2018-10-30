import database
from product import Product


class Cart:
    id = 0
    number_of_products = 0
    products = []
    total_price = 0.0

    def __init__(self):
        id_list = database.get_cart_ids()
        if not id_list:
            self.id = 0
            id_list.append(0)
            database.save_cart_ids(id_list)
        else:
            list_len = len(id_list)
            last_id = id_list[list_len - 1]
            next_id = last_id + 1
            self.id = next_id
            id_list.append(next_id)
            database.save_cart_ids(id_list)
        database.save_cart(self)

    def remove(self):
        database.remove_cart(self.id)

    def get_total_price(self):
        return self.total_price

    def add_product(self, product_obj):
        if product_obj not in self.products:
            self.products.append(product_obj)
            self.number_of_products += 1
            self.total_price += product_obj.get_price()
            database.save_cart(self)

    def remove_product(self, product_obj):
        if product_obj in self.products:
            self.products.remove(product_obj)
            self.number_of_products -= 1
            self.total_price -= product_obj.get_price()
            database.save_cart(self)

    def get_cart_items(self):
        return self.products


