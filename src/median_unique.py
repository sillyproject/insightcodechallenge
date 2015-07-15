# example of program that calculates the median number of unique words per tweet.
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


#configure the input files assuming in the following directory: change as needed
ft2 = os.path.join("/Users/sibog/Desktop/insightcodechallenge/tweet_output/ft2.txt")         
file2 = open(ft2, "w")
tweets = open("/Users/sibog/Desktop/insightcodechallenge/tweet_input/tweets.txt")
#determine how many lines in the tweets.txt file
num_lines = sum(1 for line in tweets)

#remove duplicate words in each tweet and then count the unique words in each tweet
#output: count (of unique words in each tweets)
lines =  open("/Users/sibog/Desktop/insightcodechallenge/tweet_input/tweets.txt").readlines()

n=0
for n in range(n, num_lines):
      words = lines[n].split()
      unique = remove_duplicates(words)
      count = len(unique)
      print >>file2, count
file2.close()

ft2mod = open(ft2, "r")
count = file.read(ft2mod).split()
count = [float(j) for j in count] #convert to float

#calculate median for each tweet that comes in
#output: ft2.txt file
file2mod = open(ft2, "w")
i=1
for i in range(i, num_lines+1):
      if not i%2:
            sort = sorted(count[:i])
            median = (sort[(i/2)-1]+sort[i/2])/2.0
      else:
            sort2 = sorted(count[:i])
            median = sort2[i/2]
      print >>file2mod, median

file2mod.close()

