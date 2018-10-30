import database


class Admin:
    id = 0
    name = "unknown"

    def __init__(self, name):
        self.name = name
        id_list = database.get_admin_ids()
        if not id_list:
            self.id = 0
            id_list.append(0)
            database.save_admin_ids(id_list)
        else:
            list_len = len(id_list)
            last_id = id_list[list_len - 1]
            next_id = last_id + 1
            self.id = next_id
            id_list.append(next_id)
            database.save_admin_ids(id_list)
        database.save_admin(self)

    def remove(self):
        database.remove_admin(self.id)


# a = Admin("admin1")
# b = Admin("admin2")
# c = Admin("admin3")
