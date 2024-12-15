import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TestTest1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def read_credentials(self, file_path):
        """Đọc danh sách tài khoản và mật khẩu từ file"""
        try:
            with open(file_path, "r") as file:
                credentials = [line.strip().split(",") for line in file.readlines()]
                return credentials
        except Exception as e:
            print(f"Error reading credentials: {e}")
            return []

    def test_login_multiple_accounts(self):
        try:
            credentials_list = self.read_credentials("credentials.txt")
            if not credentials_list:
                print("No credentials found. Please check the file.")
                return

            for idx, (username, password) in enumerate(credentials_list):
                print(f"Testing account {idx + 1}: {username}")

                self.driver.get("https://github.com/login")
                self.driver.set_window_size(1296, 688)

                self.driver.find_element(By.ID, "login_field").click()
                self.driver.find_element(By.ID, "login_field").clear()
                self.driver.find_element(By.ID, "login_field").send_keys(username)

                self.driver.find_element(By.ID, "password").click()
                self.driver.find_element(By.ID, "password").clear()
                self.driver.find_element(By.ID, "password").send_keys(password)

                self.driver.find_element(By.NAME, "commit").click()
                time.sleep(3)  

                try:
                    avatar_element = self.driver.find_element(By.CSS_SELECTOR, ".avatar")
                    if avatar_element:
                        print(f"Account {username}: Login Success")
                except NoSuchElementException:
                    print(f"Account {username}: Login Fail")
        except Exception as e:
            print(f"An error occurred during the test: {e}")


if __name__ == "__main__":
    t1 = TestTest1()
    t1.setup_method(None)
    t1.test_login_multiple_accounts()
    t1.teardown_method(None)
