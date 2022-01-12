from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '[value= "Add to basket"]')
    WRITE_A_REVIEW_LINK = (By.CSS_SELECTOR, "#write_review")
    ITEM_PRICE = (By.CSS_SELECTOR, ".price_color")
    STOCK_AVAILABILITY = (By.XPATH, "//div[@class='row']//p[2]")

    INNERALERT_ITEM_ADDDED = (By.XPATH, "//div[@id='messages']//div[1]//div[1]")
    NAME_OF_BOOK = (By.CSS_SELECTOR, "div.product_main h1")
    TOTAL_PRICE = (By.XPATH, "//div[@id='messages']//div[3]//div[1]//p[1]")
    VIEW_BASKET_LINK = (By.XPATH, "//a[contains(text(),'View basket')]")
    CHECKOUT_LINK = (By.XPATH, "//a[contains(text(),'Checkout now')]")
