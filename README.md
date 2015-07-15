Insight Data Engineering - Coding Challenge
===========================================================

Date: July 14, 2015

Program used in this Coding Challenge: Python 2.7.10, MacOS Lion 10.7.5, no external library used

This challenge implemented two features:

1. Calculate the total number of times each word has been tweeted.
The "words_tweeted.py" first opens the "tweets.txt" file and read each tweet into a list.
The program then count the occurance of each words and store it in "count", it also separate each word in the tweets and store them in "original". Next the program sort the list in alphabetical order and then remove any duplicated lines. Finally the program output the results in the ft1.txt file

2. Calculate the median number of *unique* words per tweet, and update this median as tweets come in. 
The "unique_median.py" first opens the "tweets.txt" file and determine how many lines in the tweets file.
Then for each new tweet, the program read the tweet, removes any duplicated words in each tweet, the output "count" that stores an integer representing unique words per tweet. 
Next the program calculate the median of the tweets as they come in by using mathematical method. 
Finally the program output the results in the ft2.txt file
