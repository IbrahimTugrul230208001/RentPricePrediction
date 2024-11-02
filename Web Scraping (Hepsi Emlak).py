import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_main_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    listings = soup.find_all('div', class_='list-view-content')

    data = []
    for listing in listings:
        try:
            price_tag = listing.find('span', class_='list-view-price')
            price = price_tag.text.strip() if price_tag else "N/A"

            location_tag = listing.find('span', class_='list-view-location')
            location = location_tag.text.strip() if location_tag else "N/A"

            rooms = listing.find('span', class_='houseRoomCount').text.strip() if listing.find('span', class_='houseRoomCount') else "N/A"
            area = listing.find('span', class_='squareMeter').text.strip() if listing.find('span', class_='squareMeter') else "N/A"
            floor = listing.find('span', class_='floortype').text.strip() if listing.find('span', class_='floortype') else "N/A"

            # Append data only if essential fields are present
            if price != "N/A" and rooms != "N/A" and area != "N/A":
                print(f"Scraped: {price}, {rooms}, {area}, {floor}, {location}")
                data.append([price, rooms, area, floor, location])
            else:
                print("Essential data missing. Skipping this listing...")
        except Exception as e:
            print(f"An error occurred: {e}. Skipping this listing...")

    return data

# Scrape the data from multiple pages
all_listings_data = []
for i in range(1, 398):  # Assuming 50 pages
    url = f"https://www.hepsiemlak.com/ankara-kiralik/daire?p32=80000&p33={i}"
    listings_data = scrape_main_page(url)
    all_listings_data.extend(listings_data)
    time.sleep(3)  # To avoid overloading the server with requests, wait for 1 second between requests

# Store the scraped data in a Pandas DataFrame
df = pd.DataFrame(all_listings_data, columns=['Price', 'Rooms', 'Area', 'Floor', 'Location'])

# Display the DataFrame
print(df)
df.to_csv("rent_price_hepsiemlak(4).csv")