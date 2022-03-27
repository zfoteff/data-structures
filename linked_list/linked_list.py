"""
LinkedList data structure implemented in Python
"""


class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0
        
    def insert(self, key, val) -> None:
        node_to_insert = Node(key, val)
        if self.length == 0:
            # List is empty
            self.head = node_to_insert
            self.length += 1
        else:
            node_to_insert.next = self.head

    def insert_at_tail (self, key, val) -> None:
        node_to_insert = Node(key, val)
        if self.length == 0:
            # List is empty
            self.head = node_to_insert
            self.length += 1
        else:
            # List is not empty
            last = self.head
            while last.next is not None:
                last = last.next

            last.set_next(node_to_insert)
            self.length += 1

    def remove_from_end(self):
        node_to_insert = self.head
        if node_to_insert is None:
            # List is empty
            print ("List is empty")
            return

        elif node_to_insert.next is None:
            # List only has one element
            self.head = None
            self.length -= 1
            return

        while node_to_insert.next.next is not None:
            # Traverse to second to last element
            node_to_insert = node_to_insert.next

        node_to_insert.next = None
        self.length -= 1

    def remove_element (self, key):
        cur = self.head
        last = None

        if cur.key == key:
            last = cur.next
            cur = None
            self.head = last
            self.length -= 1
            return

        while cur.next is not None:
            if cur.key == key:
                last.next = cur.next
                cur = None
                self.length -= 1
                return

            last = cur
            cur = cur.next

        print ("Element not found")

    def find (self, key):
        cur = self.head

        while cur is not None:
            if cur.key == key:
                return True

            cur = cur.next

        return False

    def print (self):
        cur = self.head
        print("----------------------------")
        while cur is not None:
            print(""+str(cur.key)+", "+cur.value)
            cur = cur.next

    def size (self):
        return self.length
