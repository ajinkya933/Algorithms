#understanding tuples , lists, enumarate and 'for' loops in python 

"""
########################################################
#nums=[2,7,1,15]              # a list   (list can be changed)
nums=(2,7,1,15)               # a tuple  (tuples cannot be changed)

for num in enumerate(nums):
        print(num, 'hello')   
 
#output
#(0, 2) hello        #enumarate(nums) = (0,2)
#(1, 7) hello
#(2, 1) hello
#(3, 15) hello      
        
        
for count, num in enumerate(nums):
        print(num, 'hello')      

# Output
#2 hello    here count=0 but not displayed 
#7 hello    here count=1 but not displayed
#1 hello    here count=2 but not displayed
#15 hello   here count=3 but not displayed
        
        
########################################################




#################### How to create a Dictionary ###############

a = {}    # It creates a dictionary names it 'a' and gives it size = 0
a = {'a':1, 'b':2}

a[3]=5

###############################################################
"""





# creating enumerate objects
def twosum(nums, target):
    lookup = {}
    for cnt, num in enumerate(nums):
        if target - num in lookup:
            return lookup[target-num], cnt 
        lookup[num] = cnt   


a = (1,2,3,4,5)
t = 9
print(twosum(a,t))  # (1,2)










