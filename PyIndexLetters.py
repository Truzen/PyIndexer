#/usr/bin/env Python3

from selenium import webdriver
from selenium.webdriver.edge.options import Options
import pyautogui as pag
import re
from PIL import ImageGrab, Image
import pytesseract
import numpy as np
import sys


pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def scangrab():
    pic = ImageGrab.grab(all_screens=True, bbox=(950, 600, 1500, 1200))
    pic.save("ss.png")
    #pic.show()

    imgl = np.array(Image.open("ss.png"))
    text = pytesseract.image_to_string(imgl)

    #print(text)
    return text

def matchID(passTarget):

    #TODO Build catch for detection of space between letters and numbers ex: SNP 146
    targetID = re.compile(r"\w{3}(\s)?\d{3}")
    resultID = targetID.search(passTarget)
    return resultID.group()

def webLaunch():
    opt = Options()
    opt.add_experimental_option("detach", True)
    
    browser = webdriver.Edge(options=opt)
    browser.get("https:\\www.cnn.com")
    browser.find_element_by_class_name("cd___headline").click()

def pagNav():
    if (pag.pixelMatchesColor(88, 188, (44,149,221)) or pag.pixelMatchesColor(750, 197, (235,235,235)))== True:
        try:
            pag.click(1657,235,2)
            pag.typewrite(matchID(scangrab()))
            pag.hotkey('ctrl', 'a')
            pag.sleep(1.75)
            pag.hotkey('ctrl', 'd')
            pag.sleep(1.75)
        except Exception as error:
            print(error)
    elif pag.pixelMatchesColor(770, 204, (247, 184, 11)):
        try:
            pag.hotkey('ctrl', 'r')
            pag.sleep(2)
            pag.hotkey('ctrl', 'd')
            pag.sleep(1)
        except Exception as error:
            print(error)
    else:
        pag.sleep(15)
        pagNav()

class ColorMismatch(Exception):
    pass

def main():

   #webLaunch()
    '''
    target = scangrab()
    IDtoprocess = matchID(target)
    print(IDtoprocess
    '''
    target = input("What's the count? ")
    tempCount = 0
    while tempCount<int(target):
        pagNav()
        tempCount +=1
    
main()
