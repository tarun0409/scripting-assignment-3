import pickle
import os


class Customer:
    id = 0
    name = "unknown"
    address = "location unknown"
    phone_number = 100

    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        id_file_name = "db/customer_objects/id_list.pickle"

        try:
            id_file = open(id_file_name, "rb")
            id_list = pickle.load(id_file)
            id_file.close()
            list_len = len(id_list)
            last_id = id_list[list_len-1]
            next_id = last_id + 1
            self.id = next_id
            id_list.append(next_id)
            id_file = open(id_file_name, "wb")
            pickle.dump(id_list, id_file)
            id_file.close()

        except FileNotFoundError:
            self.id = 0
            id_list = [0]
            id_file = open(id_file_name, "wb")
            pickle.dump(id_list, id_file)
            id_file.close()

        self.save_obj()

    def save_obj(self):
        file_name = "db/customer_objects/customer"+str(self.id)+".pickle"
        if os.path.exists(file_name):
            os.remove(file_name)
        p_out = open(file_name, "wb")
        pickle.dump(self, p_out)
        p_out.close()

    @staticmethod
    def get_obj(customer_id):
        file_name = "db/customer_objects/customer"+str(customer_id)+".pickle"
        p_in = open(file_name, "rb")
        new_obj = pickle.load(p_in)
        p_in.close()
        return new_obj


a = Customer("tarun", "Prithvi apts chennai", 12345)
b = Customer("shreyas", "203 OBH", 3243)
c = Customer("sampoo", "adambakkam", 543422)
