#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors
pio.templates.default = "plotly_white"


# In[5]:


data = pd.read_csv('Sample - Superstore.csv',encoding='latin-1')


# In[7]:


data.head(5)


# In[8]:


data.describe()


# In[9]:


data.info()


#  # Converting Date Columns

# In[12]:


data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])


# In[13]:


data.info()


# In[15]:


data['Order Month'] = data['Order Date'].dt.month
data['Order Year'] = data['Order Date'].dt.year
data['Order Day of Week'] = data['Order Date'].dt.dayofweek


# In[16]:


data.head(3)


# # Monthly Sales Anaylsis

# In[17]:


sales_by_month = data.groupby('Order Month')['Sales'].sum().reset_index()


# In[18]:


sales_by_month


# In[19]:


fig = px.line(sales_by_month, 
              x='Order Month', 
              y='Sales', 
              title='Monthly Sales Analysis')
fig.show()


#  # Sales By Category

# In[21]:


sales_by_category = data.groupby('Category')['Sales'].sum().reset_index()


# In[23]:


sales_by_category


# In[25]:


sales_by_category = data.groupby('Category')['Sales'].sum().reset_index()


fig = px.pie(sales_by_category, 
             values='Sales', 
             names='Category', 
             hole=0.3, 
             color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Sales Analysis by Category', title_font=dict(size=24))

fig.show()


# # Sales Analysis By Sub Category

# In[27]:


data['Sub-Category']


# In[38]:


sales_by_subcategory = data.groupby('Sub-Category')['Sales'].sum().reset_index()


# In[40]:


sales_by_subcategory


# In[41]:


fig = px.bar(sales_by_subcategory,x='Sub-Category',y='Sales',title='Sales Analysis By Sub Category')

fig.show()


# # Monthly Profit Analysis

# In[42]:


profit_by_month = data.groupby('Order Month')['Profit'].sum().reset_index()


# In[43]:


profit_by_month


# In[50]:


fig = px.line(profit_by_month,x='Order Month',y='Profit',title='Monthly Profit Analysis')

fig.show()


# # Profit By Category

# In[51]:


profit_by_category = data.groupby('Category')['Profit'].sum().reset_index()


# In[53]:


profit_by_category


# In[59]:


fig = px.pie(profit_by_category, 
             values='Profit', 
             names='Category', 
             hole=0.4, 
             color_discrete_sequence=px.colors.qualitative.Pastel)

fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Profit Analysis by Category', title_font=dict(size=24))

fig.show()


# In[60]:


profit_by_subcategory = data.groupby('Sub-Category')['Profit'].sum().reset_index()
fig = px.bar(profit_by_subcategory, x='Sub-Category', 
             y='Profit', 
             title='Profit Analysis by Sub-Category')
fig.show()


# # Sales and Profit - Customer Segment

# In[61]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()

color_palette = colors.qualitative.Pastel

fig = go.Figure()
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'], 
                     y=sales_profit_by_segment['Sales'], 
                     name='Sales',
                     marker_color=color_palette[0]))

fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'], 
                     y=sales_profit_by_segment['Profit'], 
                     name='Profit',
                     marker_color=color_palette[1]))

fig.update_layout(title='Sales and Profit Analysis by Customer Segment',
                  xaxis_title='Customer Segment', yaxis_title='Amount')

fig.show()


# # Sales to Profit Ratio

# In[62]:


sales_profit_by_segment = data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
sales_profit_by_segment['Sales_to_Profit_Ratio'] = sales_profit_by_segment['Sales'] / sales_profit_by_segment['Profit']
print(sales_profit_by_segment[['Segment', 'Sales_to_Profit_Ratio']])


# In[ ]:


# Based on the Sales to Profit Ratio:

# The Home Office segment is the most profitable among the three, requiring only ₹7.13 in sales to earn ₹1 in profit.

# The Corporate segment performs slightly worse, needing ₹7.68 in sales for the same ₹1 profit.

# The Consumer segment is the least efficient, needing ₹8.66 in sales to generate ₹1 in profit.

# 🔎 Conclusion:
# The Home Office segment delivers the highest profit efficiency.
# The Consumer segment may need a review of its pricing, cost structure, or marketing focus to improve profitability.
# Strategic business decisions should consider focusing more on Home Office and Corporate segments to enhance overall profitability.

