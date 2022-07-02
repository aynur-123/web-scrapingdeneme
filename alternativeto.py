
#from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://alternativeto.net/software/instagram/")





#driver.maximize_window() #tam ekran yapar

search = driver.find_elements(By.CLASS_NAME, "Heading_h2__7oYDQ")
print("alternatifleri şunlardır:")
print([s.text for s in search])
instagram = [s.text for s in search]
facebook = [s.text for s in search]


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://alternativeto.net/software/instagram/about/")
search2 = driver.find_elements(By.CLASS_NAME, "CommonComment_comment__trcbX")
print("yorumlar şunlardır:")

for s2 in search2:
    print(s2.text)



time.sleep(1)


driver.close()