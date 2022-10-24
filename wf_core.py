import io
import random
import string  # to process standard python strings
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#import main2
import wf_datagen
import wf_dataprocessing
import wf_visualization

# import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('popular', quiet=True)  # for downloading packages
# nltk.download('punkt') # first-time use only
# nltk.download('wordnet') # first-time use only

data_orginal = wf_datagen.file_reader()
#print("Reading the DB")
#user_name1 = str(input("Enter your name: "))

raw = data_orginal.read()
raw = wf_dataprocessing.to_lower(raw)
#raw = raw.lower()  # converts to lowercase

sent_tokens = wf_dataprocessing.list_of_sent(raw)  # converts to list of sentences
word_tokens = wf_dataprocessing.list_of_word(raw)  # converts to list of words
lemmer = nltk.stem.WordNetLemmatizer()


# WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "nods", "hi there", "hello", "I am glad! You are talking to me"]


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if "count" in user_response or req_tfidf == 0:
        scraped = wf_datagen.web_scrapping(user_response.split(" ")[1])
        if len(scraped) > 0:
            return scraped
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response


flag = True
user_name = str(input("Enter your name: "))
print("SPARKY: My name is SPARKY. I will answer your queries about Arizona State University. If you want to exit, "
      "type Bye!")
while flag == True:
    user_response = input()
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response == 'thanks' or user_response == 'thank you':
            flag = False
            print("SPARKY: You are welcome..")
        else:
            if greeting(user_response) != None:
                print("SPARKY: " + greeting(user_response))
            else:
                print("SPARKY: ", end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("SPARKY: Bye " + user_name + "! take care..")
        wf_visualization.survey()
        #main2.f1()
        # untitled2.f1()