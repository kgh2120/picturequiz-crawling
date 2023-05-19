import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib import request


driver = webdriver.Chrome()


driver.get("https://superkts.com/people/list/")
datas = driver.find_elements(By.TAG_NAME, "tr")
for i in range(1, 248):

    driver.get("https://superkts.com/people/list/?p=" + str(i))
    time.sleep(2)

    datas = driver.find_elements(By.TAG_NAME, "tr")
    for data in datas:

        attribute = data.get_attribute('innerHTML')
        split = attribute.split("</td>")
        length = len(split)
        ex = ""
        for j in range(1, 3):
            if length < 2:
                continue
            index = split[j].index(">")
            # print(split[i][index+1:])
            ex += split[j][index + 1:] + " "
        # print(ex)
        dataList.append(ex)

driver.close()
print("크롤링 끝났심더")

file = open("C:\\Users\\kgh21\\OneDrive\\Desktop\\data.txt", 'w')

for d in dataList:
    file.write(d+"\n");

file.close()

print("파일 변환 끝났심더")
