from bs4 import BeautifulSoup
import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_webpages = response.text
soup = BeautifulSoup(empire_webpages, "html.parser")
titles = soup.find_all(name="h3", class_="title")
titles = [x.getText() for x in titles][::-1]
for movie in titles:
    with open("scrape_movies/movies.txt", "a", encoding="utf-8") as f:
        movie = f"{movie}\n"
        f.write(movie)
# some isssue with the 58 so added the encoding in the with line.
#  '56) Reservoir Dogs', '57) Whiplash', '58) Inglourious Basterds', '59) E.T. â\x80\x93 The Extra Terrestrial', '60) American Beauty', '61)
# UnicodeEncodeError: 'cp932' codec can't encode character '\xe2' in position 9: illegal multibyte sequence
