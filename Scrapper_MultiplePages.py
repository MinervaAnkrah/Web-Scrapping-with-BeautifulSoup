from bs4 import BeautifulSoup
import requests
import csv


with open('Scrapper_multiple_pages.csv', 'w+', newline='', encoding='utf8') as data:
        thewriter = csv.writer(data)
        headers = ['JobTitle', 'HiringCompany', 'Location', 'EmploymentType', 'Salary', 'JobFunction', 'DatePosted']
        thewriter.writerow(headers)
        for i in range (1,73):
            url = f'https://www.jobberman.com.gh/jobs?page={i}'
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            results = soup.find_all('div', class_='mx-5 md:mx-0 flex flex-wrap col-span-1 mb-5 bg-white rounded-lg border border-gray-300 hover:border-gray-400 focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-gray-500')

            for result in results:
                JobTitle = result.find('p', class_='text-lg font-medium break-words text-link-500').text.strip()
                HiringCompany = result.find('p', class_='text-sm text-link-500').text.strip()
                AboutJob = result.find('div', class_='flex flex-wrap mt-3 text-sm text-gray-500 md:py-0').text.split('\n')
                Location = AboutJob[2]
                EmploymentType = AboutJob[5]
                if len(AboutJob) == 11:
                    Salary = AboutJob[8]
                else:
                    Salary = AboutJob[8]+' '+AboutJob[10]
                if Salary == 'GHS Confidential':
                    Salary = 'Not Available'
                JobFunction = result.find('p', class_='text-sm text-gray-500 text-loading-animate inline-block').text.strip()
                JobFunction = JobFunction.split('\n: ')[1]
                DatePosted = result.find('p', class_='ml-auto text-sm font-normal text-gray-700 text-loading-animate').text
                toAdd = [JobTitle, HiringCompany, Location, EmploymentType, Salary, JobFunction, DatePosted]
                thewriter.writerow(toAdd)
        