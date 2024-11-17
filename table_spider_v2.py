import os.path
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_and_append_to_csv(url, csv_file='output.csv'):
    # Send request and parse the response
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract all table rows
    rows = soup.find_all('tr')
    data = []

    for row in rows:
        money_text = None
        name_text = None
        company_text = None

        try:
            # Extract data
            money = row.find('strong')
            money_text = money.text.strip() if money else None

            name = row.find('a', class_='text-nowrap')
            name_text = name.text.strip() if name else None

            td_elements = row.find_all('td')
            company_text = td_elements[-1].get_text(strip=True) if td_elements else None

            # Append data only if all fields are present
            if money_text and name_text and company_text:
                data.append([money_text, name_text, company_text])

        except Exception as e:
            print(f'Error processing row: {e}')
            continue

    # Convert data to a DataFrame
    df = pd.DataFrame(data, columns=['Money', 'Name', 'Company'])

    # Write to CSV
    if not os.path.exists(csv_file):
        df.to_csv(csv_file, index=False)
    else:
        df.to_csv(csv_file, mode='a', header=False, index=False)

    print(f'Successfully written {len(data)} records to {csv_file}')

# Example usage
base_url = 'https://www.sunshineliststats.com/?page={}&provinceid=2&year=2024'
csv_filename = 'output.csv'

for page_number in range(7,33):
    url = base_url.format(page_number)
    print(f'Scraping page {page_number}...')
    scrape_and_append_to_csv(url, csv_file=csv_filename)
print("Scraping completed")

