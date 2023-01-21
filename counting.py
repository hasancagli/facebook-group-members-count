from selenium import webdriver
import time

browser = webdriver.Firefox()

# To Login to Facebook
time.sleep(80)

browser.get("https://www.facebook.com/groups/<GROUPid>/members/")
time.sleep(1)

def takeAllNames() :
    names =  []
    list1 = []

    browser.get("https://www.facebook.com/groups/<GROUPid>/members/")
    time.sleep(5)
    
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(5)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount == lenOfPage:
            match=True
    time.sleep(5)

    people = browser.find_elements_by_class_name("uiProfileBlockContent")
    for e in people :
        names.append(e.text)
    
    return names, len(names)

names, length = takeAllNames()
