from selenium.webdriver.common.by import By


class MainPageLocators():
    BUTTON_MASSAGE_EDITOR = (By.CSS_SELECTOR, "div[id='root'] button")

    BUTTON_FIRSTNAME = (By.XPATH, "//button[text() ='{firstname}']")
    BUTTON_LASTNAME = (By.XPATH, "//button[text() ='{lastname}']")
    BUTTON_COMPANY = (By.XPATH, "//button[text() ='{company}']")
    BUTTON_POSITION = (By.XPATH, "//button[text() ='{position}']")

    BUTTON_IF_THEN_ELSE = (By.XPATH, "//button[text() ='[IF-THEN-ELSE]']")

    BUTTON_PREVIEW = (By.XPATH, "//button[text()='Preview']")
    BUTTON_SAVE = (By.XPATH, "//button[text()='Save']")
    BUTTON_CLOSE = (By.XPATH, "//button[text()='Close']")

    TEMPLATE_TEXT = (By.CSS_SELECTOR, "textarea[placeholder='main']")

    BLOK_IF_THEN_ELSE = (By.XPATH, "//div[@class='undefined']")

    TEXT_EDITOR = (By.CSS_SELECTOR, "textarea[placeholder = 'optional']")


class PreviewPageLocator():
    FORM_MESSAGE_PREVIEW = (By.XPATH, "//div[contains(@class,'MessagePreview_container')]")
    BUTTON_CLOS_MESSAGE_PREVIEW = (By.XPATH, "//button[contains(@class,'MessagePreview_closeButton')]")
    TEXT_MESSAGE_PREVIEW = (By.XPATH, "//div[contains(@class,'MessagePreview_preview')]/p")

    FIRSTNAME_PREVIEW = (By.CSS_SELECTOR, "input[placeholder='firstname']")
    LASTNAME_PREVIEW = (By.CSS_SELECTOR, "input[placeholder='lastname']")
    COMPANY_PREVIEW = (By.CSS_SELECTOR, "input[placeholder='company']")
    POSITION_PREVIEW = (By.CSS_SELECTOR, "input[placeholder='position']")


class BlockIfThenElseLocator():
    DELITE_BLOCK = (By.XPATH, "//button[contains(@class,'IfThenElseBlock_deleteButton')]")
    IF_TEXT = (By.CSS_SELECTOR, "textarea[placeholder='if']")
    IF_TEXT_2 = (By.CSS_SELECTOR, ".undefined .undefined textarea[placeholder='if']")
    THEN_TEXT = (By.CSS_SELECTOR, "textarea[placeholder='then']")
    THEN_TEXT_2 = (By.CSS_SELECTOR, ".undefined .undefined textarea[placeholder='then']")
    ELSE_TEXT = (By.CSS_SELECTOR, "textarea[placeholder='else']")
    ELSE_TEXT_2 = (By.CSS_SELECTOR, ".undefined .undefined textarea[placeholder='else']")
    OPTIONAL = (By.CSS_SELECTOR, "textarea[placeholder='optional']")
    OPTIONAL_2 = (By.CSS_SELECTOR, ".undefined .undefined textarea[placeholder='optional']")
#
# def get_then_selector(element):
#     attribute = element.get_attribute("data-id")
#     return attribute
#
#
# def get_then_element_2(data_id):
#     return f"//textarea[@ data-id={data_id} and placeholder = 'then']"
