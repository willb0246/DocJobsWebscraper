import requests
import sys
import datetime
from bs4 import BeautifulSoup

scrape_date = datetime.date.today()

sys.stdout = open("DocJobsScrape.txt" + str(scrape_date), "w")

links = []

URL = 'https://www.docjobs.com/jobs/list/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

job_board_div = soup.find(id="main")

job_links = job_board_div.find_all('a', class_='job-item-link')


for job_link in job_links:
    links.append("https://www.docjobs.com" + str(job_link['href']))


for i in links:

    URL = str(i)

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    header_box = soup.find_all('section', class_="job-application-overview-section")

    for valuables in header_box:
        Title = valuables.find('h4')
        Details = valuables.findChildren('p', class_="job-application-overview-details")
        CoName = list(Details[0])
        Location = list(Details[1])
        Contact = valuables.find('a', class_="employer-questions")
        if Contact:
            Category = Contact['href']
        else:
            Category = []

        print(Title.text)
        print(CoName)
        print(Location)
        print(Category)
        print("========================================================================================")


sys.stdout.close()

