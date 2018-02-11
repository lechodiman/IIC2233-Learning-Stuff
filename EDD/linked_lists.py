class Node:

    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d


class LinkedList:

    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.size = 0
        for arg in args:
            self.append(arg)

    def append_left(self, d):
        new_node = Node(d, self.head)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.head = new_node
        self.size += 1

    def append(self, valor):
        if not self.head:
            self.head = Node(valor)
            self.tail = self.head
        else:
            self.tail.next_node = Node(valor)
            self.tail = self.tail.next_node

    def remove(self, d):
        this_node = self.head
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.head = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, d):
        this_node = self.head
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

    def __in__(self, valor):
        for elemento in self:
            if elemento == valor:
                return True
        return False

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.get_next()

    def __repr__(self):
        node = self.head
        s = "["
        if node:
            s += str(node.data) + ", "
        else:
            return "[]"
        while node.next_node:
            node = node.get_next()
            s += str(node.data) + ", "
        return s.strip(", ") + "]"

    def __getitem__(self, index):
        node = self.head
        for i in range(index):
            if node:
                node = node.next_node
            else:
                raise IndexError
        if not node:
            raise IndexError
        else:
            return node.data

    def clear(self):
        self = LinkedList()

    def count(self, valor):
        contador = 0
        for elemento in self:
            if elemento == valor:
                contador += 1
        return contador


myList = LinkedList(5, 8, 12)
# myList.add(5)
# myList.add(8)
# myList.add(12)
myList.append_left(5)
myList.append_left(8)
myList.append_left(12)
print(myList)
print(myList[1])
myList.remove(8)
print(myList[1])
print(myList.count(12))
print(myList.find(12))
