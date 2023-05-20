from bs4 import BeautifulSoup
import requests



def findJobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    # print(html_text.text)

    soup = BeautifulSoup(html_text, 'lxml')


    # =========================================
    print("Oum some skill that you are not familiar with.")
    unfamiliar_skills = input(">")
    print(f"filtering out {unfamiliar_skills}")
    # ==========================================

    # Extract all jobs from page and extract important information.
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    # print(len(jobs))
    for job in jobs:
        job_posted = job.find('span', class_='sim-posted').span.text
        if 'few' in job_posted:

            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')

            skills = job.find('span', class_='srp-skills').text

            more_info = job.header.h2.a['href'] 
            if unfamiliar_skills not in skills:

                print(f"Company Name : {company_name}")
                print(f"Required Skills : {skills}")
                print(f"Published Date: {job_posted}")
                print(f"For More info: {more_info}")
                print("**********************")





findJobs();