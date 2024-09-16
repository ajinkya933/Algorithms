# RAM is where Python keeps all the objects, variables, 
# and data structures that are actively being used by a 
# running program.

# when any object is created memory is allocated to it in RAM,
# there are two types of memory allocation:
# Stack: Memory is allocated automatically as functions are called/return.
# Heap: Memory is allocated on demand by the program.

# Structure of RAM :  
# Each location has a unique address, typically represented 
# as a hexadecimal number. By convention, lower addresses are 
# closer to zero. Lower addresses are typically at the "bottom" of memory.
# Higher addresses are at the "top" of memory.

# RAM
# +---------------------------+
# |  Higher Addresses         |  e.g., 0xFFFFFFFF
# |  (larger numbers)         |
# |                           |
# |                           |
# |                           |
# |                           |
# |                           |
# |  Lower Addresses          |  e.g., 0x00000000
# |  (smaller numbers)        |
# +---------------------------+

# RAM
# +---------------------------+
# |         Stack             |  Higher addresses
# |  +---------------------+  |
# |  | Local variables     |  |
# |  +---------------------+  |
# |                           |
# |                           |
# |         Heap              |
# |  +---------------------+  |
# |  |                     |  |
# |  |    Dynamic objects  |  |
# |  |                     |  |
# |  +---------------------+  |  Lower addresses
# +---------------------------+


# Program: 

# Instance variables : maintained in the memory allocated for the object (often in the heap).
# Local variables : created and destroyed in the stack memory for each method call.

# instance variable is created when you type "self.something",
# so "self" aids in creation of instance variable but "self"
# itself is not an instance variable



# link list uses instance variables 
# instance variables (using self) maintain their 
# values across function calls, while local variables 
# are recreated each time.

# that means after each function call ends 
# the local variables are destroyed, but the 
# instance variables are not destroyed and 
# their values are retained.


# Ideally this is how linklist looks, here 
# for simplicity we defined most basic form of linklist
# where we have avlue and next

def node(value, next):  
    value = value
    next = None
# Creating head of the Linked list
head = node(1)

# Issues in this kind of declaration:
# 1. We created linklist using just variables, so now 
# their state does not persists after the function ends variables value is destroyed
# 2. Operations like insertion, deletion, or traversal cannot be performed,
# as doing these operations need "value" to be persisted beyond the function call
# for us this "value" is destroyed after function call ends.

# The linked structure is maintained by the next references between nodes.
# If next were a local variable, the links between nodes would be lost as soon 
# as the initialization method completed.

# To overome this we use instance variables, class and constructor like this

class Node:
    def __init__(self, value):   # __init__ also called constructor is used for Object initialization
        self.value = value
        self.next = None
# Creating head of the Linked list
head = Node(1)
print("The value at head is", head.value)