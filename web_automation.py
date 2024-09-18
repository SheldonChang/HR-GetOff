from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date
import time


def login(driver, username, password):
    driver.get("https://jet-hr.jet-opto.com.tw/")
    # login ----------------------------------------------------------------
    username_field = driver.find_element(By.NAME, 'uid')
    password_field = driver.find_element(By.NAME, 'pwd')

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = driver.find_element(By.ID, 'button')
    login_button.click()


def navigate_to_attendance_report(driver):
    # 出發前往出勤表 ----------------------------------------------------------------
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dropDown")))
    actions = ActionChains(driver)
    attendance_menu = driver.find_element(By.XPATH, "//span[contains(text(), '考勤')]")
    actions.move_to_element(attendance_menu).perform()
    attendance_report_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'B4.出勤報表')]"))
    )
    actions.move_to_element(attendance_report_menu).perform()
    specific_report = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'B4.1.考勤彙總表')]"))
    )
    specific_report.click()


def search_attendance(driver):
    # 按下查詢喔 ----------------------------------------------------------------
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "button2")))
    search_btn = driver.find_element(By.ID, 'button2')
    search_btn.click()


def find_date_text(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "table1-table-content")))
    today = date.today().strftime("%Y/%m/%d")
    time.sleep(1)

    scroll_pause_time = 0.2
    max_scrolls = 10

    for i in range(max_scrolls):
        table_content = driver.find_element(By.ID, "table1-table-content")
        rows = table_content.find_elements(By.CSS_SELECTOR, ".cmc-table-row")
        max_rows = 7

        for row in rows:
            cells = row.find_elements(By.CLASS_NAME, "cmc-table-cell")
            tmp_arr = [cells[i].find_element(By.CLASS_NAME, "cmc-table-cell-text")
                       .text.strip() for i in range(max_rows)]

            if any(today in cell_text for cell_text in tmp_arr):
                print(tmp_arr)
                return tmp_arr

        print("SCROOL: " + str(i))
        driver.execute_script("arguments[0].scrollTop += 150;",
                              driver.find_element(By.ID, "table1-table-vscroll"))
        time.sleep(scroll_pause_time)

    return None
