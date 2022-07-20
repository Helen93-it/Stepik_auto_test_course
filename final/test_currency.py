import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('language', ['id', 'ru', 'es'])
def test_with_different_links(browser, language):
    link = f"https://currency.com/{language}"
    browser.implicitly_wait(10)
    browser.get(link)

    product = browser.find_element(By.CSS_SELECTOR, "header .navItemWrap:nth-child(1)>a")
    print(product.text)
    q = browser.find_element(By.CSS_SELECTOR, ".wrap .cx-head h2")
    q_text = q.text
    if language == 'id':
        assert q_text == "Mengapa Currency.com?"
    elif language == 'ru':
        assert q_text == "Почему Currency.com — прекрасный выбор?"
    elif language == 'es':
        assert q_text == "¿Por qué Currency.com?"
