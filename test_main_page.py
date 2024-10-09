import time

from pages.main_page import MainPage
from pages.editor_page import EditorTemplatePage


def test_goo_to_page_button_editor(browser):
    link = "http://localhost:3000/"
    browser.get(link)
    page = MainPage(browser, link)
    page.open()
    page.goo_to_page_button_editor()
    time.sleep(5)


def test_presence_buttons_main_page(browser):
    link = "http://localhost:3000/"
    browser.get(link)
    page = MainPage(browser, link)
    page.open()
    page.goo_to_page_editor()
    page_editor = EditorTemplatePage(browser=browser, url=browser.current_url)
    page_editor.should_be_editor_page()
    time.sleep(5)


def test_save_text_editor_in_main_windows(browser):
    link = "http://localhost:3000/"
    browser.get(link)
    page = MainPage(browser, link)
    page.open()
    page.goo_to_page_editor()
    page.set_input_text_editor()
    text_editor_before_saving = page.get_text_in_editor()
    print(text_editor_before_saving)
    page.saving_text_editor()
    page.close_editor()
    page.goo_to_page_editor()
    text_editor_after_saving = page.get_text_in_editor()
    print(text_editor_after_saving)
    assert text_editor_before_saving == text_editor_after_saving, ('The text does not match after saving and '
                                                                   'entering the editor again')
    page.clik_button_if_then_else()
    text_editor_after_clik_if_then_else = page.get_text_in_editor()

    assert text_editor_before_saving == text_editor_after_clik_if_then_else, ('The text in the main editor field does '
                                                                              'not match after saving and then logging '
                                                                              'into the editor and activating '
                                                                              'the if_then_else block')



