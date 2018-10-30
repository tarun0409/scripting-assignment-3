import pickle
import os


class Product:
    id = 0
    name = "unknown"
    price = 0.0
    group = "new group"
    sub_group = "new_sub_group"

    def __init__(self, name, price, group, sub_group):
        self.name = name
        self.price = price
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

    @staticmethod
    def remove(product_id):
        id_file_name = "db/product_objects/id_list.pickle"
        id_file = open(id_file_name, "rb")
        id_list = pickle.load(id_file)
        id_file.close()
        if product_id in id_list:
            id_list.remove(product_id)
        product_file_name = "db/product_objects/product"+str(product_id)+".pickle"
        if os.path.exists(product_file_name):
            os.remove(product_file_name)

    @staticmethod
    def get_all_products():
        id_file_name = "db/product_objects/id_list.pickle"
        id_file = open(id_file_name, "rb")
        id_list = pickle.load(id_file)
        id_file.close()
        all_products = []
        for i in id_list:
            product_file_name = "db/product_objects/product"+str(i)+".pickle"
            if os.path.exists(product_file_name):
                product_file = open(product_file_name, "rb")
                product_obj = pickle.load(product_file)
                all_products.append(product_obj)
                product_file.close()

        return all_products

    def get_string(self):
        prod_string = "id : "+str(self.id)+"\nname : "+str(self.name)+"\nprice : "+str(self.price)+"\n"
        return prod_string


# a = Product("product1", 23.40, "grp1", "sub1")
# b = Product("product2", 34.50, "grp2", "sub1")
# c = Product("product3", 100.00, "grp2", "sub2")


# Product.remove(1)
all_prods = Product.get_all_products()
for prod in all_prods:
    print(prod.get_string())
