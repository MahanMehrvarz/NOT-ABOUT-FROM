# -*- coding: utf-8 -*-
import TwitterSearch
from TwitterSearch import *

import time

try:
    TSO = TwitterSearchOrder() # create a TwitterSearchOrder object
    TSO.set_keywords(['protest']) # defining all words we would like to have a look for
    TSO.set_language('en') # we want to see english tweets only
    TSO.set_include_entities(False) # and don't give us all those entity information
    TSO.set_result_type('recent')
    #TSO.set_geocode(34.391,-100.898,1000,'km')
    #TSO.set_geocode(52.5233,13.4127,10,'km')
                   


    

    # it's about time to create a TwitterSearch object with our secret tokens
    TS = TwitterSearch(
        consumer_key = '***',
        consumer_secret = '***',
        access_token = '**',
        access_token_secret = '***'
     )

    # this is where the fun actually starts :)
    count=0
    f=open("tweets01.csv","w")
    f2=open("from01.csv","w")
    for tweet in TS.search_tweets_iterable(TSO):
        d=( '@%s TWEETED: %s' % ( tweet['user']['screen_name'],tweet['text']))
        From=tweet['user']['location']
        #response=TSO.get_metadata()
        #t=response['date']
        d=d.replace("\n","-")
        d=d.replace(",","-")
        From=From.replace(",","-")
        
        #print t
        #print d.encode('ascii', 'ignore')
        count=count+1
        f.write(d.encode('ascii', 'ignore'))
        f.write(" FROM: ")
        f.write(From.encode('ascii', 'ignore'))
        
        f2.write(From.encode('ascii', 'ignore'))
        f.write(",")
        f2.write(" ")
        f2.write(",")
        #f.write(From.encode('ascii', 'ignore'))
        #f.write(",,")
        #f.write(t.encode('ascii', 'ignore'))
        #f.write("\n")
        
    print count
    f.write(str(count))
    f.close()
    f2.write(str(count))
    f2.close()
except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print "failed on data"
