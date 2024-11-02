import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

def scrape_main_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the listings on the page
    listings = soup.find_all('div', class_='manJWF')  # Adjusted class name based on provided HTML

    data = []
    for listing in listings:
        try:
            # Use regex to find relevant data-test-selectors
            price = listing.find('p', {'data-test-selector': re.compile(r'listing-item-price-\d+')})
            rooms = listing.find('span', {'data-test-selector': re.compile(r'listing-item-property-room-count-\d+')})
            floor = listing.find('span', {'data-test-selector': re.compile(r'listing-item-property-floor-number-\d+')})
            area = listing.find('span', {'data-test-selector': re.compile(r'listing-item-property-gross-square-\d+')})
            location = listing.find('span', {'data-test-selector': re.compile(r'listing-item-location-\d+')})

            # Get text if the elements exist
            price = price.text.strip() if price else "N/A"
            rooms = rooms.text.strip() if rooms else "N/A"
            floor = floor.text.strip() if floor else "N/A"
            area = area.text.strip() if area else "N/A"
            location = location.text.strip() if location else "N/A"

            # Append data only if essential fields are present
            if price != "N/A" and rooms != "N/A":
                print(f"Scraped: {price}, {rooms}, {area}, {floor}, {location}")
                data.append([price, rooms, area, floor, location])
            else:
                print("Essential data missing. Skipping this listing...")

        except Exception as e:
            print(f"An error occurred: {e}. Skipping this listing...")

    return data

# Scrape the data from the main page
all_listings_data = []

# Scrape the initial page (page 1)
initial_url = "https://www.emlakjet.com/kiralik-konut/ankara/"
listings_data = scrape_main_page(initial_url)
all_listings_data.extend(listings_data)

# Loop through pages 2 to 50
for i in range(2, 51):  # Iterate from page 2 to page 50
    url = f"https://www.emlakjet.com/kiralik-konut/ankara/{i}/"  # Create the URL for each page
    listings_data = scrape_main_page(url)  # Scrape data from the current page
    all_listings_data.extend(listings_data)  # Add the scraped data to the overall list

# Store the scraped data in a Pandas DataFrame
df = pd.DataFrame(all_listings_data, columns=['Price', 'Rooms', 'Area', 'Floor', 'Location'])

# Display the DataFrame
print(df)
df.to_csv('rent_price_listings(1).csv', index=False)
