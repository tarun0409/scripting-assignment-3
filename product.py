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

    def remove(self):
        database.remove_product(self.id)


# a = Product("product1", 23.40, "grp1", "sub1")
# b = Product("product2", 34.50, "grp2", "sub1")
# c = Product("product3", 100.00, "grp2", "sub2")

