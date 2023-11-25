import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json


# https://news.ycombinator.com/
def get_link_score_list(page_num):
    '''
    Get title and score link list.
    param:
    page_num: the maxim page_num I want to get.
    '''
    article_link_list = []
    article_subtext_list = []
    for page in range(1, page_num + 1):
        response = requests.get(f"https://news.ycombinator.com/?p={page}")
        soup = BeautifulSoup(response.text, 'html.parser')
        # css selector . for class # for id
        article_link = soup.select('.titleline')
        # get the subtext so that they can match the title.
        article_subtext = soup.select('.subtext')
        article_link_list.extend(article_link)
        article_subtext_list.extend(article_subtext)
    return article_link_list, article_subtext_list


def create_custom_hackernews(links, subtexts, upline):
    '''
    Get custom hackernews list.
    param:
    links: a list of news link.
    subtexts: a list to get score.
    upline: the point you want to set to get more than it.
    '''
    hacker_news = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        # must find the a ancher
        link = links[idx].find("a").get("href", None)
        score = subtexts[idx].select('.score')
        if len(score):
            # because score is a list so I need to get the element!
            point = int(score[0].getText().split()[0])
            if point > upline:
                hacker_news.append(
                    {'title': title, 'link': link, 'score': point})
    return sorted(hacker_news, reverse=True, key=lambda x: x['score'])


article_link_list, article_subtext_list = get_link_score_list(page_num=2)
res = create_custom_hackernews(article_link_list, article_subtext_list, 600)
pprint(res)

for news in res:
    data = f'''
        **Title:** {news['title']}
        **Score:** {news['score']}
        **Link:** [LINK]({news['link']})
        '''

    resp = requests.post("https://ntfy.sh/snews",
                         data=data)
    print(resp.status_code)
