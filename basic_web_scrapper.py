

import requests
from bs4 import BeautifulSoup
import csv



# ---------------------Below code scrap data from worldometer including headers (titles)----------in CSV file-----------code by Ritik sharma------------------------------
# ======BASIC WEB SCRAPPER . PROGRAM NUMBER 8==========================
url = "https://www.worldometers.info/world-population/population-by-country/"  


response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve the webpage")
    exit()


html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')


table = soup.find('table')
if table is None:
    print("Table not found! Check the website's structure.")
    exit()


rows = table.find_all('tr')
data = []

headers = [header.text.strip() for header in rows[0].find_all('th')] if rows[0].find_all('th') else []


if headers:
    data.append(headers)


for row in rows[1:]: 
    cols = row.find_all(['td', 'th']) 
    cols = [col.text.strip() for col in cols]
    data.append(cols)


with open('output2.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data successfully saved to output.csv")