import database


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
        id_list = database.get_product_ids()
        if not id_list:
            self.id = 0
            id_list.append(0)
            database.save_product_ids(id_list)
        else:
            list_len = len(id_list)
            last_id = id_list[list_len - 1]
            next_id = last_id + 1
            self.id = next_id
            id_list.append(next_id)
            database.save_product_ids(id_list)
        database.save_product(self)

    def modify_product(self, attribute_name, modified_value):
        print("reached modify")
        if attribute_name == "name":
            self.name = modified_value
        elif attribute_name == "price":
            self.price = modified_value
        elif attribute_name == "group":
            self.price = modified_value
        elif attribute_name == "subgroup":
            self.sub_group = modified_value
        database.save_product(self)

    def remove(self):
        database.remove_product(self.id)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_group(self):
        return self.group

    def get_subgroup(self):
        return self.sub_group

    def get_string(self):
        prod_str = "id = "+str(self.id)+"\nname = "+self.name+"\nprice = "+str(self.price)+"\n"
        return prod_str



# a = Product("product1", 23.40, "grp1", "sub1")
# b = Product("product2", 34.50, "grp2", "sub1")
# c = Product("product3", 100.00, "grp2", "sub2")

