from pages.base_page import BasePage
from pages.locators import PreviewPageLocator, MainPageLocators


class PreviewPage(BasePage):
    def should_preview_page(self):
        self.presence_element_preview_page()
        self.equality_text_page_edite_and_preview_page()

    def presence_element_preview_page(self):
        assert self.is_element_present(*PreviewPageLocator.FORM_MESSAGE_PREVIEW), 'Not form Message Preview'
        assert self.is_element_present(*PreviewPageLocator.BUTTON_CLOS_MESSAGE_PREVIEW), 'Not form Message Preview'

    def equality_text_page_edite_and_preview_page(self):
        self.browser.find_element(*PreviewPageLocator.BUTTON_CLOS_MESSAGE_PREVIEW).click()
        self.browser.find_element(*MainPageLocators.TEMPLATE_TEXT).send_keys('Hello!')
        firstname_variables = self.browser.find_element(*MainPageLocators.BUTTON_FIRSTNAME)
        firstname_variables.click()
        lastname_variables = self.browser.find_element(*MainPageLocators.BUTTON_LASTNAME)
        lastname_variables.click()
        company_variables = self.browser.find_element(*MainPageLocators.BUTTON_COMPANY)
        company_variables.click()
        position_variables = self.browser.find_element(*MainPageLocators.BUTTON_POSITION)
        position_variables.click()

        self.browser.find_element(*MainPageLocators.BUTTON_IF_THEN_ELSE).click()
        text_editor_main = self.browser.find_element(*MainPageLocators.TEMPLATE_TEXT).text

        # assert text_editor_main == '', 'There is text in the main editor window'

        # text_editor_option = self.browser.find_element(*MainPageLocators.TEXT_EDITOR).text
        self.browser.find_element(*MainPageLocators.BUTTON_PREVIEW).click()
        text_preview = self.browser.find_element(*PreviewPageLocator.TEXT_MESSAGE_PREVIEW).text

        assert text_editor_main == text_preview, 'The text in the editor does not match the text in the preview'

        assert self.is_element_present(*PreviewPageLocator.FIRSTNAME_PREVIEW), 'Not variable firstname'
        firstname_preview = self.browser.find_element(*PreviewPageLocator.FIRSTNAME_PREVIEW)
        value_firstname_preview = firstname_preview.get_attribute('value')

        assert self.is_element_present(*PreviewPageLocator.LASTNAME_PREVIEW), 'Not variable lastname'
        lastname_preview = self.browser.find_element(*PreviewPageLocator.LASTNAME_PREVIEW)
        value_lastname_preview = lastname_preview.get_attribute('value')

        assert self.is_element_present(*PreviewPageLocator.COMPANY_PREVIEW), 'Not variable company'
        company_preview = self.browser.find_element(*PreviewPageLocator.COMPANY_PREVIEW)
        value_company_preview = company_preview.get_attribute('value')

        assert self.is_element_present(*PreviewPageLocator.POSITION_PREVIEW), 'Not variable position'
        position_preview = self.browser.find_element(*PreviewPageLocator.POSITION_PREVIEW)
        value_position_preview = position_preview.get_attribute('value')

        print(firstname_variables.text)
        print(value_firstname_preview)

        assert '{' + f'{firstname_variables.text}' + '}' == value_firstname_preview, 'The editor variable firstname is not equal to preview'
        assert '{' + f'{lastname_variables.text}' + '}' == value_lastname_preview, 'The editor variable lastname is not equal to preview'
        assert '{' + f'{company_variables.text}' + '}' == value_company_preview, 'The editor variable company is not equal to preview'
        assert '{' + f'{position_variables.text}' + '}' == value_position_preview, 'The editor variable position is not equal to preview'
