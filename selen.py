import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
url="https://github.com/oguzhanmavii"

driver.get(url)
print("siteden çıkış yapılıyor")
time.sleep(3)
print("bot sistemden çıktı")
time.sleep(1.5)
sys.exit(0) 

