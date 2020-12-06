import json
import pytest
from github_crawler import main, create_url


@pytest.mark.parametrize("test_name", ["1", "2", "unicode", "issues", "wikis"])
def test_main(test_name):
    main(f"res/in_test_{test_name}.txt", "res/out_test.txt")
    with open("res/out_test.txt") as f:
        actual_urls = set(x["url"] for x in json.load(f))
    with open(f"res/out_test_{test_name}.txt") as f:
        expected_urls = set(x["url"] for x in json.load(f))
    assert actual_urls == expected_urls
    open('res/out_test.txt', 'w').close()


def test_create_url():
    actual = create_url(["привет"], "issues")
    expected = 'https://github.com/search?q=%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82&type=issues'
    assert actual == expected
