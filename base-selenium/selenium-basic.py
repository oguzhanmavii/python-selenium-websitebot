from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time



driver=webdriver.Chrome(ChromeDriverManager().install())
url="https://github.com"

driver.get(url)
time.sleep(1.5)
driver.maximize_window()

driver.save_screenshot("github.com-homepage.png")
time.sleep(1.8)
url2="https://github.com/oguzhanmavii"
driver.get(url2)
time.sleep(3)
print(driver.title)
if "oguzhanmavi" in driver.title:
    driver.save_screenshot("github-oguzhanmavi.png")

driver.back()
print("bot gerekli işlemleri tamamladı")
time.sleep(1)
driver.close()   