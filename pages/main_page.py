from .base_page import BasePage
from .locators import MainPageLocators
from .editor_page import EditorTemplatePage


class MainPage(BasePage):
    def goo_to_page_button_editor(self):
        assert self.is_element_present(*MainPageLocators.BUTTON_MASSAGE_EDITOR), 'Not button Message Editor'

    def goo_to_page_editor(self):
        self.browser.find_element(*MainPageLocators.BUTTON_MASSAGE_EDITOR).click()

    def go_to_preview_page(self):
        self.browser.find_element(*MainPageLocators.BUTTON_PREVIEW).click()

