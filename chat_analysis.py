import csv
from collections import Counter
from textblob import TextBlob, Word, Blobber
##import nltk
##nltk.download('stopwords')
##nltk.download('wordnet')
#
chat_log_list = []

with open("chatlog_debate_1.csv", 'r') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  for row in csv_reader:
    chat_log_list.append(row[0])


#
cnt = Counter()
for row in chat_log_list:
  cnt[row]+=1

# word counter
result = cnt.most_common()

# spam filter
filtered_log_list = []

for each in result:
  if each[-1] == 1:
    filtered_log_list.append(each)


# search for keywords manually
key_search = False
key_search_result = []
while not key_search:

  counter = 0
  key_search = input("Enter keyword: ")
  overall_sentiment = 0

  for each in filtered_log_list:

    # clean text
    keyword = key_search.strip().lower()
    text = each[0].strip().lower()
    text_sentiment = 0

    #
    if keyword in text:

      counter+=1

      text_sentiment_value = TextBlob(text)
      text_sentiment_value = text_sentiment_value.sentiment[0]

      # assume neutral
      pos_neg = "[Neutral]"
      if text_sentiment_value > 0:
        pos_neg = "[Positive]"
      if text_sentiment_value < 0:
        pos_neg = "[Negative]"

      print(pos_neg, each[0])


      overall_sentiment+=text_sentiment_value

  message = "\nFound ({}) for keyword '{}'".format(counter, key_search)
  print(message)

  # don't divide by 0
  if counter != 0:
    overall_sentiment = overall_sentiment/counter
  else:
    overall_sentiment = 0

  # over all assume neutral
  pos_neg = "[Neutral]"
  if overall_sentiment > 0:
    pos_neg = "[Positive]"
  if overall_sentiment < 0:
    pos_neg = "[Negative]"

  sentiment = "Overall sentiment is {}\n".format(pos_neg)
  print(sentiment)

  key_search = False
