import urllib.request #Handling URL

from bs4 import BeautifulSoup #Handling or parsing html files

import nltk #toolkit
nltk.download('stopwords') #or is was extracted

from nltk.corpus import stopwords


#get the info from website
response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/apple')
html = response.read()

soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)

tokens = [t for t in text.split()]

sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(30, cumulative=False)

