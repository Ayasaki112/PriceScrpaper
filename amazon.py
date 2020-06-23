def search(var):
	from bs4 import BeautifulSoup as soup
	from selenium import webdriver

	url = 'https://www.amazon.in/s?k='+var.replace(" ","+")+'&ref=nb_sb_noss_2'

	driver = webdriver.Chrome(r'C:\Users\Mohan Dono\Desktop\chromedriver.exe')
	driver.get(url)

	html = driver.page_source
	page = soup(html)
	products=[]
	links=[]
	prices=[]
	imgs=[]

	jobs = page.find_all('div',{"class":"a-section a-spacing-medium"})

	for job in jobs:
		product_name = job.find('span',{'class':'a-size-base-plus a-color-base a-text-normal'})
		#product_name = product_name.text if product_name else "N/A"
       
		product_offer_price = job.find('span',{'class':'a-offscreen'})
		product_offer_price = product_offer_price.text if product_offer_price else "N/A"

		#product_mrp = job.find('div',{'class':'_3auQ3N'})
		#product_mrp = product_mrp.text if product_mrp else "N/A"

		product_link = job.find('a',{'class':'a-link-normal a-text-normal'})
		product_link = product_link.get('href') if product_link else "N/A"
		product_link = 'https://www.amazon.in'+ product_link

		product_img = job.find('img',{'class':'s-image'})['src']
		products.append(product_name.text)
		prices.append(product_offer_price)
		imgs.append(product_img)
		links.append(product_link)
		print(links)
		#print("Item : ",product_name.text," Priced ",product_offer_price," img ",product_img)
	return(products,prices,imgs,links)
