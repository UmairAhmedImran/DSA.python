class Node:
    def __init__(self,init_data):
        self.data = init_data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,new_data):
        self.data = new_data

    def setNext(self,new_next):
        self.next = new_next


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head == None:
            print("True")
        else:
            print("Flase")

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        print(f"Size of list is {count}")

### print("Name: Navdeep    Student_id: 21582009")

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        print(found)


    def print_list(self):
        node = self.head
        while node is not None:
            print(node.getData(), end=" ")
            node = node.getNext()\
            
print("Name: Navdeep    Student_id: 21582009")
mylist = UnorderedList()
mylist.add(2)
mylist.add(1)
mylist.add(5)
mylist.add(8)
mylist.add(2)
mylist.add(0)
mylist.add(0)
mylist.add(9)
# print("Displaying the content of the list using print_list function")
# mylist.print_list()
# print("Testing the is_empty function")
# mylist.isEmpty()
# print("Testing the size function")
# mylist.size()

number = int(input("Enter a number to search in the list: "))

mylist.search(number)