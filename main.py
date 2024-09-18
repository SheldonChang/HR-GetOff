from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from credentials import get_credentials
from countdown import show_window, show_message
from web_automation import login, navigate_to_attendance_report
from web_automation import search_attendance, find_date_text


def main():
    username, password = get_credentials()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

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
