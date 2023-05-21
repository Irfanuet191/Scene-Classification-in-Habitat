from bs4 import BeautifulSoup
import requests
import numpy
Word_list=requests.get("https://gre.magoosh.com/flashcards/vocabulary/high-frequency-words/vindicate")
data=BeautifulSoup(Word_list.text,"html.parser")
Qdata=data.findAll("h3",attrs={"class":"flashcard-word"})
print(Qdata)