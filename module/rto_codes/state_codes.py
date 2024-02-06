from state_list import getStateUrl
import requests
from bs4 import BeautifulSoup
import pandas

def getRtoCode():
     url = getStateUrl()
     # print(url)
     html = requests.get(url)
     soup = BeautifulSoup(html.text,'html.parser')
     td = soup.find_all('td')
     # print(td)
     state_list = []
     for i in td:
          state_list.append(i.text.replace('\n',''))
          # state_list.remove('')
     # print(state_list)
     state_list = list(filter(None,state_list))
     temp = []
     formated_data = []
     count = 0 
     while count < len(state_list):
          temp = [state_list[count],state_list[count+1]]
          formated_data.append(temp)
          count+=2
     return formated_data

def writeExcel():
     data = getRtoCode()
     df = pandas.DataFrame(data)
     excel = pandas.ExcelWriter('rto.xlsx',engine='xlsxwriter')
     df.to_excel(excel,"sheet1",index=False,header=False)
     excel.close()

writeExcel()