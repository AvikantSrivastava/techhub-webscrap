from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re
import json

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get("https://www.codechef.com/problems/school")

problem_name = []
problem_link = []
content = driver.page_source
driver.close()
soup = BeautifulSoup(content)

soup1 = soup.find('tbody')
soup2 = soup1.find('tbody')

for a in soup2.findAll('a', href=re.compile('/problems/') ):
    name = a.text
    link = 'https://www.codechef.com' + a['href']
    problem_name.append(name)
    problem_link.append(link)
    print("{}    {} ".format(name,link) )
problem_vault = dict(zip(problem_name,problem_link))

import json
with open('problems.json', 'w') as fp:
    json.dump(problem_vault, fp)
