import time

from behave import *
from selenium import webdriver
import time

@when(u'we visit google')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="C:\\Users\\mahid\\BehaveProject\\driver\\chromedriver.exe")
    context.driver.get('https://www.google.com')
    time.sleep(10)


@then(u'it should have a title "Google"')
def step_impl(context):
    assert context.browser.title == "Google"
