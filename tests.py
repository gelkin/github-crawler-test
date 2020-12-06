import json

import pytest

from github_crawler import main


@pytest.mark.parametrize("test_name", ["1", "2", "unicode", "issues", "wikis"])
def test_main(test_name):
    # keywords = ["openstack", "nova", "css"]
    # proxies = ["8.129.215.20:8080", "208.80.28.208:8080"]
    # search_type = "Repositories"  # "Issues", "Wikis"
    # data = {"keywords": keywords, "proxies": proxies, "type": search_type}
    # with open('res/in_test_1.txt', 'w') as outfile:
    #     json.dump(data, outfile)
    main(f"res/in_test_{test_name}.txt", "res/out_test.txt")
    with open("res/out_test.txt") as f:
        actual_urls = set(x["url"] for x in json.load(f))
    with open(f"res/out_test_{test_name}.txt") as f:
        expected_urls = set(x["url"] for x in json.load(f))
    assert actual_urls == expected_urls
    open('res/out_test.txt', 'w').close()
