from bs4 import BeautifulSoup
import requests
import time

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        posted_status = job.find('span', class_ = 'sim-posted').text

        if 'today' in posted_status:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.strip()
            location = job.find('span').text.strip()
            skills = ', '.join([skill.strip() for skill in job.find('span', class_ = 'srp-skills').text.split(',')])
            job_link = job.header.h2.a['href']
            
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f'Company name: {company_name} \n')
                f.write(f'Location: {location} \n')
                f.write(f'Required skills: {skills} \n')
                f.write(f'More info: {job_link} \n')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f"Waiting {time_wait} minutes")
        time.sleep(time_wait * 60)
