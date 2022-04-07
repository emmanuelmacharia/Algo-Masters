"""
A MODULE THAT CREATES LINKED LISTS; AND THEIR METHODS
IT INCLUDES CREATING A SINGLY LINKED LIST AND DOUBLY LINKED LIST

"""


from cmath import isnan


class Node:
    '''
    class that contains the nodes in a linked list. 
    a node can be anything so long as it's got the data and next to the next node in the list
    '''
    def __init__(self, data):
        self.data = data
        self.next = None

    
class SinglyLinkedList:
    """
    class that contains the methods for the singly linked list.
    These methods are: Search/find, Add, Remove and  Reverse
    It also contains some other helper methods like printList, iterate and isEmpty
    """
    def __init__(self):
        self.head = None


    def isEmpty(self) -> bool:
        '''Checks whether the linked list is empty or not'''
        if self.head is None:
            return True
        return False

    def print_list(self):
        '''Prints out all the elements in the linked list'''
        l_list = []
        print_val = self.head
        while print_val:
            l_list.append(f'{print_val.data} -> ')
            print_val = print_val.next
        return l_list


    def iterate(self):
        '''Iterates the entire linked list; returns the tail node'''
        if self.isEmpty():
            return
        node = self.head
        while node.next:
            print(node.data)
            node = node.next
        return node

    def peek(self, data):
        """
        finds the an element in the linked list
        Also returns the index of the element found
        """
        node = self.head
        count = 0
        if self.isEmpty():
            return
        
        while node.data is not data:
            if node.next == None:
                return 'Not found'
            
            node = node.next
            count += 1
        
        return node, count


    def peek_at_pos(self, index):
        """ finds an element based on its position in the linked list"""
        count = 0
        if self.isEmpty():
            return

        if isnan(index):
            return

        if count == index:
            return self.head
        
        node = self.head

        while count != index:
            if node.next == None:
                return "Not found"
            node = node.next
            count += 1
        return node


    

    def append(self, data):
        """Adds an element to the end of the linked list and prints the list out"""
        node = Node(data)
        if self.isEmpty():
            self.head = node
            return self.print_list()

        
        tail_node = self.iterate()
        tail_node.next = node
        node.next = None
        return self.print_list()


    def prepend(self, data):
        """Adds an element to the start of the linked list"""
        node = Node(data)
        if self.isEmpty():
            self.head = node
            return self.print_list()

        head_node = self.head
        node.next = head_node
        self.head = node
        return self.print_list()


    def insert(self, prev_node, data):
        """
        Insesrts an element in between nodes 
        Takes the previous node as ana argument
        returns the linked list
        """

        if self.isEmpty():
            return

        if not prev_node:
            return
        
        previous_node = self.peek(prev_node)

        if previous_node == "Not found":
            return

        new_node = Node(data)
        previous_node = previous_node[0]

        next_node = previous_node.next
        previous_node.next = new_node
        new_node.next = next_node
        return self.print_list()


    def delete(self):
        """Deletes the node at the tail of the linked list"""
        head_node = self.head

        if self.isEmpty():
            return

        while head_node and head_node.next is not None:
            if head_node.next.next == None:
                head_node.next = None
            head_node = head_node.next
        return self.print_list()

    def delete_specific_node(self, data):
        """Finds and deletes a specific node"""

        if not data:
            return
        
        if self.isEmpty():
            return

        found_node = self.peek(data)
        if found_node[1] == 0:
            found_node[0].next = None

        prev_node = self.peek_at_pos(found_node[1] - 1)
        prev_node.next = found_node[0].next
        found_node[0].next = None

    





linked_list = SinglyLinkedList()

linked_list.append(1)

linked_list.prepend(2)

# linked_list.iterate()

linked_list.peek(5)

linked_list.insert(2, 0)

print(linked_list.delete())