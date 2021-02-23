from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint

PATH = r"C:\Users\Michael\Desktop\chromedriver.exe"

driver = webdriver.Chrome(PATH)

f = open("ryukyushimpo_links.txt")
start_urls = [url.strip() for url in f.readlines()]
f.close()

output_file = open("ryukyu_shimpo_articles.txt", "w", encoding="utf-8")

for url in start_urls:
	driver.get(url)
	time.sleep(randint(4,6))

	# check to see if a Japanese version of the article exists;
	# if not, move to next iteration of the loop
	try:
		go_to_japanese = WebDriverWait(driver, 2).until(
			EC.presence_of_element_located((By.LINK_TEXT, "Go to Japanese"))
		)
	except:
		print("No translation for " + url)
		continue
	
	english_article = driver.find_element_by_css_selector(".recent.post").text

	go_to_japanese.click()
	time.sleep(randint(4,6))
	japanese_article = driver.find_element_by_id("detail").text
	output_file.write(english_article)
	output_file.write("\n\n")
	output_file.write(japanese_article)
	output_file.write("\n\n")

output_file.close()

driver.quit()