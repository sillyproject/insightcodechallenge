# example of program that calculates the total number of times each word has been tweeted.
# Author: Sibo Gao
# Date: July 14, 2015

import os.path

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet, add it to both list and set. Author: http://www.dotnetperls.com
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output


#configure the input files assuming in the following directory:/Users/sibog/download/insightcodechallenge/tweet_input/tweets.txt; change as needed
tweets = open("/Users/sibog/download/insightcodechallenge/tweet_input/tweets.txt", "r") 
readtweets = file.read(tweets).split()

ft1 = os.path.join("/Users/sibog/Desktop/insightcodechallenge/tweet_output/ft1.txt")         
file1 = open(ft1, "w")

#count the occurance of each word in the tweets.txt
l = len(readtweets)
m=0
original = {}
for m in range(m, l):
      count = readtweets.count(readtweets[m]) 
      original = ''.join(readtweets[m] + " " + str(count))
      print >> file1, original     
file1.close()


#sort the tweet list in alphabetical order as well as remove duplicated lines
ft1mod = file.read(open(ft1)).splitlines()
sort = sorted(ft1mod) 
modifiedtweets = remove_duplicates(sort)


#output sorted tweet list into ft1.txt file
file1mod = open(ft1, "w")

lmod = len(modifiedtweets)
n=0
for n in range(n, lmod):
      modified = modifiedtweets[n]
      print >> file1mod, modified
file1mod.close()



