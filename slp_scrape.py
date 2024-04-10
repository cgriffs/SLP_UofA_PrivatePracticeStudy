import requests
from bs4 import BeautifulSoup

url = "https://asapp.ca/item/page/10/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(" ")

# Assuming each SLP entry is contained within a specific HTML structure
slps = soup.find_all('div', class_='item-data')  # This 'div' and class are placeholders

for slp in slps:
    # Extracting SLP Name
    name = slp.find('h3').text
    
    # Extracting Age Served
    ages_served = [age.text for age in slp.find_all('span', class_='item-category')]
    
    # Extracting Address
    address = slp.find('span', class_='value').text  # Assuming first 'span class="value"' is always address
    
    # Extracting Website
    website = slp.find('a')['href']  # Assuming first 'a' tag inside a 'value' class span is always the website link
    
    # Extracting Features
    features = [feature.text.strip() for feature in slp.find_all('span', class_='filter-hover')]
    
    #print(f"Name: {name}")
    print(f"Ages Served: {', '.join(ages_served)}")
    print(f"Address: {address}")
    print(f"Website: {website}")
    print(f"Features: {', '.join(features)}\n")