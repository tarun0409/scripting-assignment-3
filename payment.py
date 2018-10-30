import database


class Payment:
    customer_id = 0
    name = "unknown"
    card_type = "visa"
    cart_number = "1234 4556 3213 0909"

    def __init__(self, customer_id, name, card_type, card_number):
        self.customer_id = customer_id
        self.name = name
        self.card_type = card_type
        self.cart_number = card_number
        id_list = database.get_payment_ids()
        if not id_list:
            self.id = 0
            id_list.append(0)
            database.save_payment_ids(id_list)
        else:
            list_len = len(id_list)
            last_id = id_list[list_len - 1]
            next_id = last_id + 1
            self.id = next_id
            id_list.append(next_id)
            database.save_payment_ids(id_list)
        database.save_payment(self)

    def remove(self):
        database.remove_payment(self.id)


a = Payment(0, "name1", "visa", "1234")
b = Payment(0, "name2", "master card", "1235")
c = Payment(1, "name3", "visa", "12300")

