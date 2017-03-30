from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

example_tweet = "A heavy rain fall is happening in Akuressa town, Matara. The area is already flooded up to nearly three feets. We need help immediately."

words = word_tokenize(example_tweet)

stop_words = set(stopwords.words("english"))

filtered_tweet_1 = [w for w in words if w not in stop_words]

print(filtered_tweet_1)

ps = PorterStemmer()

for w in filtered_tweet_1:
    print(ps.stem(w))

#This piece of code removes the stop words from an eample tweet
#and then stem the words    
