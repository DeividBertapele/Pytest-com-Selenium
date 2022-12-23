from selenium.webdriver import Firefox
from pytest import fixture


@fixture(scope='session')
def browser():
    # return Firefox()
    browser = Firefox()
    yield browser
    browser.quit()