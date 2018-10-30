import pickle
import os


class Product:
    id = 0
    name = "unknown"
    group = "new group"
    sub_group = "new_sub_group"

    def __init__(self, name, group, sub_group):
        self.name = name
        self.group = group
        self.sub_group = sub_group
        id_file_name = "db/product_objects/id_list.pickle"

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
        file_name = "db/product_objects/product"+str(self.id)+".pickle"
        if os.path.exists(file_name):
            os.remove(file_name)
        p_out = open(file_name, "wb")
        pickle.dump(self, p_out)
        p_out.close()

    @staticmethod
    def get_obj(product_id):
        file_name = "db/product_objects/product"+str(product_id)+".pickle"
        p_in = open(file_name, "rb")
        new_obj = pickle.load(p_in)
        p_in.close()
        return new_obj


a = Product("product1", "grp1", "sub1")
b = Product("product2", "grp2", "sub1")
c = Product("product3", "grp2", "sub2")
