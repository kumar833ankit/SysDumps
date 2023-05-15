"""
#from cProfile import label
#from html import entities
from tkinter import *
#from tkinter import *font,
from tkinter import Entry
import webbrowser
from selenium import webdriver
root = Tk()
root.title("search ")


def search():
        url=enter_box.get()
        webbrowser.open(url)
        browser1 = webdriver.Chrome('chromedriver')
        for i in range(1):
            matched_elements = browser1.get("https://www.google.com/search?q=" +
                                     url + "&start=" + str(i))


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
root.mainloop()
"""




from tkinter import *
import webbrowser
root=Tk()
root.title("Search Bar")
def search():
    url1= ".com"
    #chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    #webbrowser.get(chrome_path).open('http://docs.python.org/')

   
    #url=entry.get().open(url)
    url=entry.get()
    #url +=url1
    webbrowser.open("https://www.google.com/search?q="+url)
    webbrowser.open("https://en.wikipedia.org/wiki/"+url)
    webbrowser.open("https://www.youtube.com/results?search_query="+url)
lable1=Label(root,text="Enter URL here :   ",font=("arial",15,"bold"))
lable1.grid(row=0,column=0)
entry=Entry(root,width=35)
entry.grid(row=0,column=1)
btn=Button(root,text="Search",command=search,bg="blue",fg="white",font=("arial",14,"bold"))
btn.grid(row=1,column=0,columnspan=2,pady=10)
root.mainloop()














from tkinter import *
#from tkinter import *font,
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from tkinter import Entry
import webbrowser
root = Tk()
root.title("search ")


def search():
    url=enter_box.get()
    webbrowser.open(url)
    for i in range(1):
        matched_elements = browser.get("https://www.google.com/search?q=" + url + "&start=" + str(i))
        #
        matched_element = browser2.get("http://www.youtube.com/search?q=" + url + "&start=" + str(i))
        #
        #
        matched_element = browser3.get("http://www.infoplease.com/search?q=" + url + "&start=" + str(i))



label=Label(root,text = "enter url ",font = ("arial",15,"bold"))
label.grid(row=0,column=0)
enter_box = Entry(root, width = 35)
enter_box.grid(row=0,column=1)

btn= Button(root,text ="Search ",bg="blue",fg= "white",font = ("arial", 15,"bold"),command=search)
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





root.mainloop()