import time

from pages.main_page import MainPage
from pages.editor_page import EditorTemplatePage

def test_goo_to_page_button_editor(browser):
    link = "http://localhost:3000/"
    browser.get(link)
    page = MainPage(browser, link)
    page.open()
    page.goo_to_page_button_editor()


def test_presence_buttons_main_page(browser):
    link = "http://localhost:3000/"
    browser.get(link)
    page = MainPage(browser, link)
    page.open()
    page.goo_to_page_editor()
    page_editor = EditorTemplatePage(browser=browser,url=browser.current_url)
    page_editor.should_be_editor_page()
    time.sleep(1)
