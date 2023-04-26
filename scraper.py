import requests
import json
from bs4 import BeautifulSoup


def extract_tag(ancestor, selector=None, attribute=None, return_list=False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)]
        if not selector and attribute:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except (AttributeError,TypeError):
        return None

selectors = {
        "opinion_id": [None, "data-entry-id"],
        "author": ["span.user-post__author-name"],
        "recommendation": ["span.user-post__author-recomendation > em"],
        "rating": ["span.user-post__score-count"],
        "verified": ["div.review-pz"],
        "post_date": ["span.user-post__published > time:nth-child(1)","datetime"],
        "purchase_date": ["span.user-post__published > time:nth-child(2)","datetime"],
        "vote_up": ["button.vote-yes","data-total-vote"],
        "vote_down": ["button.vote-no","data-total-vote"],
        "content": ["div.user-post__text"],
        "cons": ["div.review-feature__title--negatives ~ div.review-feature__item", None, True],
        "pros": ["div.review-feature__title--positives ~ div.review-feature__item", None, True],
}

# product_code = input("Podaj kod produktu\n")
product_code = "96693065"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
all_opinions = []
while(url):
    print(url)
    response = requests.get(url)
    page_dom = BeautifulSoup(response.text, "html.parser")
    opinions = page_dom.select("div.js_product-review")
    for opinion in opinions:
        single_opinion = {}
        for key, value in selectors.items():
            single_opinion[key] = extract_tag(opinion, *value)
        all_opinions.append(single_opinion)
    try:
        url = f"https://www.ceneo.pl" + extract_tag(page_dom, ".pagination__next", "href")
    except TypeError:
        url = None
with open(f"./opinions//{product_code}.json", "w", encoding="UTF-8") as file:
    json.dump(all_opinions, file, indent=4, ensure_ascii=False)