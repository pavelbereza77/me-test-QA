from pages.main_page import MainPage
from pages.preview_page import PreviewPage


def test_preview_page(browser):
    link = "http://localhost:3000/"
    browser.get(link)
    page = MainPage(browser=browser, url=link)
    page.open()
    page.goo_to_page_editor()
    page.go_to_preview_page()
    preview_page = PreviewPage(browser=browser, url=browser.current_url)
    preview_page.should_preview_page()


