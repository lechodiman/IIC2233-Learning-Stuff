import pickle
from linked_lists import LinkedList
# example_dict = {1: "6", 2: "2", 3: "f"}
#
# pickle_out = open('dict.pickle', 'wb')
# pickle.dump(example_dict, pickle_out)
# pickle_out.close()

pickle_in = open('dict.pickle', 'rb')
example_dict = pickle.load(pickle_in)
pickle_in.close()

my_list = LinkedList(2, 3, 4, 5, "s", example_dict)

with open('my_list.pickle', 'wb') as wf:
    pickle.dump(my_list, wf)
