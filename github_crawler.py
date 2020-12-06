import json
import random
import urllib.request
from urllib.parse import quote
from itertools import islice

from bs4 import BeautifulSoup

# todo put variables to config
# todo clean everything
# keywords = ["openstack", "nova", "css"]
# proxies = ["8.129.215.20:8080", "208.80.28.208:8080"]
# search_type = "Repositories"  # "Issues", "Wikis"


def set_proxy(proxies):
    proxy_support = urllib.request.ProxyHandler({'http': f'http://{random.choice(proxies)}'})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)


def create_url(keywords, search_type):
    URL_BASE = "https://github.com/search?q="
    converted_keywords = map(quote, keywords)  # support unicode
    return URL_BASE + "+".join(converted_keywords) + f"&type={search_type.lower()}"


def get_links(parsed_html, tag, attrs):
    items = parsed_html.body.find(tag, attrs=attrs)
    links = []
    for item in items.find_all("div", {"class": "f4 text-normal"}):
        links.append("https://github.com" + item.find("a")["href"])
    return links


def main(in_filename="in.txt", out_filename="out.txt"):
    with open(in_filename) as json_file:
        data = json.load(json_file)
        keywords = data["keywords"]
        proxies = data["proxies"]
        search_type = data["type"]
    set_proxy(proxies)
    search_url = create_url(keywords, search_type)
    with urllib.request.urlopen(search_url) as response:
        html = response.read()
    parsed_html: BeautifulSoup = BeautifulSoup(html, "html5lib")
    links = []
    if search_type == "Repositories":
        links = get_links(parsed_html, "ul", {'class': "repo-list"})
    elif search_type == "Issues":
        links = get_links(parsed_html, "div", {'class': "issue-list"})
    elif search_type == "Wikis":
        links = get_links(parsed_html, "div", {'id': "wiki_search_results"})
    else:
        print(f"Type {search_type} not supported.")
    res_json = []
    for link in links:
        res_json.append({"url": link})
    with open(out_filename, 'w') as outfile:
        json.dump(res_json, outfile)


if __name__ == "__main__":
    main()
