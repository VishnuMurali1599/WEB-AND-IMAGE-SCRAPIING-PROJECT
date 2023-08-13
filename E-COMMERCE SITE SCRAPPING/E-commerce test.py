import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
webpage=requests.get(url).text
#print(webpage)
soup=BeautifulSoup(webpage,"html.parser")
#print(soup)


## Fetching Records From Webpage

Web_details=soup.find_all('div')

Computer_Name=[]
for i in soup.find_all('a',class_='title'):
    Computer_Name.append(i.text.strip())
    
#print(Computer_Name)

Price=[]
for i in soup.find_all('h4',class_="pull-right price"):
    Price.append(i.text)
    
#print(Price)


### Here we are fetching from div class separately
Product_Details=soup.find_all("div",class_='caption')
Product_Detailed_Name=[]
Display_Details=[]
Processor=[]
Ram=[]
SSD=[]
for i in Product_Details:
    try:
        Product_Detailed_Name.append(i.find('p').text.split(",")[0])
    except:
        Product_Detailed_Name.append(np.nan)
        
    
    try:
        Display_Details.append(i.find('p').text.split(",")[1])
    except:
        Display_Details.append(np.nan)
        
        
    try:
        Processor.append(i.find('p').text.split(",")[2])
    except:
        Processor.append(np.nan)
        
    try:
        Ram.append(i.find('p').text.split(",")[3])
    except:
        Ram.append(np.nan)
        
        
    try:
        SSD.append(i.find('p').text.split(",")[4])
    except:
        SSD.append(np.nan)
        
#print(Product_Detailed_Name) 
#print(Display_Details)
#print(Processor)
#print(Ram)
#print(SSD)


Ratings=[]
for i  in soup.find_all('p',class_="pull-right"):
    Ratings.append(i.text)
    
#print(Ratings)


d={'System_Name':Computer_Name,'Product_Name':Product_Detailed_Name,'Display_Details':Display_Details,'Proccessor':Processor,"RAM":Ram,"SSD":SSD,"Price":Price,"Ratings":Ratings}

#print(d)

print(pd.DataFrame(d))


