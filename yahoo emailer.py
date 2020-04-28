from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

host_email = "@yahoo.com"                       # add a yahoo email here
print("Host email:", host_email)
password = input("Email Password: ")
email_reciever = input("Reciever's Email: ")
email_subject = input("Email Subject: ")
email_body = input("Email body: ")
print("\nSending Email...")

browser = webdriver.Chrome(executable_path =r'')      # write path of chromedriver.exe inside executable_path
browser.get("https://login.yahoo.com/")
email_elem = browser.find_element_by_id("login-username")
email_elem.send_keys(host_email)
email_elem.submit()

time.sleep(3)
password_elem = browser.find_element_by_id("login-passwd")
password_elem.send_keys(password)
password_elem.send_keys(Keys.ENTER)
browser.get("https://mail.yahoo.com/")

time.sleep(3)
compose_elem = browser.find_element_by_link_text("Compose")
compose_elem.click()
time.sleep(3)
reciever_email_elem = browser.find_element_by_id("message-to-field")
reciever_email_elem.send_keys(email_reciever)
subject_elem = browser.find_element_by_css_selector(r'input[data-test-id="compose-subject"]')
subject_elem.send_keys(email_subject)
email_body_elem = browser.find_element_by_css_selector(r'div[role="textbox"]')
email_body_elem.send_keys(email_body)
send_email_elem = browser.find_element_by_css_selector(r'button[data-test-id="compose-send-button"]')
send_email_elem.click()

time.sleep(3)
browser.quit()
