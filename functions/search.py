import requests
from bs4 import BeautifulSoup
import json, numpy as np
import re
import sys
from googlesearch import search
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pyrebase
from firebase import firebase

firebase = firebase.FirebaseApplication("https://honestly-on-firebase.firebaseio.com/", None)

# to search
searchword = ""


def get_results(query):
    result_list = []
    for j in search(query, tld="com", num=10, stop=10, pause=3):
        result_list.append(j)
    return result_list


def combine_strings(links):
    articles = ""
    for link in links:
        articles += ((scrape_article(link)))
    articles = cutString(articles)
    print(articles)
    return articles


def cutString(fullText):
    stop = stopwords.words('english')
    fullText = word_tokenize(fullText.lower())
    fullText = [w for w in fullText if not w in stop]
    listToStr = ' '.join([str(elem) for elem in fullText])
    return listToStr


def scrape_article(url):
    res = requests.get(url)
    if (res.status_code == 200 and 'content-type' in res.headers and
            res.headers.get('content-type').startswith('text/html')):
        html = res.text
    else:
        return "Error loading webpage: " + url

    soup = BeautifulSoup(html, 'html.parser')

    h1 = soup.body.find('h1')
    root = h1
    if(root == None):
        return ""
    #article may not have fewer than 4 paragraphs
    while root.name != 'body' and len(root.find_all('p')) < 4:
        root = root.parent

    ps = root.find_all(['h2', 'h3', 'h4', 'h5', 'p', 'pre'])
    ps.insert(0, h1)
    content = [tag2md(p) for p in ps]
    strings = str(content).lower()

    strings = strings.replace("\\r", "")
    strings = strings.replace("\\n", "")
    listquery = searchword.split()
    for w in listquery:
        strings = strings.replace(w, "*****")
    filter = ''.join([chr(i) for i in range(1, 32)])
    strings.translate(str.maketrans('','', filter))
    pat = re.compile(r'[^A-za-za-z]+')
    answer = re.sub(pat, '', strings)
    return answer
def tag2md(tag):
    if tag.name == 'p':
        return tag.text
    elif tag.name == 'h1':
        return f'{tag.text}\n{"=" * len(tag.text)}'
    elif tag.name == 'h2':
        return f'{tag.text}\n{"-" * len(tag.text)}'
    elif tag.name in ['h3', 'h4', 'h5', 'h6']:
        return f'{"#" * int(tag.name[1:])} {tag.text}'
    elif tag.name == 'pre':
        return f'```\n{tag.text}\n```'
def printResult(query):
    combine_strings(get_results(query))

if __name__=="__main__":
    query= str(sys.argv[1].lower())
    searchword=query
    ret = combine_strings(get_results(query))
    data = {
        'results': ret,
        'textfield': searchword
    }
    result = firebase.post('/honestly-on-firebase/searches', data)
    print(result)