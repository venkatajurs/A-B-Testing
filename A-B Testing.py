#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
from datetime import date,timedelta
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as po


# In[2]:


con_data=pd.read_csv('control_group.csv',sep=';')
test_data=pd.read_csv('test_group.csv',sep=';')


# In[3]:


con_data.head()


# In[4]:


test_data.head()


# In[5]:


con_data.columns=['Campaign Name','Date','Amount Spend','No of Impressions','Reach','Website Clicks','Searches','Content Views','Add to cart','Purchases']


# In[6]:


test_data.columns=['Campaign Name','Date','Amount Spend','No of Impressions','Reach','Website Clicks','Searches','Content Views','Add to cart','Purchases']


# In[7]:


con_data.isnull().sum()


# In[8]:


test_data.isnull().sum()


# In[9]:


con_data['No of Impressions'].fillna(value=con_data['No of Impressions'].mean(),inplace= True)
con_data['Reach'].fillna(value=con_data['Reach'].mean(),inplace= True)
con_data['Website Clicks'].fillna(value=con_data['Website Clicks'].mean(),inplace= True)
con_data['Searches'].fillna(value=con_data['Searches'].mean(),inplace= True)
con_data['Content Views'].fillna(value=con_data['Content Views'].mean(),inplace= True)
con_data['Add to cart'].fillna(value=con_data['Add to cart'].mean(),inplace= True)
con_data['Purchases'].fillna(value=con_data['Purchases'].mean(),inplace= True)


# In[25]:


#merge both data sets


# In[10]:


ab_data=con_data.merge(test_data,how='outer').sort_values(['Date'])


# In[11]:


ab_data=ab_data.reset_index(drop=True)
ab_data.head()


# In[33]:


#ab testing by comparing two marketing strategey


# In[12]:


fig=px.scatter(data_frame=ab_data,x='No of Impressions',y='Amount Spend',size='Amount Spend',color='Campaign Name',trendline='ols')
fig.show()


# In[13]:


fig=px.scatter(data_frame=ab_data,x='Website Clicks',y='Content Views',size='Amount Spend',color='Campaign Name',trendline='ols')
fig.show()


# In[14]:


fig=px.scatter(data_frame=ab_data,x='Content Views',y='Add to cart',size='Content Views',color='Campaign Name',trendline='ols')
fig.show()


# In[40]:


#no of searches in both campaigns


# In[15]:


label = ["Total Searches from Control Campaign", 
         "Total Searches from Test Campaign"]
counts = [sum(con_data["Searches"]), 
          sum(test_data["Searches"])]
colors = ['lightblue','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Searches of campaigns: Control Vs Test')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# In[16]:


label = ["Total Searches from Control Campaign", 
         "Total Searches from Test Campaign"]
counts = [sum(con_data["No of Impressions"]), 
          sum(test_data["No of Impressions"])]
colors = ['lightblue','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='No of Impressions of campaigns: Control Vs Test')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# In[17]:


label = ["Total Searches from Control Campaign", 
         "Total Searches from Test Campaign"]
counts = [sum(con_data["Reach"]), 
          sum(test_data["Reach"])]
colors = ['lightblue','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Reach of campaigns: Control Vs Test')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# In[18]:


label = ["Total Searches from Control Campaign", 
         "Total Searches from Test Campaign"]
counts = [sum(con_data["Website Clicks"]), 
          sum(test_data["Website Clicks"])]
colors = ['lightblue','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Website clicks of campaigns: Control Vs Test')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# In[19]:


label = ["Total Searches from Control Campaign", 
         "Total Searches from Test Campaign"]
counts = [sum(con_data["Content Views"]), 
          sum(test_data["Content Views"])]
colors = ['lightblue','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Content views of campaigns: Control Vs Test')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# In[20]:


label = ["Total Searches from Control Campaign", 
         "Total Searches from Test Campaign"]
counts = [sum(con_data["Add to cart"]), 
          sum(test_data["Add to cart"])]
colors = ['lightblue','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Searches of campaigns: Control Vs Test')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# In[21]:


label = ["Total Searches from Control Campaign", 
         "Total Searches from Test Campaign"]
counts = [sum(con_data["Amount Spend"]), 
          sum(test_data["Amount Spend"])]
colors = ['lightblue','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Amount spend of campaigns: Control Vs Test')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# In[22]:


label = ["Total Searches from Control Campaign", 
         "Total Searches from Test Campaign"]
counts = [sum(con_data["Purchases"]), 
          sum(test_data["Purchases"])]
colors = ['lightblue','lightgreen']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Purchases of campaigns: Control Vs Test')
fig.update_traces(hoverinfo='label+percent', textinfo='value', 
                  textfont_size=30,
                  marker=dict(colors=colors, 
                              line=dict(color='black', width=3)))
fig.show()


# In[ ]:


#In comparisons of percentage of both tests test campaign secured more percentage in each category but we need to conversion
#rate by using scatter plots


# In[23]:


fig=px.scatter(data_frame=ab_data,x='Purchases',y='Add to cart',size='Purchases',color='Campaign Name',trendline='ols')
fig.show()


# In[ ]:


#test campaign has highest conversion rate compared to control campaign rate instead of having highest purchases


# In[24]:


fig=px.scatter(data_frame=ab_data,x='Website Clicks',y='Add to cart',size='Website Clicks',color='Campaign Name',trendline='ols')
fig.show()


# In[88]:


#contol campaign and test campaign has eqaul range of add to cart but control campaign has better conversion rate compared to 
#test campaign 


# In[ ]:


#Conclusion:
#From both visualizations say percentage of each campaign and conversion rate of each campaigns, control campaigns has capable to 
#reach mass audience and its be used. test campaign may not high conversion rate but it has capable of market specific product for 
#specific audience.

