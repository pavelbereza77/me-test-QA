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
