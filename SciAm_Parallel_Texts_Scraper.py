from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from random import randint
# Some of these import statements will probably be unnecessary

# The aim of this script is to scrape all of the English and Japanese
# sample texts from the Nikkei Science website.

# Set path to chromedriver.exe
PATH = r"C:\Users\Michael\Desktop\chromedriver.exe"

driver = webdriver.Chrome(PATH)

# Change these to set the minimum and maximum delay after a new page is loaded
# (Should be reasonable to avoid rudely slamming the server with requests)
sleep_min = 2
sleep_max = 10

# There must be a list of links (e.g., one made using nikkeisciencelinks.py)
# in order for the following code to work
f = open("nikkei_science_links.txt")
article_urls = [url.strip() for url in f.readlines()]
f.close()

# One file for the English articles, one file for the Japanese translations,
# and one for both, with source texts and translations printed adjacently
en_output = open("sciam_en.txt", "w", encoding="utf-8")
ja_output = open("sciam_ja.txt", "w", encoding="utf-8")
ja_en_output = open("sciam_ja_en.txt", "w", encoding="utf-8")

for url in article_urls:
	driver.get(url)
	print("Current URL: " + url)
	time.sleep(randint(sleep_min, sleep_max))

	# The pages have bizarrely coded layouts,
	# hence the spaghetti code that follows
	article_titles = driver.find_element_by_class_name("title-article")
	english_title = article_titles.find_element_by_tag_name("h1").text
	japanese_title = article_titles.find_element_by_css_selector(
		".large.bold").text

	author_names = driver.find_element_by_class_name(
		"table-author").find_elements_by_tag_name("td")
	english_names = ""
	japanese_names = ""

	for names in author_names:
		if names.get_attribute("class") == "text-en":
			english_names = names.text
		else:
			japanese_names = names.text

	table = driver.find_element_by_class_name("table-english")
	cells = table.find_elements_by_tag_name("td")

	japanese_text = ""
	english_text = ""

	japanese_text = japanese_text + japanese_title +"\n"+ japanese_names +"\n"
	english_text = english_text + english_title + "\n" + english_names + "\n"

	for cell in cells:
		attr = cell.get_attribute("class")
		if (attr != "text-ja") and (attr != "p-0"):
			english_text = english_text + cell.text + "\n"
		elif attr == "text-ja":
			japanese_text = japanese_text + cell.text + "\n"

	en_output.write(english_text + "\n")
	ja_output.write(japanese_text + "\n")
	ja_en_output.write(english_text + "\n" + japanese_text + "\n")


en_output.close()
ja_output.close()
ja_en_output.close()
driver.quit()