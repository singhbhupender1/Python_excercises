#T7Q1
#Write the function countA(word) that takes in a word as argument and
#returns the number of 'a' in that word. 

def countA(word):
    count = 0
    for i in range(len(word)):
        if word[i] == 'a':
            count += 1
    return count
	
#T7Q2
#Write the function countLetter(word, letter) that takes in a word and
#a letter as arguments and returns the number of occurrence of that letter
#in the word. 

def countLetter(word, letter):
    count = 0
    for i in range(len(word)):
        if word[i] == letter:
            count += 1
    return count
	
#T7Q3
#Write a function removeLetter(word, letter) that takes in a word and a
#letter as arguments and remove all the occurrence of that particular
#letter from the word. The function will returns the remaining leters
#in the word. 

def removeLetter(word, letter):
    return "".join([i for i in word if i != letter])
    
            


#T7Q4
#Write the function changeCase(word) that changes the case of all the
#letters in a word and returns the new word. 

def changeCase(word):
    return word.swapcase()
	
	

#T7Q5
#Write the function search(word, substring) that takes in a word and
#a substring as arguments and returns the position (0 indexed) of the
#substring if it is found in the word. The function returns -1 if the
#substring is not found.

def search(word, substring):
    index = -1
    if substring in word:
        index = word.find(substring)
    return index
            

#T7Q6

#A string contains a sequence of characters. Elements within a string can
#be accessed using index that starts from 0. Write the function getChar(word, pos)
#that takes in a word and a number as argument and returns the character at that position. 

def getChar(word, pos):
    alpha = ''
    counter = 0 
    
    if len(word) > pos:
        for i in word:
            
            if counter == pos:
                alpha = i   
            counter = counter + 1
    else:
        alpha = 'Invalid Range.'
         
    return alpha
    
        


#T7Q7
#Write a function countVowels(word) that takes in a word as an argument and returns the
#number of vowels ('a', 'e', 'i', 'o', 'u') in the word. 

def countVowels(word):
    count = 0
    vowel = 'aeiou'
    for i in word:
        if i in vowel:
           count += 1
    return count

#T7Q8
#Write the function getVowels(word) that takes in a word as an argument and returns
#the vowels ('a', 'e', 'i', 'o', 'u') in that word. 

def getVowels(word):
    return [i for i in word if i in 'aeiouAEIOU' ]
    


#T7Q9
#Write the function capitalizeVowels(word) that returns the word with all the vowels capitalized.

def capitalizeVowels(word):
    #return  "".join[x.upper() if x in 'aeiou' else x for x in word]
    string = ''
    for x in word:
        if x in 'aeiou':
            string += x.upper()
        else:
            string += x
    return string
	
#T7Q10
#Write the function startEndVowels(word) that returns True if the word starts and e


def startEndVowels(word):
    vowels = 'aeiouAEIOU'
    return len(word) > 0 and word[0] in vowels and word[-1] in vowels
    

#T7Q11
#Write the function removeVowels(word) that removes all the vowels ('a', 'e', 'i', 'o', 'u') in a word
#and returns the remaining letters in the word. 

def removeVowels(word):
    return "".join([i for i in word if i not in 'aeiouAEIOU'])

#T7Q12
#Write the function reverseWord(word) that returns the word in the reverse order. 

def reverseWord(word):
    return ''.join(reversed(word))
	
#T7Q13
#Write the function isReverse(word1, word2) that takes two words as arguments and returns True is the
#second word is the reverse of the first word. 

def isReverse(word1, word2):
    return word1 == ''.join(reversed(word2))

#T7Q14
#Write the function startWithVowel(word) that takes in a word as argument and returns a substring that starts
#with the first vowel found in the word. The function returns 'No vowel' if the wor


#T7Q15
#Write the function getCommonLetters(word1, word2) that takes in two words as arguments and returns a new string
#that contains letters found in both string. Ignore repeated letters and sort the result in alphabetical order. 


def getCommonLetters(word1, word2):
    res = ""

    for letter in word1:
       if letter in word2:
          if letter not in res: # skip if we already found it
             # don't return yet, but rather accumulate the letters
              res = res + letter
    res = ''.join(sorted(res))
    return res
	
#T7Q16
#Write a function mirrorText(word1, word2) that takes in 2 words as arguments and returns a new word in the
#following order: word1word2word2word1. 

def mirrorText(word1, word2):
    return word1+word2+word2+word1
	
#T7Q17
#Write a function echoWord(word) that takes in a word as arguments and returns a word that repeats itself
#based on the number of letter in the word.

def echoWord(word):
    return (len(word) * word)

#T7Q18
#Write a function rightJustify(word) that takes in a word as argument and return a word with leading
#spaces so that the last letter of the word is in column 50 of the display. 


#T7Q19
#A palindrome is a word, phrase, number or other sequence of units that can be read the same way in
#either direction. Write a function that determines whether the given word or numbe


def isPalindrome(word):
    word = str(word)
    if(word == ""):
        return False
    word = word.lower()
    rev_word = word[::-1]
    if(word == rev_word):
        return True
    else:
        return False
		
#T7Q20
#Topic 7: Question 20
#Write a function isInAlphabeticalOrder(word) that takes in a word as argument and returns True if the
#word contains letters that are arranged in alphabetical order. For example, the letter 'c' should not
#appear before the letter 'a'. 

def isInAlphabeticalOrder(word):
    sorted_word = ''.join(sorted(word))
    if(word == sorted_word):
        return True
    return False
	

#T7Q21
#Write a function isAllLettersUsed(word, required) that takes in a word as the first argument and returns
#True if the word contains all the letters found in the second argument. 

def isAllLettersUsed(word, required):
    splited = list(word)
    for i in required:
        if i not in splited:
            return False
    return True

#T7Q22
#Write a function isTripleDouble(word) that takes in a word as argument and returns True if the word contains
#three consecutive double letters. 

def isTripleDouble(word):
    count = 0  
    i = 1 
    while i < len(word): 
 	if word[i] == word[i-1]: 
 		count += 1 
 		i+=2 
 	else: 
 		count = 0 
 		i+=1 
    if count == 3: 
 	return True 
    else: 
 	return False 


#T7Q23
#Write a function splitWord(word, numOfChar) that takes in a word and a number as arguments. The function will
#split the word into smaller segments with each segment containing the number of letter specified in the numOfChar
#argument. These segments are stored and returned in a list. 


#T7Q24
#An anagram is a word formed by reordering the letters of another word. Write a function isAnagram(w1, w2) that
#takes in two words as arguments and return True if one word is an anagram of the other word. 
def isAnagram(w1, w2):
    w1 = sorted(w1.lower())
    w2 = sorted(w2.lower())
    if(w1==w2):
        return True
    return False