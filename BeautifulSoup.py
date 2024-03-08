import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://ghanayellowpages.com/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div', class_='hp-listing__content')

with open('jobs_listed.csv', 'w', newline='', encoding='utf8') as data:
    thewriter = writer(data)
    header = ['CompanyName', 'Location', 'ServiceOfferings', 'ListingDate']
    thewriter.writerow(header)
    for result in results:
        companyName = result.find('h4', class_='hp-listing__title').text.strip()
        location = result.find('div', class_='hp-listing__location').text.strip()
        services = result.find('div', class_='hp-listing__categories hp-listing__category').text.strip()
        dateAdded = result.find('time', class_='hp-listing__created-date hp-listing__date hp-meta').text.replace("Added on", '').strip()
        toAdd = [companyName, location, services, dateAdded]
        thewriter.writerow(toAdd)
