def search(var):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    import requests
    import pandas as pd
    import time
    driver = webdriver.Chrome(r'C:\Users\Mohan Dono\Desktop\chromedriver.exe')
    #var = "lenovo"#input()
    tp = var
    var.replace(" ","%20")
    imgs=[]#"a","b"] #List to store image urls
    links=[]
    products=[]#"tomato","potato"] #List to store name of the product
    prices=[]#"70","30"] #List to store price of the product
    driver.get("https://www.flipkart.com/search?q="+var+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
    
    content = driver.page_source
    soup = BeautifulSoup(content)#,"html.parser")
    #soup2 = BeautifulSoup(content)
    #print(soup)
    
    
    for a in soup.findAll('div', attrs={'class':'_3liAhj'}):
        img=a.find('img')#,attrs={'class':'_1Nyybr  _30XEf0'})
        name=a.find('a', attrs={'class':'_2cLu-l'})['title']
        #if tp in name.text :
        price=a.find('div', attrs={'class':'_1vC4OE'})
        products.append(name)
        prices.append(price.text)
        #img = img.get('src')
        #print(" img : ",img['src'])
        imgs.append(img['src'])
        link = a.find('a',attrs={'class':"_2cLu-l"})
        link = 'https://www.flipkart.com' + link['href']
        links.append(link)
        print (link)
    
    #print(products)
    #print(prices)
    print(links)
    return (products,prices,imgs,links)
