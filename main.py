from selenium import webdriver
import time
import pyautogui

class Type:
    def __init__(self):
        self.website = input("Enter Website\n>")
        self.username = input("Enter Username\n>")
        self.password = input("Enter Password\n>")
        self.errors = int(input("Enter Number of Errors\n>"))
        self.times = int(input("Seconds in between lines\n>"))

        self.driver = webdriver.Chrome('Add your path to your web-driver here')

    def login(self):

        self.driver.get(self.website)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[3]/div/button[2]').click()
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/header/div/div[2]/button[1]').click()
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/form/div[1]/div/div[1]/div/input').send_keys(self.username)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/form/div[2]/div/div[1]/div[1]/input').send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/form/div[3]/button[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[1]/div/div/button').click()

    def begin(self):
        time.sleep(3)
        repeat = self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div[2]/div[5]/div').text.split()[0]
        text = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[2]/div[4]').text
        repeat = int(repeat)
        lines = 0
        for x in range(0, self.errors):
            pyautogui.typewrite(' .')
            time.sleep(2)

        while lines != repeat:
            repeat = self.driver.find_element_by_xpath('/html/body/div/div[1]/div/div[2]/div/div/div[2]/div[5]/div').text.split()[0]
            repeat = int(repeat)
            pyautogui.typewrite(text)
            text = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[2]/div[4]').text
            lines += 1
            time.sleep(self.times)

        print('Lines Complete')

if __name__ == '__main__':
    start = Type()
    start.login()
    start.begin()
