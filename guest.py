import database


class Guest:
    id = 0

    def __init__(self):
        id_list = database.get_guest_ids()
        if not id_list:
            self.id = 0
            id_list.append(0)
            database.save_guest_ids(id_list)
        else:
            list_len = len(id_list)
            last_id = id_list[list_len - 1]
            next_id = last_id + 1
            self.id = next_id
            id_list.append(next_id)
            database.save_guest_ids(id_list)
        database.save_guest(self)

    def remove(self):
        database.remove_guest(self.id)


# a = Guest()
# b = Guest()
# c = Guest()
