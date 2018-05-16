import re
import csv
import nltk

"""docstring for twitterClean"""
def __init__(self):
    super(twitterClean, self).__init__()
    
def renameUser(corpus):
        _new = []      
        for _temp in corpus:
            _temp =  re.sub( r'(^|[^@\w])@(\w{1,15})\b','',_temp)
            _new.append(_temp)

        return _new

def removeHashtag(corpus):
    _new = []
    for _temp in corpus:
        _temp = re.sub(r'#(\w+)', '', _temp)
        _new.append(_temp)

    return _new

def removeURL(corpus):
    _new = []
    for _temp in corpus:
        _temp = re.sub(r'http:\S+', '', _temp, flags=re.MULTILINE)
        _temp = re.sub(r'https:\S+', '', _temp, flags=re.MULTILINE)
        _new.append(_temp)

    return _new

def removeEmoticon(corpus):
    _new = []
    emoticons_str = r"(?:[:=;B\-][oO\"\_\-]?[\-D\)\]\(\]/\\Op3]{2,3})"
    for _temp in corpus:
        _temp.replace(emoticons_str, '')
        _temp = re.sub(r'[^\x00-\x7F]', '', _temp)
        _new.append(_temp)

    return _new

def getTweetData(filename="dataset/Indonesian_Tweets.tsv"):
    #Gain large corpus of tweets
    toFeed = []
    rawSentence = []
    with open(filename, 'rU') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\n', quotechar='|')
        for spam in spamreader:
            rawSentence.append(spam)
    corpusSentence =[]
    for individualSentence in rawSentence:
        if individualSentence == []:
            pass
        else:
            corpusSentence.append(individualSentence[0])
    
    # corpusSentence = self.text.removeAll(corpusSentence)
    _temp = removeURL(corpusSentence)
    _temp = renameUser(_temp)
    _temp = removeHashtag(_temp)
    _temp = removeEmoticon(_temp)
    
    for sentences in _temp:
        token = nltk.wordpunct_tokenize(sentences.lower())
        toFeed.append(token)
    
    return toFeed