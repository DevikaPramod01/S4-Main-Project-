from selenium import webdriver
# The BeautifulSoup module
from bs4 import BeautifulSoup
    
# you have to run the script after running collect_ids.py
# configure the following
#chrome_driver_path = 'D:/Downloads/chromedriver_win32/chromedriver.exe'
chrome_driver_path = 'C:/Users/devik/Desktop/S4 main project/prjt/chromedriver-win64/chromedriver-win64/chromedriver.exe'

path_template = 'http://www.addgene.org/{}/sequences/'
plasmid_ids = [line.rstrip('\n') for line in open('plasmid_ids.txt')]
driver = webdriver.Chrome(chrome_driver_path)
      
n = 0
with open('all_plasmid_dna.txt', 'w', encoding='utf-8') as f:
    for id in plasmid_ids:
        path = path_template.format(id)
        driver.get(path)
        page = driver.page_source
        parser = BeautifulSoup(page, "lxml")
        list_of_attributes = {"class": "copy-from form-control"}
        tags = parser.findAll('textarea', attrs=list_of_attributes)
        n += 1
        for tag in tags:
            tag = tag.text
            lines = tag.split('\n')
            ref = lines[0].strip()
            lines = lines[1:]
            dna = ('').join(lines).strip()
            try:
                f.write('{}, {},"{}",{}\n'.format(n, id, ref, dna.upper()))
            except Exception as es:
                print('problem with id:', id, es)

driver.close()




