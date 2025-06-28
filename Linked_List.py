class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insertatbegin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def insertatend(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def insertatposition(self, data,position):
        node = Node(data)
        if position < 0:
            print("Invalid position")
            return
        if position == 0:
            node.next = self.head
            self.head = node
            return

        temp = self.head
        c=1
        while temp != None and c < position-1:
            temp = temp.next
            c+=1
        node.next=temp.next
        temp.next=node

    def display(self):
        if self.head ==None:
            print("List is empty")
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def deleteatbegin(self):
        if self.head == None:
            print("List is empty")
            return None
        deleted_node=self.head
        self.head = self.head.next
        return deleted_node

    def deleteatend(self):
        if self.head == None:
            print("List is empty")
            return
        temp = self.head
        while temp.next.next != None:
            temp=temp.next
        deleted_node=temp.next
        temp.next = None
        return deleted_node

    def deleteatposition(self,position):
        if self.head == None:
            print("List is empty")
            return None

        if position == 0:
            deleted_node=self.head
            self.head = self.head.next
            return deleted_node

        temp = self.head
        c=1
        while temp != None and c < position-1:
            temp = temp.next
            c+=1
        deleted_node=temp
        temp.next = temp.next.next
        return deleted_node

def main():
    ll=LinkedList()

    ll.insertatbegin(5)
    ll.insertatbegin(6)
    ll.insertatbegin(7)
    ll.insertatbegin(8)
    ll.insertatbegin(9)
    ll.insertatend(10)
    ll.insertatposition(33,3)
    print("elements in list")
    ll.display()
    print("delete at beginning")
    ll.deleteatbegin()
    ll.display()
    print("delete at position 3")
    ll.deleteatposition(3)
    ll.display()
    print("delete at end")
    ll.deleteatend()
    ll.display()

if __name__ == '__main__':
    main()