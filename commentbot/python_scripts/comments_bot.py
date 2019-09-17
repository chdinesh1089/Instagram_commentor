from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from commentbot.models import Page
from django.contrib.auth.models import User

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def signIn(driver,usr,pas):
    username=driver.find_element_by_name('username')
    password=driver.find_element_by_name('password')
    login= driver.find_element_by_xpath('//*[text()="Log In"]')
    #login = WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.CLASS_NAME, "_0mzm"))

    #)
    username.send_keys(usr)
    password.send_keys(pas)
    login.click()


def comment(driver,cmnt):
    post= driver.find_element_by_class_name('eLAPa')
    cmt_actns = ActionChains(driver)
    cmt_actns.send_keys(cmnt)
    cmt_actns.send_keys(Keys.RETURN)
    post.click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@aria-label="Add a comment…"]').click()
    cmt_actns.perform()
    time.sleep(1)
    driver.find_element_by_class_name('ckWGn').click()
def isNew(driver,account_id):
    account_object = Page.objects.get(account_id=account_id)
    postId = account_object.latest_post_id
    post=driver.find_element_by_xpath('//*[@class="v1Nh3 kIKUG  _bz0w"]')
    soup = BeautifulSoup(post.get_attribute('innerHTML'), 'html.parser')
    latest_id = soup.find_all('a')[0].get('href')
    if(latest_id!=postId):
        account_object.latest_post_id =latest_id
        account_object.save()
        return True
    return False


if __name__ == '__main__':
    driver =webdriver.Firefox()
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(1)
    signIn(driver,"pavanghanacmnts","PavanGhana")
    time.sleep(2)
    driver.get('https://www.instagram.com/dextergen1985/')
    while True:
            if(isNew(driver)):
               comment(driver,"damn! we made it")
               time.sleep(30)
            else:
                driver.refresh()
                time.sleep(30)

def start_monitoring(account_id,current_user):
    driver =webdriver.Firefox()
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)
    current_user = User.objects.get(username=current_user)
    current_user = current_user.logindetails_set.get()
    signIn(driver,current_user.account_id,current_user.password)
    time.sleep(2)
    page_url = 'https://www.instagram.com/' + account_id +'/'
    driver.get(page_url)
    while True:
        account_object = Page.objects.get(account_id=account_id)
        if(account_object.run_status=='no'):
            driver.quit()
        if(isNew(driver,account_id)):
               comment(driver,account_object.comment)
               time.sleep(30)
        else:
            driver.refresh()
            time.sleep(5)
