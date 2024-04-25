from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

for job in jobs:
    posted_status = job.find('span', class_ = 'sim-posted').text

    if 'today' in posted_status:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
        location = job.find('span').text.strip()
        skills = ', '.join([skill.strip() for skill in job.find('span', class_ = 'srp-skills').text.split(',')])
        print(f'''
        Company name: {company_name}
        Location: {location}
        Required skills: {skills} \n      
            ''')
