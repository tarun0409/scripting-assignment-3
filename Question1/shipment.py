import database


class Shipment:
    id = 0
    customer_id = 0
    product_id = 0
    quantity = 0
    payment_id = 0
    confirmation = False

    def __init__(self, customer_id, product_id, quantity, payment_id):
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.payment_id = payment_id
        id_list = database.get_shipment_ids()
        if not id_list:
            self.id = 0
            id_list.append(0)
            database.save_shipment_ids(id_list)
        else:
            list_len = len(id_list)
            last_id = id_list[list_len - 1]
            next_id = last_id + 1
            self.id = next_id
            id_list.append(next_id)
            database.save_shipment_ids(id_list)
        database.save_shipment(self)

    def remove(self):
        database.remove_shipment(self.id)

    def confirm_delivery(self):
        self.confirmation = True
        database.save_shipment(self)

    def get_string(self):
        ship_string = "shipment_id = "+str(self.id)+"\n"+"confirmation = "+str(self.confirmation)+"\n"
        return ship_string


# s1 = Shipment(0, 1, 2, 3)
# s2 = Shipment(1, 2, 3, 4)
# s3 = Shipment(2, 3, 4, 5)
