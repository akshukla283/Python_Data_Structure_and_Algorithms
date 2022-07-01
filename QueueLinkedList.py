# Creaing the Queue class using linked list

class Node:
    
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
    
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def __iter__(self):
        node = self.head
        while node :
            yield node
            node = node.next
            
            
        
class Queue:
    
    def __init__(self):
        self.linkedList = LinkedList()
        
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return " ".join(values)
    
    def enqueue(self, value):
        
        new_node = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = new_node
            self.linkedList.tail = new_node
            
        else:
            self.linkedList.tail.next = new_node
            self.linkedList.tail = new_node
            
            
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
        
        
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty!"
        
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            
            else:
                self.linkedList.head = self.linkedList.head.next
                
            
        return tempNode
    
    def peek(self):
        if self.isEmpty():
            return "The Queue is empty!"
        else:
            return self.linkedList.head
        
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None
            