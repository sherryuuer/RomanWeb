# pass the goods url : sony earphone
goods_url = "https://www.amazon.co.jp/%E3%82%BD%E3%83%8B%E3%83%BC-%E3%83%AF%E3%82%A4%E3%83%A4%E3%83%AC%E3%82%B9%E3%83%8E%E3%82%A4%E3%82%BA%E3%82%AD%E3%83%A3%E3%83%B3%E3%82%BB%E3%83%AA%E3%83%B3%E3%82%B0%E3%83%98%E3%83%83%E3%83%89%E3%83%9B%E3%83%B3-%E3%83%8E%E3%82%A4%E3%82%BA%E3%82%AD%E3%83%A3%E3%83%B3%E3%82%BB%E3%83%AA%E3%83%B3%E3%82%B0%E6%90%AD%E8%BC%89-Bluetooth%E5%AF%BE%E5%BF%9C-WH-CH720N/dp/B0BVPVBG3W?ref_=ast_sto_dp&th=1"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7"


def get_price(goods_url):
    from bs4 import BeautifulSoup
    import requests
    import lxml

    headers = {
        "User-Agent": USER_AGENT,
        "Accept-Language": ACCEPT_LANGUAGE
    }
    response = requests.get(url=goods_url, headers=headers)
    amazon_webpages = response.content
    # print(amazon_webpages)
    soup = BeautifulSoup(amazon_webpages, "lxml")
    # print(soup.prettify())
    price = soup.find(name="span", class_="a-offscreen").get_text()
    # eg.<span class="a-offscreen">￥18,466</span>
    price = price.split("￥")[1]
    return price


# price = get_price(goods_url)
price = "18,466"

price = float(price.replace(",", ""))
print(price)

buy_price = 12000
if price <= buy_price:
    pass  # send a message to me.
