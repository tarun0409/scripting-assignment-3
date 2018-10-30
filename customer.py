import database


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


# a = Customer("tarun", "Prithvi apts chennai", 12345)
# b = Customer("shreyas", "203 OBH", 3243)
# c = Customer("sampoo", "adambakkam", 543422)
