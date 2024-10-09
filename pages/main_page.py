from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def goo_to_page_button_editor(self):
        assert self.is_element_present(*MainPageLocators.BUTTON_MASSAGE_EDITOR), 'Not button Message Editor'

    def goo_to_page_editor(self):
        self.browser.find_element(*MainPageLocators.BUTTON_MASSAGE_EDITOR).click()

    def go_to_preview_page(self):
        self.browser.find_element(*MainPageLocators.BUTTON_PREVIEW).click()

    def set_input_text_editor(self, text='hello abracadabra'):
        self.browser.find_element(*MainPageLocators.TEMPLATE_TEXT).send_keys(text)

    def get_text_in_editor(self):
        return self.browser.find_element(*MainPageLocators.TEMPLATE_TEXT).text

    def saving_text_editor(self):
        self.browser.find_element(*MainPageLocators.BUTTON_SAVE).click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def close_editor(self):
        self.browser.find_element(*MainPageLocators.BUTTON_CLOSE).click()

    def clik_button_if_then_else(self):
        self.browser.find_element(*MainPageLocators.BUTTON_IF_THEN_ELSE).click()

    def clare_text_editor(self):
        return self.browser.find_element(*MainPageLocators.TEMPLATE_TEXT).clear()

    def click_firstname(self):
        self.browser.find_element(*MainPageLocators.BUTTON_FIRSTNAME).click()

    def click_lastname(self):
        self.browser.find_element(*MainPageLocators.BUTTON_LASTNAME).click()

    def click_company(self):
        self.browser.find_element(*MainPageLocators.BUTTON_COMPANY).click()

    def click_position(self):
        self.browser.find_element(*MainPageLocators.BUTTON_POSITION).click()
