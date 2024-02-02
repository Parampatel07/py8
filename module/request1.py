import requests
from bs4 import BeautifulSoup

html = requests.get('''https://www.cricbuzz.com/live-cricket-scorecard/37336/csxi-vs-inds-3-day-warm-up-match-india-tour-of-england-2021''')

# print(html.text)

soup = BeautifulSoup(html.text,'html.parser')
# print(soup.prettify())

players = soup.find_all('a',{'class':'cb-text-link'})
# print(players)

player_name = []
for i in players:
     player_name.append(i.text)

runs = soup.find_all('div',{'class':'cb-col cb-col-8 text-right text-bold'})
runs_text = []
for i in runs:
     # print(i)
     runs_text.append(i.text)
# print(player_name[0])
count = 1
while count <=11:
     print(f"{player_name[count]:30}  {runs_text[count]}")
     count+=1
