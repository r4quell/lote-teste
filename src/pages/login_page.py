from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def fazer_login(self, usuario, senha):
        username_field = self.wait.until(EC.visibility_of_element_located(self.username_input))
        username_field.clear()
        username_field.send_keys(usuario)

        password_field = self.driver.find_element(*self.password_input)
        password_field.clear()
        password_field.send_keys(senha)

        self.driver.find_element(*self.login_button).click()
        self.wait.until(EC.url_contains("/inventory.html"))
