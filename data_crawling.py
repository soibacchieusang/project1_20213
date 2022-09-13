from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import json
import csv

#1 khai báo biến browser
q_a = []
browser = webdriver.Chrome(executable_path='chromedriver.exe')

for page_number in range(1,102,1):
    browser.get('https://ts.hust.edu.vn/hoi-dap?page=' + str(page_number))
    sleep(2)
    titles = browser.find_elements(By.CLASS_NAME, 'item-faq')
    for title in titles:
        try:
            answer_texts = title.find_element(By.CSS_SELECTOR, '.high-comment .desc-cmt')
            paragraph = answer_texts.find_elements(By.CSS_SELECTOR, 'p')
            answer = ''
            for i in paragraph:
                answer += i.text +' '
                
        except:
            answer = ''
    

        question = title.find_element(By.CLASS_NAME, 'faq-title').text
        
        qa_dict = {}
        qa_dict ['questions'] = question
        qa_dict ['answers'] = answer
        q_a.append(qa_dict)

browser.close()
try:
    with open('data1.csv', 'w', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['questions', 'answers'])
        writer.writeheader()
        for data in q_a:
            writer.writerow(data)
except IOError:
    print("I/O error")

        
    

