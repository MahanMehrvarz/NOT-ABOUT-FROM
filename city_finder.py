from text_sentence import Tokenizer
import fileinput

datafile2="cities2.csv"

# finding the nth tweet
def nth_line_geo(n):
    with open(datafile2, 'r') as f:
        f.readline()
        list_of_lines=[]
        for l in f:
            list_of_lines.append(l)
        f.close()
    return list_of_lines[n]


#this def will seperate a tweet into it's words
def single_line_words(a):
    gline=nth_line_geo(a)
    gnameL=[]

    #this peace of code gets rid of all numbers in the geoname database
    for i,word in enumerate(gline.split()):
        
        #if any(char.isdigit() for char in word) == False :
        word=word.lower()
        gnameL.append(word)

    return gnameL

def third_word(a):
    list1=single_line_words(a)
    return list1[2]
    
    #for i in range(0,29471)
        

a=input("what is a?")
print nth_line_geo(a)
print single_line_words(a)
print third_word(a)
