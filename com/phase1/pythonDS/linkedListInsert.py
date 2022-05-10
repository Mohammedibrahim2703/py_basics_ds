class Node:
 def __init__(self,data):
     self.data=data
     self.next=None


class linkedList:
    def __init__(self):
        print("Inside head method")
        self.head = None

    def push(self, new_value):
        print("Push method")
        newNode = Node(new_value)
        newNode.next = self.head
        self.head = newNode
        print("Push method" ,newNode)
    def insertAt(self, prev_node, new_value):
        if prev_node is Node:
            print("Previous node is empty")
        newNode = Node(new_value)
        newNode.next = prev_node.next
        prev_node.next = newNode

    def append(self, new_value):
        new_value = Node(new_value)
        if self.head is None:
            self.head = new_value
            return
        last = self.head
        while (last.next):
            last = last.next
            last.next = new_value

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next






if __name__ == "__main__":
  print("Inside Main method")
  llist = linkedList()
  print(llist.append(3))
  llist.push(7)
  llist.printList()