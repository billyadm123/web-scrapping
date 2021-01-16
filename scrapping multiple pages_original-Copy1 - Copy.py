#!/usr/bin/env python
# coding: utf-8

# In[55]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[56]:




url = 'https://www.ebay.com/b/Other-Natural-Remedies/1279?Type=Ear%2520Candle%7CCandles%7CEssential%2520Oils%7CHerb%7CHerbal%2520Plaster%7CHerbs%7CHerbs%2520%2526%2520Resins%7CPendant%7CSalt%2520Pipe%7CSuppositories%7C%21%7CTea&rt=nc'


# In[57]:


source = requests.get(url)


# In[58]:


source


# In[59]:


soup = BeautifulSoup(source.text, 'html.parser')


# In[60]:


#soup


# In[61]:


main_content = soup.find('div', attrs = {'id':'mainContent'})


# In[62]:


#main_content


# In[63]:


items = main_content.find('div', attrs = {'class': 's-item__info clearfix'})


# In[65]:


product_list = []
for i in range(1, 50):
    source = requests.get('https://www.ebay.com/b/Other-Natural-Remedies/1279?Type=Ear%2520Candle%7CCandles%7CEssential%2520Oils%7CHerb%7CHerbal%2520Plaster%7CHerbs%7CHerbs%2520%2526%2520Resins%7CPendant%7CSalt%2520Pipe%7CSuppositories%7C%21%7CTea&rt=nc&_pgn={i}')
    for i in main_content.find_all('div', attrs = {'class': 's-item__info clearfix'}):
        product = i.find_all('h3', attrs={'class':'s-item__title'})
        info = i.find_all('span', attrs={'class': 's-item__price'})
        sold = i.find_all('span', attrs={'class':'NEGATIVE'})
        products = {
            'product': product,
            'info': info,
            'amount sold': sold
        }
        
        product_list.append(products)


# In[66]:


df = pd.DataFrame(product_list)


# In[67]:


df.head()


# In[ ]:




