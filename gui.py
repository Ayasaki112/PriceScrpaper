
import urllib.request
from tkinter import *
from PIL import ImageTk,Image
import flipkart
import amazon
import new1
aproducts =[]
aprices =[]
aimg=[]
fproducts =[]
fprices =[]
fimg=[]
flinks=[]
alinks=[]
link_list = []
prod_list = ["None"]
countr = 1

def searchonline():
    (fproducts,fprices,fimgs)=flipkart.search(E1.get())
    (aproducts,aprices,aimgs)=amazon.search(E1.get())
    #print("Flipkart Results")
    btn = Button(root,text = " FLIPKART RESULTS ")
    btn.grid(row=3,column=0)
    btn = Button(root,text = " AMAZON RESULTS ")
    btn.grid(row=3,column=1)
    for i in range(0,5):#len(fproducts)):
        #Flipkart results
        txt=str(fproducts[i]+" Priced : "+fprices[i])
        btn = Button(root, text=txt)
        btn.grid(row=i+5,column=0)
        #Amazon products on right
        txt=str(aproducts[i]+" Priced : "+aprices[i])
        btn = Button(root, text=txt)
        btn.grid(row=i+5,column=1)
        #print(" I am visiting ",aimgs[i])
        resource = urllib.request.urlopen(str(aimgs[i]))
        filename = "img" + str(i) + ".jpg"
        output = open(filename,"wb")
        output.write(resource.read())
        output.close()
        try:
            print("Opening image : ",filename)
            canvas = Canvas(root, width = 300, height = 300)
            canvas.grid(row=i+5,column=2)
            img = ImageTk.PhotoImage(Image.open("img0.jpg"))
            canvas.create_image(20,20, anchor=NW, image=img)
        except IOError:
            pass

def DisplayImage(Expected_price):  

    img_file = str(variable2.get())
    print("Entered Display Image Function to look for ",img_file)
    for i in range (0,len(prod_list)):
        if prod_list[i] == img_file:
            
            img = "img"+str(i)+".jpg"
            image = Image.open(img)
            image.show()
            print("opening new form with url "+link_list[i-1])
            if variable.get() == "FLIPKART":
                new1.flipkart(link_list[i-1],Expected_price)
            elif variable.get() == "AMAZON":
                new1.amazon(link_list[i-1],Expected_price)

def addToList():
    
    file = open(variable.get()+".txt","a")
    for i in range(0,len(prod_list)):
        if prod_list[i]==str(variable2.get()):
            file.write(link_list[i-1]+"\n")
            print(" Writing "+link_list[i-1])
            file.close()
            print(" Successfully written to the file")
    return 
    
def searchselection():
    print (" Searching :" + variable.get())
    selected_link = ""
    if(str(variable.get()) == "AMAZON" ):
        (aproducts,aprices,aimgs,alinks)=amazon.search(E1.get())
        for i in range(0,5):
            txt=str(aproducts[i]+" Priced : "+aprices[i])
            #append resulting products in a drop down list and save those images
            prod_list.append(txt)
            link_list.append(alinks[i])
            #print(" I am visiting ",aimgs[i])
            resource = urllib.request.urlopen(str(aimgs[i]))
            filename = "img" + str(len(prod_list)) + ".jpg"
            print( "added ",filename," for ",prod_list[len(prod_list) - 1])
            output = open(filename,"wb")
            output.write(resource.read())
            output.close()
            
        w2 = OptionMenu(root,variable2,*prod_list)
        w2.pack()
        LP = Label(root,text = "Enter the expected price for the selected product")
        LP.pack()
        EP = Entry(root,bd=5)
        EP.pack()
        B2 = Button(root, text ="Display image and Add to watchlist", command = lambda : DisplayImage(int(EP.get())))
        B2.pack()
    
    elif (str(variable.get()) == "FLIPKART" ):
        (fproducts,fprices,fimgs,flinks)=flipkart.search(E1.get())
        for i in range(0,5):
            txt=str(fproducts[i]+" Priced : "+fprices[i])
            prod_list.append(txt)
            link_list.append(flinks[i])
            resource = urllib.request.urlopen(str(fimgs[i]))
            filename = "img" + str(len(prod_list)) + ".jpg"
            print( "added ",filename," for ",prod_list[len(prod_list) - 1])
            output = open(filename,"wb")
            output.write(resource.read())
            output.close()
        
        w2 = OptionMenu(root,variable2,*prod_list)
        w2.pack()
        LP = Label(root,text = "Enter the expected price for the selected product")
        LP.pack()
        EP = Entry(root,bd=5)
        EP.pack()
        B2 = Button(root, text ="Display image and Add to watchlist", command = lambda : DisplayImage(int(EP.get())))
        B2.pack()
    
    #B3 = Button(root, text = " Add to list " , command = lambda : addToList)
    #B3.pack()
    

root = Tk()
root.attributes("-fullscreen", True)
w = Label(root, text="Multi Platform Price Checker")
w.pack()#grid(row=0,column=1)#pack()
L1 = Label(root, text="Product Name")
L1.pack()#grid(row=1,column=0)# side = LEFT)
E1 = Entry(root, bd =5)
E1.pack()#grid(row=1,column=1)#pack()#side = RIGHT)
OPTIONS = ["AMAZON" , "FLIPKART"]
variable = StringVar(root)
variable.set(OPTIONS[0]) 
variable2 = StringVar(root)
variable2.set(prod_list[0])
w = OptionMenu(root, variable, *OPTIONS)
w.pack()
B = Button(root, text ="Search", command = searchselection )
B.pack()#grid(row=1,column=2)#pack()#grid(column = 3,row = 1)

root.mainloop()