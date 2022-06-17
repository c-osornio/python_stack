# Singly Linked Node
from pkg_resources import add_activation_listener


class SLNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SList:
    def __init__(self):
        self.head = None
# Just as we would pass in a value to a Python list's append method, our add_to_front method should accept a value to be added to the list:
    def add_to_front(self, val):
        #Create a node with the given value, with the SLNode
        new_node = SLNode(val)
        #Set the new node's next to be the current head
        new_node.next = self.head
        # Set the list's head to the new node
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head # pointer to the list's first node
        # could also be while runner:
        while runner != None: # iterating while runner is a node and not None
            print(runner.value)
            runner = runner.next # set the runner to its neighbor
        return self    # once the loop is done, allow for chaining

    def add_to_back(self, val): # accepts a value
        if self.head == None:   # if the list is empty
            self.add_to_front(val)  # run the add_to_front method
            return self # lets make sure the rest of this function doesnt happen if we add to the front
        new_node = SLNode(val) # create a new instance of our Node class with the given value
        runner = self.head # set an iterator to start at the front of the list
        while runner.next != None: # iterator until the iterator doesnt have a neighbor
            runner = runner.next # increment the runner to the next node in the list
        runner.next = new_node # increament the runner to the next node in the list
        return self # chaining

    def remove_from_front(self):
        if self.head != None: 
            # runner = self.head
            self.head = self.head.next
            # runner = None
        return self 

    # def remove_from_back(self):
    #     if self.head == None:
    #         return self
    #     elif self.head.next == None:
    #         self.head = None
    #         return self
    #     else:
    #         current = self.head
    #         while current.next.next != None:
    #             current = current.next
    #         current.next = None
    #     return self

    def remove_from_back(self):
        if self.head != None:  # if we have a list
            if self.head.next == None: # if there there is only one node
                self.head = None # remove the head
            else: # more than one node
                runner = self.head # set runner to iterate over the list
                while runner.next.next != None: # move the runner to the back
                    runner = runner.next # keep moving runner until it reaches the second to last node
            lastNode = runner.next # runner is at the second to last node, so here the last node = runner.next
            runner.next = None  # runner is at the second to last node, so here we update the second to last node's next to None
            lastNode = None # then the last node is set to None as well
        return self # chaining

    def remove_val(self, val): # accepts a value, value is to be removed
        runner = self.head  # pointer to the list's first node
        found = False # check to see if we found the value in our list
        if runner != None:  # check if list is empty
            if runner.value == val: # if not, check if the first node's value is the value we are searching
                self.remove_from_front() # if so, call the remove from front method
                return self
            while runner != None: # if not, look through every node
                if runner.value == val: # check if value of runner is the value we are searching
                    found = True # if found, update found to True
                    break # exit
                runner = runner.next #if not found, move runner to the next node and continue search until found or runner is at the last node without a match
            if found == True: # if we found a matching value
                if runner.next == None: # if we found the matching value in the last node
                    self.remove_from_back() # call the remove from the back method
                    return self 
                else: # matching value found in the middle nodes
                    foundNode = runner # set foundNode to runner which is currently at the matching node
                    prevRunner = self.head # looking for the previous node before the maching node so we can update the next node to skip the matching node that we will eventually remove
                    while prevRunner != None: # iterate through the list of nodes until we find the matching node's prevRunner 
                        current = prevRunner.next # trying to make current equal the matching node
                        if current.value == val: # if current is the matching node
                            prevRunner.next = foundNode.next # attach the previous node to the matching node's next node
                            foundNode = None # remove the matching node
                            return self #chaining
                        prevRunner = current #if not, update the prevRunner as the next node until we find the matching node
            else:
                print(val, "is not found in the list.") # searched each node and value was not found
                return self # chaining
        else:
            print("The list is empty") # else the list is empty
            return self # Chaining

    def insert_at(self, val, n):
        list = []
        runner = self.head 
        while runner:
            list.append(runner.value)
            runner = runner.next
        if n == 0:
            self.remove_from_front()
            self.add_to_front(val)
            return self
        elif n == len(list):
            self.remove_from_back()
            self.add_to_back(val)
            return self
        else:
            currentValue = list[n]
            runner = self.head
            while runner:
                if runner.value == currentValue:
                    runner.value = val
                    return self
                runner = runner.next

# my_list = SList()
# my_list.add_to_front("Jim")
# my_list.add_to_front("Dwight")
# my_list.add_to_front("Andy")
# my_list.print_values()

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()          # chaining, yeah!
# output should be:
# Linked lists
# are
# fun!

#1. remove_from_front(self) - remove the first node and return its value
my_list.remove_from_front().print_values()
#2. remove_from_back(self) - remove the last node and return its value
my_list.remove_from_back().print_values()
#3 remove_val(self, val) - remove the first node with the given value
my_list.add_to_back("fun!").add_to_front("Linked lists").print_values()
my_list.remove_val("are").print_values()
#4 insert_at(self, val, n) - insert a node with value val as the nth node in the list
# Consider the following cases:
# n is 0
# n is the length of the list
# n is between 0 and the length of the list

my_list.insert_at("are",1).add_to_back("fun!").print_values()