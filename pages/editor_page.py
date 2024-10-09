from .base_page import BasePage
from .locators import MainPageLocators


class EditorTemplatePage(BasePage):
    def should_be_editor_page(self):
        self.presence_buttons_main_page()
        self.presence_variable_buttons()
        self.add_text_template()

    def presence_variable_buttons(self):
        assert self.is_element_present(*MainPageLocators.BUTTON_FIRSTNAME), 'Button {firstname} not presented'
        assert self.is_element_present(*MainPageLocators.BUTTON_LASTNAME), 'Button {lastname} not presented'
        assert self.is_element_present(*MainPageLocators.BUTTON_COMPANY), 'Button {company} not presented'
        assert self.is_element_present(*MainPageLocators.BUTTON_POSITION), 'Button {position} not presented'

    def presence_buttons_main_page(self):
        assert self.is_element_present(*MainPageLocators.BUTTON_PREVIEW), 'Button PREVIEW not presented'
        assert self.is_element_present(*MainPageLocators.BUTTON_SAVE), 'Button SAVE not presented'
        assert self.is_element_present(*MainPageLocators.BUTTON_CLOSE), 'Button CLOSE not presented'
        assert self.is_element_present(*MainPageLocators.BUTTON_IF_THEN_ELSE), 'Button IF_THEN_ELSE not presented'

    def add_text_template(self):
        assert self.is_element_present(*MainPageLocators.TEMPLATE_TEXT), 'The template text input block is missing'
        windows_text_template = self.browser.find_element(*MainPageLocators.TEMPLATE_TEXT)
        windows_text_template.send_keys('Hello!')
        assert 'Hello!' == windows_text_template.text, 'Not input text in window template'

        firstname = self.browser.find_element(*MainPageLocators.BUTTON_FIRSTNAME)
        firstname.click()
        assert firstname.text in windows_text_template.text, f'Not {firstname.text} in edition'

        lastname = self.browser.find_element(*MainPageLocators.BUTTON_LASTNAME)
        lastname.click()
        assert lastname.text in windows_text_template.text, f'Not {lastname.text} in edition'

        company = self.browser.find_element(*MainPageLocators.BUTTON_COMPANY)
        company.click()
        assert company.text in windows_text_template.text, f'Not {company.text} in edition'

        position = self.browser.find_element(*MainPageLocators.BUTTON_POSITION)
        position.click()
        assert position.text in windows_text_template.text, f'Not {position.text} in edition'
