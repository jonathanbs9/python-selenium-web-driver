"""
This tests cover duckduckgo searches.
"""
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
import pytest

@pytest.mark.parametrize('phrase', ['panda', 'golang', 'python', 'river plate'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    #phrase = "panda"

    # Given the DuckduckGo Home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(phrase)

    # And the search resulta query is "panda"
    #import ipdb; ipdb.set_trace()
    assert phrase == result_page.search_input_value()
    

    # And the search result pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # Then the search result contains "panda"
    #time.sleep(3) -> Nunca hacer un hard sleep! 
    assert phrase in result_page.title()
    