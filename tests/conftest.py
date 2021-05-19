"""
This module contains shared fixtures
"""
import pytest
import selenium.webdriver
import json

@pytest.fixture
def config(scope='session'):
    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)
    
    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config

@pytest.fixture
def browser(config):
    # Initiate WebDriver instance
    if config['browser'] == 'Firefox':
      browser = selenium.webdriver.Firefox()
    elif config['browser'] == 'chrome':
      browser = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
      opts = selenium.webdriver.ChromeOptions()
      opts.add_argument('headless')
      browser = selenium.webdriver.Chrome(options=opts)
    else:
      raise Exception(f'Browser "{config["browser"]}" is NOT supported')

    
    #Make its calls wait up to 10 secs for elem to appear
    browser.implicitly_wait(config['implicit_wait'])

    #Return the Bwedriver instance for the setup
    yield browser

    # Quit the WebDriver instane for cleanup
    browser.quit()