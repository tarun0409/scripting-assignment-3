import pickle
import os


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
        payment_file_name = "db/payment_objects/customer"+str(self.customer_id)+".pickle"
        if os.path.exists(payment_file_name):
            payment_file = open(payment_file_name, "rb")
            payment_list = pickle.load(payment_file)
            payment_file.close()
            os.remove(payment_file_name)
            payment_file = open(payment_file_name, "wb")
            payment_list.append(self)
            pickle.dump(payment_list, payment_file)
            payment_file.close()
        else:
            payment_list = [self]
            payment_file = open(payment_file_name, "wb")
            pickle.dump(payment_list, payment_file)

    @staticmethod
    def remove(customer_id):
        payment_file_name = "db/payment_objects/customer"+str(customer_id)+".pickle"
        if os.path.exists(payment_file_name):
            os.remove(payment_file_name)

# a = Payment(0, "name1", "visa", "1234")
# b = Payment(0, "name2", "master card", "1235")
# c = Payment(1, "name3", "visa", "12300")


Payment.remove(1)
