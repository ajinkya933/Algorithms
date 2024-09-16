#############################################
#  Given a array find missing element in it
#  Find total by total=n*(n+1)/2  where n is the length of the array
#  find sum 0f total elements in array
#  Sum of elements - total is the missing element
#############################################

def miss(A):

    
    sum_of_A=sum(A)
    n=len(A)
    total=n*(n+1)/2
    
    return abs(total-sum_of_A)
    
   
A = [1, 2, 4, 5, 6] 

print(miss(A))
