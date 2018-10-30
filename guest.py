import pickle
import os


class Guest:
    id = 0

    def __init__(self):
        id_file_name = "db/guest_objects/id_list.pickle"

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
        file_name = "db/guest_objects/guest"+str(self.id)+".pickle"
        if os.path.exists(file_name):
            os.remove(file_name)
        p_out = open(file_name, "wb")
        pickle.dump(self, p_out)
        p_out.close()

    @staticmethod
    def get_obj(guest_id):
        file_name = "db/guest_objects/guest"+str(guest_id)+".pickle"
        p_in = open(file_name, "rb")
        new_obj = pickle.load(p_in)
        p_in.close()
        return new_obj

    @staticmethod
    def remove(guest_id):
        id_file_name = "db/guest_objects/id_list.pickle"
        id_file = open(id_file_name, "rb")
        id_list = pickle.load(id_file)
        id_file.close()
        if guest_id in id_list:
            id_list.remove(guest_id)
        guest_file_name = "db/guest_objects/guest" + str(guest_id) + ".pickle"
        if os.path.exists(guest_file_name):
            os.remove(guest_file_name)


# a = Guest()
# b = Guest()
# c = Guest()
Guest.remove(2)