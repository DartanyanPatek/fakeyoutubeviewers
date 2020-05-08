from selenium import webdriver
from threading import Thread
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from threading import Thread
import threading

link = input("Input Link: ")
threads = input("Input Threads: ") 
video_time = input("Input your video time: ")

def main():
    while True:
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=3')
        options.add_argument('headless')
        options.add_argument("--mute-audio")
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(link)
        print("Перешел по ссылке") 
        driver.find_element_by_xpath('//*[@id="movie_player"]/div[4]/button').click()
        print("Кликнул на просмотр") 
        print("Смотрю видео") 
        time.sleep(int(video_time))
        print("Посмотрел видео. END")
        driver.close()

for i in range(int(threads)):
    threading.Thread = Thread(target=main).start()
