import pickle
import os


class Admin:
    id = 0
    name = "unknown"

    def __init__(self, name):
        self.name = name
        id_file_name = "db/admin_objects/id_list.pickle"

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

        except IOError:
            self.id = 0
            id_list = [0]
            id_file = open(id_file_name, "wb")
            pickle.dump(id_list, id_file)
            id_file.close()

        self.save_obj()

    def save_obj(self):
        file_name = "db/admin_objects/admin"+str(self.id)+".pickle"
        if os.path.exists(file_name):
            os.remove(file_name)
        p_out = open(file_name, "wb")
        pickle.dump(self, p_out)
        p_out.close()

    @staticmethod
    def get_obj(admin_id):
        file_name = "db/admin_objects/admin"+str(admin_id)+".pickle"
        p_in = open(file_name, "rb")
        new_obj = pickle.load(p_in)
        p_in.close()
        return new_obj

    @staticmethod
    def remove(admin_id):
        id_file_name = "db/admin_objects/id_list.pickle"
        id_file = open(id_file_name, "rb")
        id_list = pickle.load(id_file)
        id_file.close()
        if admin_id in id_list:
            id_list.remove(admin_id)
        admin_file_name = "db/admin_objects/admin" + str(admin_id) + ".pickle"
        if os.path.exists(admin_file_name):
            os.remove(admin_file_name)


# a = Admin("user1")
# b = Admin("user2")
# c = Admin("user3")
# Admin.remove(6)
