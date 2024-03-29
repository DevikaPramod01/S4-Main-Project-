from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# configure the followings
#chrome_driver_path = 'D:/Downloads/chromedriver_win32/chromedriver.exe'
chrome_driver_path ='C:/Users/devik/Desktop/S4 main project/prjt/chromedriver-win64/chromedriver-win64/chromedriver.exe'

total_page = 15
page_size = 50
       
path_template = 'http://addgene.org/search/catalog/plasmids/?page_number={}&page_size={}&q=e.coli'
driver = webdriver.Chrome(chrome_driver_path)

with open('plasmid_ids.txt', 'w') as f:
    for i in range(1,(total_page+1)):
        driver.get(path_template.format(i, page_size))
        page = driver.page_source
        for line in page.split('\n'):
            if '<div class="col-xs-10">#' in line:
                line = line.strip()
                ## example: <div class ="col-xs-10" >  # 107251</div>
                id = line.split('#')[1].split('</div>')[0]
                f.write(id+'\n')
driver.close()







