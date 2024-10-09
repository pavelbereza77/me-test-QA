import time

from pages.block_if_then_else import IfThenElseBlock

from pages.main_page import MainPage
from pages.preview_page import PreviewPage


def test_present_blok_if_then_else(browser):
    link = "http://localhost:3000/"
    browser.get(link)
    page = MainPage(browser=browser, url=link)
    page.open()
    page.goo_to_page_editor()
    page.clik_button_if_then_else()
    if_then_else_blok = IfThenElseBlock(browser=browser, url=browser.current_url)
    browser.implicitly_wait(5)
    if_then_else_blok.should_if_then_else_block()

    page.set_input_text_editor(text='Hello! ')
    page.click_firstname()
    page.set_input_text_editor(text='\n\nI just went through your profile and would love to join your network!\n')

    page.clik_button_if_then_else()
    page.click_company()
    if_then_else_blok.input_text_then(text='I know you work at ')
    page.click_company()
#######################################################################
    # page.clik_button_if_then_else()
    # page.click_position()

    # if_then_else_blok.input_text_then_2(text='as ')
    # page.click_position()
    # if_then_else_blok.input_text_else_2(text=' , but what is your role?')
    # if_then_else_blok.input_text_optional_2(text=' :)')
############################################################################################
    if_then_else_blok.input_text_else(text='\nWhere do you work the moment?')
    if_then_else_blok.input_text_optional(text='Jake\nSoftware Developer\njakelennard@gmail.com')
    time.sleep(3)

    page.go_to_preview_page()
    preview_page = PreviewPage(browser=browser, url=browser.current_url)
    preview_page.set_firstname_variable(text='Bill')
    preview_page.set_company_variable(text='Bill & Melinda Gates Foundation')
##############################################################################################
    # preview_page.set_lastname_variable(text='Gates')
    # preview_page.set_position_variable(text='Co-Chair')

    time.sleep(20)

