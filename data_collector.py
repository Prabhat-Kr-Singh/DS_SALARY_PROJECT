##author: Prahat Kumar Singh


import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Users/HP/Documents/DS_SALARY/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)

