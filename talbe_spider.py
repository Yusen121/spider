import os.path

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.sunshineliststats.com/?page=7&provinceid=2&year=2024"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

rows = soup.find_all('tr')

data = []

for row in rows:
    money_text = None
    name_text = None
    company_text = None
    try:
        money = row.find('strong')
        if money:
            money_text = money.text.strip() if money else None
        name = row.find('a', class_='text-nowrap')
        if name:
            name_text = name.text.strip() if name else None

        td_elements = row.find_all('td')
        company_text = td_elements[-1].get_text(strip=True) if td_elements else None

        if money_text and name_text and company_text:
            data.append([money_text, name_text, company_text])
    except Exception as e:
        print(f'Error processing row: m {e}. Row content: {row}')
        continue
df = pd.DataFrame(data, columns=['Money', 'Name', 'Company'])
csv_file = 'output.csv'

if not os.path.exists(csv_file):
    df.to_csv(csv_file, index=False)
else:
    df.to_csv(csv_file, mode='a', header=False, index=False)
print(f'Successfully written {len(data)} record to {csv_file}')



