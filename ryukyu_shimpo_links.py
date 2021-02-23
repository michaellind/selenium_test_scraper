from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint

PATH = r"C:\Users\Michael\Desktop\chromedriver.exe"

driver = webdriver.Chrome(PATH)

i = 197 # set to page to count down from

output_file = open("ryukyushimpo_links.txt", "w", encoding="utf-8")

while i > 0:
	driver.get("http://english.ryukyushimpo.jp/page/" + str(i))
	time.sleep(randint(2, 7))
	article_links = driver.find_element_by_id("content").find_elements_by_tag_name("a")
	for article_link in article_links:
		href = article_link.get_attribute("href")
		if href is not None:
			output_file.write(href)
			output_file.write("\n")
	i = i - 1
	time.sleep(randint(2, 7))

output_file.close()

driver.quit()
