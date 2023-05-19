import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib import request

driver = webdriver.Chrome()

f = open('converted.txt', 'r', encoding='UTF-8')

lines = f.readlines()
for line in lines:
    line = line.strip()

    path = "https://www.google.com/search?q="+line+"&newwindow=1&sxsrf=ALiCzsYsCyjB4JBREwqbrQFnAbQmppVx9w:1668657998937&source=lnms&tbm=isch&sa=X&ved=2ahUKEwirxJy6q7T7AhVNkVYBHSJ0DqoQ_AUoAXoECAEQAw&cshid=1668658016783529&biw=1536&bih=810&dpr=1.25"
    driver.get(path)
    time.sleep(3)
    area = driver.find_elements(By.CLASS_NAME, "PNCib")
    area[0].click()

    img = driver.find_elements(By.CSS_SELECTOR, "img.n3VNCb")[0]
    src = img.get_attribute("src")
    opener = request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozila/5.0')]
    request.install_opener(opener)

    request.urlretrieve(src, line+".jpg")
    time.sleep(3)

f.close()
