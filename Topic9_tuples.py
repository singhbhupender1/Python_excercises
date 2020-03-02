#T9Q3
#The determinant of a 2x2 matrix is the product of the elements on the main
#diagonal minus the product of the elements off the main diagonal. 

def det(M):
    return M[0][0]*M[1][1] - M[1][0]*M[0][1]
	
#T9Q4
#Write a function hasSameContent(t1, t2) that takes in two tuples as arguments
#and return True if both tuples contain the same items. 
def hasSameContent(t1, t2): 
    i = 1
    if(len(t1) != len(t2)):
        return False
    return sorted(t1)==sorted(t2)
	
	
#T9Q5
#Write a function sumNumbers(*args) that takes in a variable-length argument
#list of numbers and returns the sum of the numbers. 

def sumNumbers(*args):
    return sum(args)

#T9Q6
#Write a function commonElements(t1, t2) that takes in 2 tuples as arguments
#and returns a sorted tuple containing elements that are found in both tuples. 


#T9Q7
#Write a function removeCommonElements(t1, t2) that takes in 2 tuples as
#arguments and returns a sorted tuple containing elements that are not found
#in both tuples. 

#T9Q8
#Write a function shiftByTwo(*args) that takes in variable-length argument
#and returns a tuple with its elements shifted to the right by two indices.

#T9Q9
#Write a function sortByIndex(aList) that takes in a list of tuple in the
#following format: (index, value) and returns a new tuple with its elements
#sorted based on the index. 

#T9Q10
#Write a function sortByLength(t, order) that takes in a tuple of string and
#returns a new tuple with its elements sorted by the length of the string. The
#order of sorting is based on the value of the second argument: 'asc' or 'des'.