from tkinter import *  
import requests
from bs4 import BeautifulSoup as soup
from PIL import ImageTk,Image
from selenium import webdriver
from bs4 import BeautifulSoup
import time 

def send_mail(url,price,product):
    msg = product + " is now available for " +price+" Purchase it by visiting : "+url
    print(msg)

    import smtplib

    sender = "emailid@gmail.com"
    receiver = ["reciever@gmail.com"]

    try:    
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login('emailid@gmail.com', 'email_password')
        print("logged in")
        session.sendmail(sender,receiver,msg)
        print("email sent")
        session.quit()

    except smtplib.SMTPException as e:
        print(e)

       
def flipkart(url,pricex):
    driver = webdriver.Chrome(r'C:\Users\Mohan Dono\Desktop\chromedriver.exe')  
    next_time = time.time()
    while True:
        root = Tk()  
        L = Label(root,text="Enter Expected Price")
        L.pack()
        E = Entry(root,bd=10)
        E.pack()
        Prod = Label(root,text = " " )
        Prod.pack()
        Req_Price = Label(root,text = " Extpected Price : "+str(pricex))
        Req_Price.pack()
        Curr_Price = Label(root,text = " " )
        Curr_Price.pack()
        driver.get(url)
        html = driver.page_source
        page = soup(html)
        product = page.find('span',{'class':'_35KyD6'})
        price = page.find('div',{'class':'_1vC4OE _3qQ9m1'})
        Prod['text']=product.text
        Curr_Price['text']=" Current Price : " + price.text
        if int(price.text.replace("₹","")) <= pricex:
            send_mail(url,price.text,product.text)
        next_time += 20
        time.sleep(max(0, next_time - time.time()))
        root.mainloop()


def amazon(url,pricex):
  
    driver = webdriver.Chrome(r'C:\Users\Mohan Dono\Desktop\chromedriver.exe')  
    next_time = time.time()
    while True:
        root = Tk()  
        L = Label(root,text="Enter Expected Price")
        L.pack()
        E = Entry(root,bd=10)
        E.pack()
        Prod = Label(root,text = " " )
        Prod.pack()
        Req_Price = Label(root,text = " Extpected Price : "+str(pricex))
        Req_Price.pack()
        Curr_Price = Label(root,text = " " )
        Curr_Price.pack()
        driver.get(url)
        html = driver.page_source
        page = soup(html)
        product = page.find('span',{'class':'a-size-large'})
        price = page.find('span',{'class':'a-size-medium a-color-price priceBlockBuyingPriceString'})
        Prod['text']=product.text.replace(" ","")
        Curr_Price['text']=" Current Price : " + price.text
        cp = price.text[2:]
        print(cp)
        if int(float(cp)) <= pricex:
            send_mail(url,price.text,product.text)
        next_time += 20
        time.sleep(max(0, next_time - time.time()))
        root.mainloop()

#amazon("https://www.amazon.in/Dettol-Body-Wash-shower-Refresh/dp/B07XTSQT4R/ref=sr_1_10?dchild=1&keywords=dettol&qid=1588054958&sr=8-10",800)