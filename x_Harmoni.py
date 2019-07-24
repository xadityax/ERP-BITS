# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:00:48 2019

@author: Aditya Agarwal
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:05:33 2019

@author: Aditya Agarwal
"""

from tkinter import *
from tkinter.filedialog import askdirectory
import selenium
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from PIL import ImageTk
from PIL import Image

import threading
from threading import Thread

#ids=str(input("Give id number: "))
#passw=str(input("Give pass: "))

cwd = os.getcwd()
print (cwd)
def do_it():
    def callback():
        window = Toplevel(root)
        window.title("xHARMONI")
        window.geometry("200x100")
        headings=Label(window,text="Working...")
        headings.pack(side="bottom",fill="both",expand="yes")
        delay=30
        WINDOW_SIZE = "1920,1080"
        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        #chrome_options.binary_location = CHROME_PATH
        chrome_path=(r"{}\chromedriver.exe".format(cwd))
        driver=webdriver.Chrome(executable_path=chrome_path,chrome_options=chrome_options)
        delay=30
        driver.maximize_window()
        #introducing waiting time till the webpage is fully loaded
        wait = WebDriverWait(driver, 40)
        driver.get("https://erp.bits-pilani.ac.in:4431/psp/hcsprod/?cmd=login&languageCd=ENG")
        wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="userid"]')))
        #pressing all the buttons required to download the gct file with connections
        driver.find_element_by_xpath('//*[@id="userid"]').send_keys("{}".format(str(names.get())))
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="pwd"]')))
        driver.find_element_by_xpath('//*[@id="pwd"]').send_keys("{}".format(str(names2.get())))
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.XPATH,'/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[1]/td/table[2]/tbody/tr[5]/td[3]/input')))
        driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr[1]/td/table[2]/tbody/tr[5]/td[3]/input').click()
        wait = WebDriverWait(driver, 5)
        time.sleep(2)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="fldra_CO_EMPLOYEE_SELF_SERVICE"]')))
            driver.find_element_by_xpath('//*[@id="fldra_CO_EMPLOYEE_SELF_SERVICE"]').click()
            #wait = WebDriverWait(driver, 5)
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="crefli_HC_SSS_STUDENT_CENTER"]/a')))
            driver.find_element_by_xpath('//*[@id="crefli_HC_SSS_STUDENT_CENTER"]/a').click()
            seq = driver.find_elements_by_tag_name('iframe')
    
            print("No of frames present in the web page are: ", len(seq))
    
            iframe = driver.find_element_by_id('ptifrmtgtframe')
    
            driver.switch_to.frame(iframe)
            driver.find_element_by_xpath('//*[@id="DERIVED_SSS_SCL_SSS_MORE_ACADEMICS"]').click()
            driver.find_element_by_xpath('//*[@id="DERIVED_SSS_SCL_SSS_MORE_ACADEMICS"]/option[7]').click()
            wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="DERIVED_SSS_SCL_SSS_GO_1"]/img')))
            driver.find_element_by_xpath('//*[@id="DERIVED_SSS_SCL_SSS_GO_1"]/img').click()
            for i in range(1,15):
                try:
                    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="SSR_DUMMY_RECV1$sels$0"]')))
                    driver.find_element_by_xpath('(//*[@id="SSR_DUMMY_RECV1$sels$0"])[{}]'.format(i)).click()
                    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="DERIVED_SSS_SCT_SSR_PB_GO"]')))
                    driver.find_element_by_xpath('//*[@id="DERIVED_SSS_SCT_SSR_PB_GO"]').click()
                    wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="DERIVED_SSS_SCT_SSS_TERM_LINK"]')))
                    #driver.execute_script("document.body.style.zoom='70%'")
                    driver.save_screenshot(r"{}\Grades{}.png".format(cwd,i))
                    #driver.execute_script("document.body.style.zoom='100%'")
                    driver.find_element_by_xpath('//*[@id="DERIVED_SSS_SCT_SSS_TERM_LINK"]').click()
                except Exception:
                    window.destroy()
    
            driver.quit()
        except Exception:
            window.destroy()
            window2 = Toplevel(root)
            window2.title("xHARMONI")
            window2.geometry("200x100")
            headings=Label(window2,text="Wrong credentials..")
            headings.pack(side="bottom",fill="both",expand="yes")
            driver.quit()
            window2.destroy()
    t = threading.Thread(target=callback)
    t.start()   



root=Tk()
root.title("xHARMONI")
root.geometry("500x300")
#canvas=Canvas(width=500,height=300)
#Display text instructions
image = Image.open('{}\image.png'.format(cwd))
tkimage=ImageTk.PhotoImage(image)
#canvas_object=canvas.create_image(25,25,image=tkimage)
panel=Label(root,image=tkimage)
panel.pack(side="bottom",fill="both",expand="yes")
#angle = 0
#while True:
 #   tkimage=ImageTk.PhotoImage(image.rotate(angle))
  #  canvas_object=canvas.create_image(25,25,image=tkimage)
   # canvas.delete(canvas_object)
   # angle+=10
    #angle%=360


heading2=Label(root,text="Hello Kids. ").place(x=215,y=50)
heading=Label(root,text="Please enter your ID number. (41120XXYYYY)").place(x=130,y=76)
heading=Label(root,text="Please enter your ERP password.").place(x=159,y=125)
heading3=Label(root,text="Don't take CG lite.").place(x=400,y=275)
#heading4=Label(root,text="v1.2").place(x=5,y=275)
#heading=Label(root,text="Select function to perform and specify directory to save data").place(x=100,y=170)
names=StringVar()
names2=StringVar()
entry_box=Entry(root, textvariable=names, width=48, bg="red").place(x=99,y=102)
entry_box2=Entry(root, textvariable=names2, width=48, bg="red").place(x=99,y=150)

work=Button(root,text="Get my CG!",width=16,height=2,bg="lightblue", command=do_it).place(x=115,y=195)
work=Button(root,text="IDGAF",width=16,height=2,bg="lightblue", command=root.destroy).place(x=249,y=195)
#browse button 
#work=Button(root,text="Browse",width=20,height=1,bg="lightgray", command=lambda: do_it_3(1)).place(x=178,y=143)
root.mainloop()

