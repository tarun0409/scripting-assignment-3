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
        payments = database.get_payments(customer_id)
        payments.append(self)
        database.save_payments(self.customer_id, payments)

    def remove(self):
        database.remove_payments(self.customer_id)


# a = Payment(0, "name1", "visa", "1234")
# b = Payment(0, "name2", "master card", "1235")
# c = Payment(1, "name3", "visa", "12300")

