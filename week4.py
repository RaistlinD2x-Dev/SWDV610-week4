class Empty(Exception):
    """ Creates Empty Exception for empty lists """

    def __init__ (self, message="This is empty."):
        super().__init__(self.message)



class StackLinkedList:
    """Last in first out Stack using singly linked list"""

    class _Node:
        """ embedded Node class to simplify creation of nodes"""

        """ slots removes native dict creation and improves memory as # of nodes increases """
        __slots__ = '_ele', '_next'

        def __init__(self, ele, next): # init of node instance variables
            self._ele = ele            # reference to data in node
            self._next = next          # maintains reference to next node in sequence

    
    def __init__(self):
        """ Creates an empty stack """
        self._head = None              # initializes empty
        self.size = 0                  # maintin reference to stack size to mitigate linked list traversal

    def __len__(self):
        """ Returns the current size of the stack """
        return self.size

    def is_empty(self):
        """ Return True if the stack is empty. """
        return self.size == 0

    def push(self, ele):
        """ Add data 'ele' to the top of the Stack """
        self._head = self._Node(ele, self._head) # initializes new head node with 'ele' data and sets it as the head
        self.size += 1                          # adds 1 to the size to maintain current size count

    def pop(self):
        """ Remove and return the element from the top of the stack (This represents Last In First Out)
        
        Raise an Empty Exception if the stack is Empty
        """
        if self.is_empty():
            raise Empty()
        answer = self._head._ele                # set answer = data in head Node
        self._head = self._head._next           # sets head Node equal to the proceeding Node
        self.size -= 1                          # decrement the size to account for the head node being removed
        return answer                           # return the original head data element


print("---- This is the Stack Linked List ----")
newStack = StackLinkedList()
newStack.push(25)
newStack.push(101)
newStack.push(378)
print("The size of the stack is: {}".format(newStack.size))
print("The last element is the first in the list, it's value is: {}".format(newStack.pop()))
print(newStack.is_empty())

class QueueLinkedList:
    """ First In First Out Queue using Singly Linked List """
    class _Node:
        """ embedded Node class to simplify creation of nodes"""

        """ slots removes native dict creation and improves memory as # of nodes increases """
        __slots__ = '_ele', '_next'

        def __init__(self, ele, next): # init of node instance variables
            self._ele = ele            # reference to data in node
            self._next = next          # maintains reference to next node in sequence

    def __init__(self):
        """ This creates an empty queue """
        self._head = None               # assign None to the head, means nothing exists
        self._tail = None               # assign None to tail, means nothing exists
        self._size = 0                  # mitigate linked list traversal by keep count of node amount

    def __len__(self):
        """ Returns 'length' or size of queue """
        return self._size

    def is_empty(self):
        """ Returns True is size is 0 """
        return self._size == 0

    def first(self):
        """ Return the element at the front of the queue but don't remove it as will be seen in pop """
        if self.is_empty():
            raise Empty()
        return self._head._ele          # returns the element at the front of the queue

    def dequeue(self):
        """ Remove and return first element in the queue, like pop but first instead of last 
        
        Raise Empty exception if the queue is empty
        """

        if self.is_empty():
            raise Empty()
        answer = self._head._ele        # creates temp variable to store original value of head data element
        self._head = self._head._next   # assigns the proceeding data element to the head 
        self._size -= 1                 # reduce quantity count of queue by 1
        if self.is_empty():
            self._tail = None           # clean up assignment to tail is the queue has become empty
        return answer

    def enqueue(self, ele):
        """ Add an element to the back of queue, like append on list """
        newest = self._Node(ele, None)
        if self.is_empty():
            self._head = newest         # if the queue was empty, the element added becomes the head element
        else:
            self._tail._next = newest   # creates the tail reference to the new element before assigning the new element to tail
        self._tail = newest
        self._size += 1                 # increment the quantity of Nodes present in the queue


print("---- This is the Queue Linked List ----")
newQueue = QueueLinkedList()
newQueue.enqueue(38)
newQueue.enqueue(100)
newQueue.enqueue(3498)
print("The size of the Queue is: {}".format(newQueue._size))
print("The first element was (now removed): {}".format(newQueue.dequeue()))
print("The first element in the list now is (not removed): {}".format(newQueue.first()))
print("The queue is empty? {}".format(newQueue.is_empty()))


