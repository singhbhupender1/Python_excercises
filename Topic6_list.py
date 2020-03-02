#T6Q1
#A list behaves like a container, and it is able to contain more than one value. Create a list with the
#values as shown in the example below.
aList = ['Hello', 0, 20.0, 'World']

#T6Q2
#A list can be modified, and more elements can be added to an existing list. Use the append(x) function
#to add some more items to the list to produce the same content shown in the sample below.

aList = ['Hello', 0] 
aList.append(20.0)
aList.append('World')

#T6Q3
#A list can be modified, and elements can be removed from an existing list. Use the remove(x) function
#to remove some items from the list shown in the sample given below so that the list is left with the
#following content: ['hello', 'python','programming'].

aList = ['hello', 'i', 'love', 'python', 'programming'] 
aList.remove('i')
aList.remove('love')

#T6Q4
#Write a function addNumbersInList(numbers) to add all the numbers in a list. To access each element in
#a list, you can use the statement 'for num in numbers:'.

def addNumbersInList(numbers):
    return sum(numbers)
	
#T6Q5
#Write a function addOddNumbers(numbers) to add all the odd numbers in a list. To access each element in
#a list, you can use the statement 'for num in numbers:'.


def addOddNumbers(numbers): 
    total = 0
    for num in numbers:
        if num % 2 == 0:
            continue
        else:
            total += num
    return total  
	
#T6Q6
#Write a function countOddNumbers(numbers) to count the number of odd numbers in a list.
	
	
def countOddNumbers(numbers): 
     total = 0
     for num in numbers:
         if num % 2 == 0:
             continue
         else:
             total += 1
     return total

	 
#T6Q7
#Write a function getEvenNumbers(numbers) to return all the even numbers in a list. 

def getEvenNumbers(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)
    return new_list 

#T6Q8
#Write a function removeFirstAndLast(list) that takes in a list as an argument and remove the first and last
#elements from the list. The function will return a list with the remaining items. 

def removeFirstAndLast(numbers): 
    new_list = numbers[1:-1]
    return new_list
	
	
#T6Q9
#Write a function getMaxNumber(numbers) that returns the maximum number in a list. 

def getMaxNumber(numbers):
    max = 0
    if len(numbers) > 0:
        for i in numbers:
            if i > max:
                max = i
    else:
        max  = 'N.A'
        
    return max
	
	
#T6Q10
#Write a function getMinNumber(numbers) that returns the minimum number in a list. 


def getMinNumber(numbers):
    mas = 0
    if len(numbers) > 0:
        mas = min(numbers)
    else:
        mas = 'N.A'
    return mas
	
	
#T6Q11
#Write a function that does matrix multiplication.
#The product of a mxn matrix with a nxp matrix results in a mxp matrix.
#A mxn matrix, with m rows and n columns, can be represented using nested lists.
#Am,n = [ [x11, x12, ..., x1n], ..., [xm1, ..., xmn] ] 



#T6Q13
#A mxn matrix, m rows and n columns, can be represented using
#nested lists. Write a function that returns the diminensions of a matrix. 

#T6Q16
#Write a function combine(la, lb) that takes in two lists and return
#a list with the contents of both list sorted in ascending order.


def combine(la, lb): 
    return sorted(la + lb)
	
	
#T6Q17
#The transpose of a matrix M, denoted MT, is formed by interchanging
#the rows and columns of M. That is, a mxn matrix is transformed into
#a nxm matrix.[MT]ij = [M]ji. Write a function that returns the
#transpose of a matrix. 

def transpose(matrix): 
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] 

#T6Q19
#Write a function calCumulativeSum(numbers) that takes in a list of
#numbers as argument and returns the cumulative sum of the list. That
#is, the new list where the i element is the sum of the first i + 1
#elements from the original list. For example, the cumulative sum of
#[1, 2, 3] is [1, 3, 6]. 

def calCumulativeSum(numbers): 
    list = []
    csum = 0
    for i in numbers:
        csum += i
        list.append(csum)
    return list
	

#T6Q20
#Write a function combineList(list1, list2) that takes in two lists
#as arguments and return a list that combines all the elements in
#the two list. 


def combineList(list1, list2): 
    
    for i in range(len(list2)):
        list1.append(list2[i])
    return list1
        

#T6Q21
#Write a function (list1, list2) that takes in two lists as arguments
#and return a list that is the result of removing elements from list1
#that can be found in list2. 


def subtractList(list1, list2): 
    
    res = [i for i in list1 if i not in list2]
    return res
	
	
#T6Q22
#Write a function countLetters(word) that takes in a word as argument
#and returns a list that counts the number of times each letter appears.
#The letters must be sorted in alphabetical order. 

def countLetters(word):
    u = set(word)
    return sorted([(l, word.count(l)) for l in u])
	
	
#T6Q23
#Write a function getNumbers(number) that takes in a number as argument
#and return a list of numbers as shown in the samples given below
#>>> getNumbers(10)
#    [100, 64, 36, 16, 4, 0, 4, 16, 36, 64, 100]

#T6Q24
#Write a function getSumOfFirstDigit(numList) that takes in a list of
#positive numbers and returns the sum of all the first digit in the list. 

def getSumOfFirstDigit(num): 
    sum1 = 0
    for x in num:
        temp = str(x)
        sum1 += int(temp[0])
    return sum1

#T6Q26
#List comprehension offers a concise way to derive a new list from an
#existing list or sequence. Given a list of numbers, write a function
#that returns the numbers that are greater than the average.

def getAboveAverage(nums):
    return [ x for x in nums if x > sum(nums) / len(nums) ]  # complete the list comprehension 