
# Oxford Club Regression Test Script - oxfordclub.com
# Tester - Vinodha Rajan


from threading import Thread
from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
desired_cap=[
    

    {
      'os_version': 'Monterey',
      'os': 'OS X',
      'browser': 'Safari',
      'browser_version': 'latest',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-2'
    }
]


#run_session function searches for 'BrowserStack' on manwardpress.com
def run_session(desired_cap):
    driver = webdriver.Remote(
    command_executor='https://laura62:RFwB4esATEbbUMaH6hKa@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities= desired_cap)
    
    driver.maximize_window()

    # The driver.get method will navigate to a page given by the url
    driver.get('https://oxfordclub.com')

    if(driver.title=="The Oxford Club – Home | The Oxford Club"):
        print("Success: The page is launched successfully")
    else:
        print("Failed: The page tiltle is incorrect")

    time.sleep(5)

    driver.get('https://oxfordclub.com/member-login/')

    time.sleep(5)

    try:
      popup = driver.find_element(By.CLASS_NAME,"pf-widget-close")
      popup.click()
    except NoSuchElementException:
      pass


    #Find the username using xpath
    username = driver.find_element(By.CSS_SELECTOR, '#tfs-mw-user-login')
    username.send_keys("shoguybrk@yahoo.com")

    # #Find the password element using xpath
    password = driver.find_element(By.XPATH, "//input[@id='tfs-mw-user-pass']")
    password.send_keys('21201')
    time.sleep(2)

    

    login = driver.find_element(By.NAME,"wp-submit")
    login.click()

    time.sleep(5)


    try:
      popup = driver.find_element(By.CLASS_NAME,"pf-widget-close")
      popup.click()
    except NoSuchElementException:
      pass

    time.sleep(5)

    # Membership
    
    oc_membership = driver.find_element(By.XPATH,"//a[contains(text(),'My Membership')]")
    oc_membership.click()
    time.sleep(5)

    # My profile

    my_profile= driver.find_element(By.XPATH,"//a[contains(text(),'My Profile')]")
    my_profile.click()
    time.sleep(5)

    # My report

    my_report= driver.find_element(By.XPATH,"//a[contains(text(),'My Reports')]")
    my_report.click()
    time.sleep(5)

    # My Protofolio

    my_portfolios = driver.find_element(By.XPATH,"//a[contains(text(),'My Portfolios')]")
    my_portfolios.click()
    time.sleep(5)

    # Favourite

    favourite = driver.find_element(By.XPATH,"//a[contains(text(),'Favorites')]")
    favourite.click()
    time.sleep(2)

    # Pillar of wealth

    pillar_of_wealth = driver.find_element(By.XPATH,"//a[contains(text(),'Pillars of Wealth')]")
    pillar_of_wealth.click()
    time.sleep(2)

    # About the oxford club

    oxford_club = driver.find_element(By.XPATH,"//a[contains(text(),'About The Oxford Club')]")
    oxford_club.click()
    time.sleep(2)

    # Product and service

    service = driver.find_element(By.XPATH,"//a[contains(text(),'Our Products and Services')]")
    service.click()
    time.sleep(2)

    # Investor Resources

    investor_resources = driver.find_element(By.XPATH,"//a[contains(text(),'Investor Resources')]")
    investor_resources.click()
    time.sleep(2)

    # Pillar one advisor

    pillar_advisor = driver.find_element(By.XPATH,"//a[contains(text(),'Pillar One Advisors')]")
    pillar_advisor.click()
    time.sleep(2)

    

    # Benfits

    benfits = driver.find_element(By.XPATH,"//a[contains(text(),'Benefits')]")
    benfits.click()
    time.sleep(2)

    # FQA

    fqa = driver.find_element(By.LINK_TEXT,"FAQ")
    fqa.click()
    time.sleep(2)

    # Event

    event = driver.find_element(By.XPATH,"//a[contains(text(),'Events')]")
    event.click()
    time.sleep(2)



    driver.quit()

for cap in desired_cap:
  Thread(target=run_session, args=(cap,)).start()
