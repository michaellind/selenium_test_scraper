import bs4
import requests
import time
from random import randint

# trying out bs4

sleep_min = 1
sleep_max = 3

f = open("joongangcolumnsjapanese.txt") # URLS from japanese.joins.com here
urls = [url.strip() for url in f.readlines()]
f.close()

output_file = open("joongang_columns.txt", "w", encoding="utf-8")

i = 0

for url in urls:
	#time.sleep(randint(sleep_min, sleep_max))
	res = requests.get(url)

	res.raise_for_status()
	
	soup = bs4.BeautifulSoup(res.text, 'html.parser')

	title = soup.find_all(class_="headline mg")[0].text.strip()
	pub_date = soup.find_all(class_="article_source")[0].text.strip()
	article_text = soup.find_all(id="article_body")[0].text.strip()
	output_text = title + "\n" + pub_date + "\n" + article_text + "\n"

	# problem to solve later: line breaks

	i += 1

	print(i)
	
	print(output_text)

	output_file.write(output_text)

output_file.close()
