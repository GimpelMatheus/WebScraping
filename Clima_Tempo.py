import requests
from bs4 import BeautifulSoup  
import pandas as pd

def clear_duplicate(data):
    """ Clean duplicated data"""

    clean_data = []

    for i in range(0, len(data), 2):
        clean_data.append(data[i])
    
    return clean_data

url = "https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/107/belohorizonte-mg"

#if we use request.get and then call the html so we need to use .text or html.text
html = requests.get(url).text 
bs = BeautifulSoup(html,"lxml")

#Collectin Data from the website
min_temp = [min.get_text().strip() for min in bs.find_all("span", class_="min-temp")]
max_temp = [max.get_text().strip() for max in bs.find_all("span", class_="max-temp")]

min_temp = clear_duplicate(min_temp)
max_temp = clear_duplicate(max_temp)

rain = [rainy.get_text().strip() for rainy in bs.find_all("p", class_="-gray _flex _align-center")]
date = []
#retiring the blanks and collecting date 
for time in bs.find_all("p", class_= "-gray _float-l _max-w-75-pct"):
    date.append(time.get_text().strip())


df = pd.DataFrame({'date':[day for day in date],
'min_temp':[min for min in min_temp],
'max_temp':[max for max in max_temp],
"rainy":[rainy_day for rainy_day in rain]})

