
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(URL)

soup = bs(page.text, 'html.parser')

start_table = soup.find('table')

temp_list = []

tableRows = start_table.find_all('tr')

for i in tableRows:
    td = i.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
    

    
names = []
distance = []
mass =[]
radius = []


for i in range(1 , len(temp_list)):
    names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])


data = pd.DataFrame(list(zip(names , distance , mass , radius)) , columns=["Star_Names" , "Distance" , "Mass" , "Radius"])

data.to_csv('stars.csv')








