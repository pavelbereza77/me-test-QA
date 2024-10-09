import time
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators import BlockIfThenElseLocator, MainPageLocators


class IfThenElseBlock(BasePage):
    def should_if_then_else_block(self):
        self.presence_element_block()
        self.delite_block()

    def presence_element_block(self):
        assert self.is_element_present(*BlockIfThenElseLocator.IF_TEXT), 'Not text form IF'
        assert self.is_element_present(*BlockIfThenElseLocator.THEN_TEXT), 'Not text form THEN'
        assert self.is_element_present(*BlockIfThenElseLocator.ELSE_TEXT), 'Not text form ELSE'

    def click_button_delite(self):
        self.browser.find_element(*BlockIfThenElseLocator.DELITE_BLOCK).click()

    def delite_block(self):
        assert self.is_element_present(*MainPageLocators.BLOK_IF_THEN_ELSE), 'Not blok IF_THEN_ELSE'
        # time.sleep(2)
        self.click_button_delite()
        assert not self.is_element_present(*MainPageLocators.BLOK_IF_THEN_ELSE), 'Blok IF_THEN_ELSE not is delite'

    def input_text_if(self, text='test'):
        self.browser.find_element(*BlockIfThenElseLocator.IF_TEXT).send_keys(text)

    def input_text_then(self, text='test'):
        self.browser.find_element(*BlockIfThenElseLocator.THEN_TEXT).send_keys(text)

    # def get_element_then(self):
    #     return self.browser.find_element(*BlockIfThenElseLocator.THEN_TEXT)

    def input_text_else(self, text='test'):
        self.browser.find_element(*BlockIfThenElseLocator.ELSE_TEXT).send_keys(text)

    def input_text_then_2(self, text='test'):
        self.browser.find_element(*BlockIfThenElseLocator.THEN_TEXT_2).send_keys(text)

    def input_text_else_2(self, text='test'):
        self.browser.find_element(*BlockIfThenElseLocator.ELSE_TEXT_2).send_keys(text)

    def input_text_optional(self, text='test'):
        self.browser.find_element(*BlockIfThenElseLocator.OPTIONAL).send_keys(text)

    def input_text_optional_2(self, text='test'):
        self.browser.find_element(*BlockIfThenElseLocator.OPTIONAL_2).send_keys(text)