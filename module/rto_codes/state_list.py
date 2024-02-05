# https://www.coverfox.com/rto/
def getStateUrl():
     import bs4 
     from bs4 import BeautifulSoup
     import requests
     html = requests.get('''https://www.coverfox.com/rto/''')
     soup = BeautifulSoup(html.text,'html.parser')
     table = soup.find('table',{'class':'art-table'})
     td = table.find_all('td')
     state_name = []
     count = 0
     while count < len(td):
          state_name.append(td[count].text.replace('\n',''))
          count = count + 2 
     state_name = list(filter(None,state_name))
     count = 1
     for state in state_name:
          print(f"Enter {count} for {state} ")
          count+=1
     option = int(input("Select Any One State From Above : "))
     selected_state = state_name[option - 1]
     selected_state = selected_state.replace(" ",'-')
     selected_state = selected_state.replace("-RTO",'').lower()
     # print(selected_state)
     url = '''https://www.coverfox.com/rto/''' + selected_state
     # print(url) 
     return url 