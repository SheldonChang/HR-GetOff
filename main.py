#!/usr/bin/env python3
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from credentials import get_credentials
from countdown import show_window, show_message
from web_automation import login, navigate_to_attendance_report
from web_automation import search_attendance, find_date_text


def main():
    username, password = get_credentials()
    options = Options()
    options.add_argument("--headless")
    # options.add_argument("--window-size=1920,1080")
    if platform.system() == "Windows":
        options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)
    login(driver, username, password)
    navigate_to_attendance_report(driver)
    search_attendance(driver)

    found = find_date_text(driver)
    driver.quit()

    if not found or not found[6]:
        show_message()
    else:
        show_window(found)


if __name__ == "__main__":
    main()
