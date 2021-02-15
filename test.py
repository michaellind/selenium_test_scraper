from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint

PATH = r"C:\Users\Michael\Desktop\chromedriver.exe"

driver = webdriver.Chrome(PATH)

f = open("urllist.txt")
start_urls = [url.strip() for url in f.readlines()]
f.close()

output_file = open("output.txt", "w", encoding="utf-8")

for url in start_urls:
	driver.get(url)
	time.sleep(randint(15, 25))
	article_title = driver.find_element_by_class_name("module-header").text
	article_body = driver.find_element_by_class_name("module-body").text
	output_file.write(article_title)
	output_file.write("\n")
	output_file.write(article_body)
	output_file.write("\n")

output_file.close()
driver.quit()
