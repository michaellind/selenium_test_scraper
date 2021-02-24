from selenium import webdriver
import time
from random import randint

PATH = r"C:\Users\Michael\Desktop\chromedriver.exe"

driver = webdriver.Chrome(PATH)

sleep_min = 2
sleep_max = 10

driver.get("https://natgeo.nikkeibp.co.jp/atcl/news/16/a/092600060/")

article_header = driver.find_element_by_class_name("articleTitleBox").text

is_end_of_article = False

article_text = "" + article_header + "\n"

while not is_end_of_article:
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
		print(article_text)

driver.quit()