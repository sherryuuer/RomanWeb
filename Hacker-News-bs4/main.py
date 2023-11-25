from bs4 import BeautifulSoup
import requests


# https://news.ycombinator.com/ get the highest score of news!
response = requests.get("https://news.ycombinator.com/")
yc_webpages = response.text
soup = BeautifulSoup(yc_webpages, "html.parser")
article = soup.find_all(name="span", class_="titleline")
article_name = []
article_link = []
article_score = [int(x.getText().split()[0])
                 for x in soup.find_all(name="span", class_="score")]

for element in article:
    name = element.getText()
    article_name.append(name)
    link = element.find("a").get("href")
    article_link.append(link)
# print(article_name)
# print(article_link)
# print(article_score)
max_score = max(article_score)
max_index = article_score.index(max_score)
top_news = article_name[max_index]
top_link = article_link[max_index]
print(top_news)
print(top_link)


# with open("bs4/website.html", encoding="utf-8") as f:
#     contents = f.read()
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.text)
# # print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     # text = tag.getText()
#     text = tag.get("href")
#     print(text)

# heading = soup.find(name="h1", id="name")
# find will find the first one.
# print(heading)

# select_heading = soup.find(name="h3", class_="heading")
# class must wrote to be class_
# print(select_heading)
# a = select_heading.name # attribute is tag
# a = select_heading.getText() # tag's method
# a = select_heading.get("class") # some dict?
# print(a)

# css selector
# company_url = soup.select_one(selector="p a")
# name = soup.select(selector="#name")
# class_in_it = soup.select(selector=".heading")
