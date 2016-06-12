
from text_sentence import Tokenizer
import fileinput



# this def will make a list of geonames in a file
def geonames_into_words():
    fg=open("worldcitiespop.txt", "r")
    #fg=open("dataset05.txt", "r")
    gline=fg.read()
    fg.close
    
    gline=gline.replace(","," ")
    gline=gline.replace("@","")
    gline=gline.replace("#","")
    gline=gline.replace("\n"," ")
    gnameL=[]

    #this peace of code gets rid of all numbers in the geoname database
    for i,word in enumerate(gline.split()):
        f=open("city_names_clean.txt","a")
        if any(char.isdigit() for char in word) == False :
            word=word.decode('ascii', 'ignore')
            word=word.lower()
            gnameL.append(word)
            print word
            f.write(word.encode('ascii', 'ignore'))
            f.write("\n")
        f.close() 
    
    final_list=set(gnameL)
    for word in final_list:
        f=open("city_names_clean_set.txt","a")
        f.write(word.encode('ascii', 'ignore'))
        f.write("\n")
        f.close()
    return final_list




print geonames_into_words()
