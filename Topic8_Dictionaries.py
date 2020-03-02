#T8Q1
# Initialize dictionary "contactinfo" with the values 
# as shown in above examples. Hint: The key is a string 
# literal while the value is a dictionary type.

contactinfo = {"Sally" : {'Email':'sally@hotmail.com', 'Phone':67654321},  "Tom" : {'Email':'tom@gmail.com', 'Phone':61234567}  }


#T8Q5
#In gene expression, mRNA is transcribed from a DNA template. The 4
#nucleotide bases of A, T, C, G corresponds to the U, A, G, C bases
#of the mRNA. Write a function that returns the mRNA transcript given
#the sequence of a DNA strand.
#Use a dictionary to provide the mapping of DNA to RNA bases.

# Use a dictionary to provide the mapping of DNA to RNA bases.
def mRNAtranscription(dna_template):
    dna2rna = {'A' : 'U', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
    mRNA = ''
    for base in dna_template:    
        mRNA += dna2rna[base]

    return mRNA
	
	
#T8Q6
#A DNA strand consisting of the 4 nucleotide bases is usually represented
#with a string of letters: A,T, C, G. Write a function that computes the base
#composition of a given DNA sequence. 


def baseComposition(dna_seq): 
    composition = {'A' : 0, 'C' : 0, 'T' : 0, 'G' : 0}
    for element in dna_seq:
        if element in composition:
          composition[element] += 1
          
    return composition
        
        
		
#T8Q7
#Write a function countLetters(word) that takes in a word as argument and
#returns a dictionary that counts the number of times each letter appears. 

def countLetters(word):
    dict = {}
    for base in word:
        if base in dict:
           dict[base] += 1
        else:
           dict[base] = 1
           
    return dict
           


#T8Q8
#Write a function reverseLookup(dictionary, value) that takes in a dictionary
#and a value as arguments and returns a sorted list of all keys that contains
#the value. The function will return an empty list if no match is found.

#T8Q9
#Write a function invertDictionary(d) that takes in a dictionary as argument
#and return a dictionary that inverts the keys and the values of the original
#dictionary. 

def invertDictionary(d):
    inv = {}
    for k, v in d.items():
        if v in inv:
            inv[v].append(k)
        else:
            inv[v] = [k]
    return inv
    
	
#T8Q10
#A sparse vector is a vector whose entries are almost all zero, like
#[1, 0, 0, 0, 0, 0, 0, 2, 0]. Storing all those zeros wastes memory and
#dictionaries are commonly used to keep track of just the nonzero entries.
#For example, the vector shown earlier can be represented as {0:1, 7:2}, since
#the vector it is meant to represent has the value 1 at index 0 and the value
#2 at index 7. Write a function that converts a sparse vector into a dictionary
#as described above. 

#T8Q11
#A sparse vector is a vector whose entries are almost all zero, like
#[1, 0, 0, 0, 0, 0, 0, 2, 0]. Storing all those zeros wastes memory and dictionaries
#are commonly used to keep track of just the nonzero entries. For example, the vector
#shown earlier can be represented as {0:1, 7:2}, since the vector it is meant to represent
#has the value 1 at index 0 and the value 2 at index 7. Write a function that converts a
#dictionary back to its sparese vector representation. 