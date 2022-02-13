
class List(object):
    class LElem(object):
        id = 0
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
            self.id = List.LElem.id + 1
            List.LElem.id += 1 

        def append(self, knode):
            if self.next is not None:
                self.next.append(knode)
            else:
                self.next = knode

        def __repr__(self) -> str:
            return self.data

        def Print(self):
            print("ID: ", self.id, " Data: ", self.data)
            if self.next is not None:
                self.next.Print()
            else:
                return

    head = None
    last = None

    def append(self, data):
        if self.head == None:
            self.head = self.LElem(data)
            return
        self.head.append(self.LElem(data))

    def Print(self):
        self.head.Print()

    def __repr__(self) -> LElem:
        return self.head.__repr__()

l1 = List()
l1.append("eins")
l1.append("zwei")
l1.append("drei")
l1.Print()
print(l1.__repr__())