# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest2():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_test2(self):
        # Đọc danh sách tài khoản và mật khẩu từ file
        with open('github.txt', 'r') as file:
            github_list = file.readlines()

        # Lặp qua từng cặp tài khoản và mật khẩu
        for line in github_list:
            username, password = line.strip().split(',')

            self.driver.get("https://github.com/login")
            self.driver.set_window_size(1296, 688)
            self.driver.find_element(By.ID, "login_field").click()
            self.driver.find_element(By.ID, "login_field").send_keys(username)
            self.driver.find_element(By.ID, "password").click()
            self.driver.find_element(By.ID, "password").send_keys(password)
            self.driver.find_element(By.NAME, "commit").click()

            try:
                # Tìm phần tử chứa thông báo lỗi
                alert_text = self.driver.find_element(By.CSS_SELECTOR, ".js-flash-alert").text
                if "Incorrect username or password." in alert_text:
                    print(f"Test case for username: {username} and password: {password} -> successful test case")
                else:
                    print(f"Test case for username: {username} and password: {password} -> failed test case")
            except Exception as e:
                # Nếu không tìm thấy thông báo lỗi
                print(f"Test case for username: {username} and password: {password} -> failed test case")

# Chạy thử test case
t1 = TestTest2()
t1.setup_method(None)
t1.test_test2()
t1.teardown_method(None)
