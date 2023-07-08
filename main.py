import time

import requests
from bs4 import BeautifulSoup

"""
#For single job, use the code listed belowHunch
job=soup.find('li',class_='clearfix job-bx wht-shd-bx')
#print(job)

company_name = job.find('h3',class_="joblist-comp-name").text.replace(' ','')
#print(company_name)

skills = job.find('span', class_='srp-skills').text.replace(' ','')
#print(skills)

print(f'''
Company Name : {company_name}
Required skills : {skills}
''')

published_date = job.find('span',class_='sim-posted').text.replace(' ','')
#print (published_date)

more_info= job.header.h2.a['href']
#more_info= job.find('h2')
print(more_info)


#taking inputs from the user to filter out unfamiliar skills
print('''Put some skill that you are unfamiliar with''')
unfamiliar_skill = input('>')
print(f'''Filering out {unfamiliar_skill}\n''')
"""

# Taking multiple inputs from the user
num_inputs = 2
unfamiliar_skill = []
for _ in range(num_inputs):
    user_input = input('Please enter any unfamiliar skills that should be excluded from the job search:')
    unfamiliar_skill.append(user_input)
# print(unfamiliar_skill)

#Defining a function
def find_jobs():

    # send request to scrape the website
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)

    # parse the whole thing using beautifulsoup parser
    soup = BeautifulSoup(html_text, 'lxml')
    # print(soup)

    # Find all the jobs present in the page
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    # print(jobs)

    for index,job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').text.replace(' ', '')
        if 'few' in published_date:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            for items in unfamiliar_skill:
                if items.upper() not in skills:
                    with open(f'posts/{index}.txt','w') as f:
                        f.write(f'''Company Name: {company_name.strip()}\n''')
                        f.write(f'''Required skills: {skills.strip()}\n''')
                        f.write(f'''More Info: {more_info}\n''')
                        print(f'File saved : {index}')

                        """
                        print(f'''Company Name:{company_name.strip()}''')
                        print(f'''Required skills:{skills.strip()}''')
                        print(f'''More info:{more_info}\n''')
                        """

#Calling the find_jobs function through if clause
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)

# next task in this project : Creating a multiple file with different job vacancies based on skill set as per the question asked to the user

