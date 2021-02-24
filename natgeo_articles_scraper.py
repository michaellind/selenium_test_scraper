from selenium import webdriver
import time
from random import randint

# Set path to chromedriver.exe
PATH = r"C:\Users\Michael\Desktop\chromedriver.exe"

driver = webdriver.Chrome(PATH)

sleep_min = 5
sleep_max = 15

f = open("NATGEO_URLS.TXT")
article_urls = [url.strip() for url in f.readlines()]
f.close()

output_file = open("natgeo_articles.txt", "w", encoding="utf-8")

for url in article_urls:
	driver.get(url)
	
	article_header = driver.find_element_by_class_name("articleTitleBox").text
	
	is_end_of_article = False
	
	article_text = "" + article_header + "\n"
	
	while not is_end_of_article:
		time.sleep(randint(sleep_min, sleep_max))
		article = driver.find_element_by_id("newsArticle")
		page_text = article.find_element_by_id("kiji").text
		article_text += page_text + "\n"
	
		# Keep going to the next page until there is no next page
		try:
			driver.get(article.find_element_by_class_name(
				"topPageNav").find_element_by_class_name(
				"nextPage").get_attribute("href"))
		except:
			is_end_of_article = True
	
			# some articles don't have a by-line
			try:
				article_text += article.find_element_by_class_name(
					"author").text + "\n"
			except:
				raise
			output_file.write(article_text + "\n")

output_file.close()
driver.quit()