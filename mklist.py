from text_sentence import Tokenizer
import fileinput

datafile="tweets02.txt"

datafile2="cities2.csv"

# finding the nth line
def nth_line_geo(n):
    with open(datafile2, 'r') as f:
        f.readline()
        list_of_lines=[]
        for l in f:
            list_of_lines.append(l)
        f.close()
    return list_of_lines[n]


#this def will seperate a line into it's words
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
        



# counting the number of tweets
def all_tweet_count():
    with open(datafile, 'r') as f:
        f.readline()
        count=0
        for l in f:
            count=count+1
        f.close()
    return count
# finding the nth tweet
def nth_line(n):
    with open(datafile, 'r') as f:
        f.readline()

        list_of_tweets=[]
        for l in f:
            list_of_tweets.append(l)
        f.close()
    return list_of_tweets[n]


#this def will seperate a tweet into it's words
def single_tweet_words(a):
    tline=nth_line(a)
    tnameL=[]

    #this peace of code gets rid of all numbers in the geoname database
    for i,word in enumerate(tline.split()):
        
        if any(char.isdigit() for char in word) == False :
            word=word.lower()
            word=word.replace("@","")
            word=word.replace("-","")
            word=word.replace(",","")
            tnameL.append(word)

    return tnameL

#making a list of the list of words in each tweet
def list_of_lists():
    list_of_lists=[]
    for i in range (0,(all_tweet_count()-1)):
        list_of_lists.append(single_tweet_words(i))
    return list_of_lists
        
# this def will make a list of geonames in a file
def geonames_into_words():
    #fg=open("worldcitiespop.txt", "r")
    gline=fg.read()
    fg.close
    
    gline=gline.replace("US","")
    gline=gline.replace("\n"," ")
    gnameL=[]

    #this peace of code gets rid of all numbers in the geoname database
    for i,word in enumerate(gline.split()):
        
        if any(char.isdigit() for char in word) == False :
            word=word.lower()
            gnameL.append(word)
                
        final_list=set(gnameL)

    return final_list







a=input("what is a?")
print nth_line_geo(a)
print single_tweet_words(a)
print third_word(a)










































    