class DequeLinkedList:
    """ Create deque with singly linked list """

    class _Node:
        """ embedded Node class to simplify creation of nodes"""

        """ slots removes native dict creation and improves memory as # of nodes increases """
        __slots__ = '_ele', '_next'

        def __init__(self, ele): # init of node instance variables
            self._ele = ele            # reference to data in node
            self._next = None         # maintains reference to next node in sequence

    
    def __init__(self):
        """ Creates an empty deque """
        self._head = None              # initializes empty
        self.size = 0                  # maintin reference to stack size to mitigate linked list traversal

    def __len__(self):
        """ Returns the current size of the stack """
        return self.size

    def is_empty(self):
        """ Return True if the deque is empty. """
        return self.size == 0

    def insertAtFront(self, ele):
        """ Add Node to the beginning of the LL """
        tempVar = self._Node(ele)           # temporary assignment of the new node for comparison
        if self._head == None:              
            self._head = tempVar            # if the deque is empty assign head to new node
            self.size += 1                  # increment deque size by 1
        else:
            tempVar._next = self._head       # if deque is not empty, assign next node relation to current head
            self._head = tempVar            # replace head value with new Node
            self.size += 1                  # increment the deque size by 1

    def insertAtBack(self, ele):
        """ Traverse the LL to find and append to the new Node to the LL """
        tempVar = self._Node(ele)           # temp assignment of new Node
        if self._head == None:              
            self._head = tempVar            # if LL is empty assign temp variable as new head
            self.size += 1                  # increment size of LL by 1
        else:
            current = self._head            
            while current._next != None:    # traverse LL to get to the end
                current = current._next
            current._next = tempVar         # assign new node as the last element in the LL
            self.size += 1

    def deleteFromFront(self):
        """ delete the first element in the LL """
        if self.is_empty():
            raise Empty()
        else:
            tempVar = self._head            # temporary assignment of current head element to temp variable
            self._head = self._head._next   # assign proceeding element as head element
            del tempVar                     # delete the old head element
            self.size -= 1

    def deleteFromBack(self):
        """ traverse the LL to find the last element and delete it """
        if self.is_empty():
            raise Empty()
        else:
            current = self._head            # assign head value as current
            previous = None                 # assign None to previous temp var as a starting point
            while current._next != None:    # traverse LL while assigning new previous and current to element and next
                previous = current
                current = current._next
            previous._next = current._next
            del current                     # delete the final element in the ::
            self.size -= 1

    def getFirst(self):
        """ Return the first element in LL without removing """
        if self.is_empty():
            raise Empty()
        else:
            return self._head._ele          # return the first element in the LL without removing

    def getLast(self):
        """ Return the last element in LL without removing"""
        if self.is_empty():
            raise Empty()
        else:
            current = self._head
            while current._next != None:    # traverse LL to find the end
                current = current._next
            return current._ele             # return the last element in LL without removing

    def getAllElements(self):
        current = self._head
        print(current._ele, end = " ")
        while current._next != None:
            current = current._next
            print(current._ele, end = " ")
        print()

print(" ---- This is the Deque Linked List ----")
newDeque = DequeLinkedList()
print("----- Now inserting the number 23 at the front -----")
newDeque.insertAtFront(23)
print("The first element in the list is: {}".format(newDeque.getFirst()))
print("----- Now inserting the number 48 at the front -----")
newDeque.insertAtFront(48)
print("The new first element in the list is: {}".format(newDeque.getFirst()))
print("And the last element in the list is now: {}".format(newDeque.getLast()))
print("----- Now inserting the number 101 at the rear -----")
newDeque.insertAtBack(101)
print("The first element in the list is: {}".format(newDeque.getFirst()))
print("And the last element in the list is now: {}".format(newDeque.getLast()))
newDeque.getAllElements()
print("----- Deleting last element in LL -----")
newDeque.deleteFromBack()
newDeque.getAllElements()
print("----- Deleting first element in LL -----")
newDeque.deleteFromFront()
newDeque.getAllElements()
print("Is the list empty? {}".format(newDeque.is_empty()))
