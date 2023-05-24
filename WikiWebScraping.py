
# import relevant libraries

from bs4 import BeautifulSoup
import requests

Wikidata = requests.get("https://en.wikipedia.org/wiki/Casiopea")
htmldata = BeautifulSoup(Wikidata.content, 'html.parser')
result = htmldata.prettify()
res = [i for i in range(len(result)) if result.startswith("<a href=\"/wiki", i)]
for i in range(len(res)):
    curlink = result[res[i] + 9:res[i] + (result[res[i]:res[i]+200]).find('" title')]
    if(curlink and curlink.find(':') < 0):
        print("https://en.wikipedia.org" + curlink)