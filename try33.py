#from cProfile import label
#from html import entities
from tkinter import *
#from tkinter import *font,
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Entry
import webbrowser
root = Tk()
root.title("search ")


def search():
        url=enter_box.get()
        webbrowser.open(url)



label=Label(root,
               text = "enter url ", 
               font = ("arial",15,"bold"))
label.grid(row=0,column=0)
enter_box = Entry(root, width = 35)
enter_box.grid(row=0,column=1)
btn= Button(root,
text ="Search ",
bg="blue",
fg= "white",
font = ("arial", 15,"bold"))
btn.grid(row=1, column=0)
browser = webdriver.Chrome('chromedriver')
#browser.maximize_window()
browser2 = webdriver.Chrome('chromedriver')
#browser2.maximize_window()
browser3 = webdriver.Chrome('chromedriver')
#browser3.maximize_window()

browser.set_window_size(480, 320)
browser.set_window_position(480, 320)
browser2.set_window_size(480, 320)
browser.set_window_position(480, 320)
browser3.set_window_position(35, 320)
browser3.set_window_size(480, 320)



for i in range(1):


	matched_elements = browser.get("https://www.google.com/search?q=" +
									url + "&start=" + str(i))

matched_element =  browser2.get("http://www.youtube.com/search?q=" + 
                                url + "&start=" + str(i))




matched_element =  browser3.get("http://www.infoplease.com/search?q=" + 
                                url + "&start=" + str(i))




root.mainloop()
