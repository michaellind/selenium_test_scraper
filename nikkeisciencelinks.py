from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint

PATH = r"C:\Users\Michael\Desktop\chromedriver.exe"

driver = webdriver.Chrome(PATH)

i = 1

output_j_file = open("nikkei_science_links.txt", "w", encoding="utf-8")

while i < 22:
	driver.get("https://www.nikkei-science.com/?cat=8&paged=" + str(i))
	print("i = " + str(i))
	time.sleep(randint(1, 3))
	j_links = driver.find_elements_by_partial_link_text("続きを読む")
	for j_link in j_links:
		href = j_link.get_attribute("href")
		if href is not None:
			print(href)
			output_j_file.write(href)
			output_j_file.write("\n")

	i = i + 1

output_j_file.close()

driver.quit()
