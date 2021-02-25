from selenium import webdriver
import time
from random import randint

# Anyone who uses this other than me must change the PATH variable to point to chromedriver.exe
PATH = r"C:\Users\Michael\Desktop\chromedriver.exe"

driver = webdriver.Chrome(PATH)

sleep_min = 5
sleep_max = 15

# put a list of links here from natureasia.com/ja-jp/research
f = open("nature_research_highlights_links.txt")
urls = [url.strip() for url in f.readlines()]
f.close()

en_output = open("researchhighlights_en.txt", "w", encoding="utf-8") # English only
ja_output = open("researchhighlights_ja.txt", "w", encoding="utf-8") # Japanese only
ja_en_output = open("researchhighlights_ja_en.txt", "w", encoding="utf-8") # alternating English and Japanese

for url in urls:

	driver.get(url)
	time.sleep(randint(sleep_min, sleep_max))
	
	article = driver.find_element_by_id("content").find_element_by_class_name("main-container")
	
	j_article_text = ""
	
	j_title = article.find_element_by_class_name("title").text
	j_journal = article.find_element_by_class_name("journal").text
	j_pub_date = article.find_element_by_class_name("pubdate").text
	
	j_article_text += j_title + "\n" + j_journal + "\n" + j_pub_date + "\n"
	
	p_elements = article.find_elements_by_tag_name("p")
	for p_element in p_elements:
		class_val = p_element.get_attribute("class")
		if (class_val == ""):
			j_article_text += p_element.text + "\n"
	
	url = url.replace("ja-jp", "en")

	driver.get(url)
	time.sleep(randint(sleep_min, sleep_max))
	
	article = driver.find_element_by_id("content").find_element_by_class_name("main-container")
	
	e_article_text = ""
	
	e_title = article.find_element_by_class_name("title").text
	e_journal = article.find_element_by_class_name("journal").text
	e_pub_date = article.find_element_by_class_name("pub-date").text
	
	e_article_text += e_title + "\n" + e_journal + "\n" + e_pub_date + "\n"
	
	p_elements = article.find_elements_by_tag_name("p")
	for p_element in p_elements:
		class_val = p_element.get_attribute("class")
		if (class_val == ""):
			e_article_text += p_element.text + "\n"
	
	en_output.write(e_article_text + "\n")
	ja_output.write(j_article_text + "\n")
	ja_en_output.write(e_article_text + "\n" + j_article_text + "\n")

	# idea I wanted to try out: also make files for each individual press release
	file_name = "(Nature) " + e_title
	file_name = file_name.replace(":", " -")
	file_name = file_name.replace("%", " percent")
	file_name = file_name.replace("°C", " degrees Celsius")
	file_name = file_name.replace("?", "")
	file_name = file_name.replace("‘", "'")
	file_name = file_name.replace("’", "'")

	e_file_name = file_name + " (English).txt"
	j_file_name = file_name + " (Japanese).txt"

	en_single_file = open(e_file_name, "w", encoding="utf-8")
	ja_single_file = open(j_file_name, "w", encoding="utf-8")

	en_single_file.write(e_article_text + "\n")
	ja_single_file.write(j_article_text + "\n")

	en_single_file.close()
	ja_single_file.close()

en_output.close()
ja_output.close()
ja_en_output.close()

driver.quit()