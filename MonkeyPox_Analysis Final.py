#!/usr/bin/env python
# coding: utf-8

# # Monkey_pox EDA Analysis
# 
# By:- PRIYA KUMARI

# Problem Statement:
# Monkey pox is a newly spreading virus that threatens for a outbreak.
# Our job as Data Scientist is to analyse the given dataset by performing exploratory data analysis.

# # EDA:-
# Is a method of Descriptive Statistics, to evaluate and comprehend data in order to derive insights.
# EDA has 2 categories:-
# 1. Graphical Analysis
# 2. Non Graphical Analysis
# 
# Here we will perform Graphical Analysis, identify the key variables, their correlation with various other variables and gather meaningful insights out of the given datasets.

# # Monkey Pox

# Monkeypox is a viral zoonotic disease(a virus that is transmitted to humans from animals) that occurs primarily in tropical rainforest areas of Central and West Africa and is occasionally exported to other regions.

# # Import All Important Libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly.graph_objects as go


# # Data Collection Source:-
# 1. kaggle.com

# # Loading Monkey_Pox_Cases_Worldwide dataset.
# 

# In[2]:


monkeypox_data = pd.read_csv(r'C:\Users\badal\Downloads\monkeypox\Monkey_Pox_Cases_Worldwide.csv')
monkeypox_data1 = pd.read_csv(r'C:\Users\badal\Downloads\monkeypox new\monkeypox-main\latest.csv')


# In[3]:


monkeypox_data


# # find insights from Monkey_Pox_Cases_Worldwide dataset.

# # Data Cleaning

# In[4]:


monkeypox_data.head(10)


# In[5]:


monkeypox_data.tail(10)


# In[6]:


monkeypox_data.shape


# In[7]:


monkeypox_data1


# In[8]:


monkeypox_data1.shape


# In[9]:


monkeypox_data1.columns


# In[10]:


monkeypox_data.columns


# In[11]:


monkeypox_data1.info()


# In[12]:


monkeypox_data.info()


# # Description of the datasets

# In[13]:


monkeypox_data.describe()


# In[14]:


monkeypox_data1.describe()


# # Missing Values

# In[15]:


monkeypox_data.isnull().sum()


# In[16]:


monkeypox_data1.isnull().sum()


# # Symptoms

# # Symptoms being the most important feature of the Dataset

# In[17]:


# shows the column indicating all the symptoms as an array
# Array:- is a collection of items that are stored at contiguous memory locations;
#it is basically a container which can hold fixed number of items, of the same type.
monkeypox_data1['Symptoms'].unique()


# In[18]:


# shows the number of patients having the respective symptom
monkeypox_data1['Symptoms'].value_counts()


# In[19]:


temp_monkeypoxdata = pd.DataFrame(monkeypox_data1['Symptoms'].value_counts()).reset_index()
temp_monkeypoxdata = temp_monkeypoxdata.append(pd.DataFrame({'index':'multiple or other', 'Symptoms':temp_monkeypoxdata.loc[temp_monkeypoxdata['Symptoms'] < 2]['Symptoms'].sum()},index = [0]))
temp_monkeypoxdata = temp_monkeypoxdata.loc[temp_monkeypoxdata['Symptoms'] > 1]


fig = go.Figure(data = [go.Pie(labels = temp_monkeypoxdata['index'],
                               values = temp_monkeypoxdata['Symptoms'],
                               hole = .75,
                               #title = '% of Symptoms',
                               marker_colors = px.colors.sequential.algae_r,
                              )
                       ])



fig.update_layout(
    title_text = "Distribution of Symptoms",
    template = 'ggplot2',
    height = 600,
    annotations = [dict(text = 'Symptoms',
                      x = 0.5,
                      y = 0.5,
                      font_size = 20,
                      showarrow = False
                     )])



fig.show()


# # Insights
# From above pie chart we can see that genital ulcer lesions is the top symtom for monkey pox.

# # Bar Plot of Country vs Date of Confirmation and Confirmed cases with all other data for overview.
# 
# Other Data considered here are Suspected cases, Hospitalised, Travel History Yes and Travel History No. 

# In[20]:


px.bar(monkeypox_data1, x='Date_confirmation', y='Country',text_auto=True, color= 'Country', height=1500,width=1000,
                   hover_data=monkeypox_data1.columns)


# In[21]:


px.bar(monkeypox_data, x='Country', y='Confirmed_Cases',text_auto=True, color= 'Country', height=1000,width=1000,
                   hover_data=monkeypox_data.columns)


# In[22]:


px.line(monkeypox_data, x='Country', y='Confirmed_Cases', markers=True, title="Country with Confirmed Cases of Monkeypox")


# # Insights
# From above bar plot we conclude that how a particular Country is getting Confirmed cases; ie it shows the velocity of spreading of monkey pox virus.
# 
# From the Line plot we conclude that 
# England has the most number of confirmed cases, which is 180.
# 
# there are no confirmed cases in in countries like Sudan, Iran, Malta, Brazil, Pakistan,Ecuador, Malaysia,Peru.

# In[23]:


px.line(monkeypox_data, x='Country', y='Suspected_Cases', markers=True, title="Country with Suspected Cases of Monkeypox")


# # Insights:
# Fromthe above line plot Spain has the maximum number of Suspected cases ie. 68.

# In[24]:


monkeypox_data1['Hospitalised (Y/N/NA)'].unique()


# In[25]:


monkeypox_data1['Hospitalised (Y/N/NA)'].value_counts()


# In[26]:


plt.figure(figsize=(15,6))
sns.countplot('Hospitalised (Y/N/NA)', data = monkeypox_data1, palette='hls')
plt.xticks(rotation = 90)
plt.show()


# In[27]:


px.line(monkeypox_data, x='Country', y='Hospitalized', markers=True, title="Country with Hospitalised Patients of Monkeypox")


# # Insights:
# The Graph shows that out of the people showing symptoms of monkeypox only 79 were hospitlised and rest 72 were not.
# 
# Line plot shows Germany and Italy have maximum number of hospitalised patients. 

# In[28]:


px.line(monkeypox_data, x='Country', y='Travel_History_Yes', markers=True, title="Country with Travel History")


# # Insights:-
# Italy,US and Germany have maximum people with a travel history, number being 9, 9 and 8 respectively.

# In[29]:


px.line(monkeypox_data, x='Country', y='Travel_History_No', markers=True, title="Country with No Travel History")


# # Insights
# Portugal has 34 patients with no travel history.

# # presenting First 10 countries having
# 1. Confirmed Cases
# 2. Suspected Cases

# In[30]:


plt.figure(figsize=(25,10))
sns.barplot(x = 'Country', y = 'Confirmed_Cases',
            data = monkeypox_data.nlargest(10, 'Confirmed_Cases'))
plt.xticks(rotation = 90)
plt.show()


# In[31]:


plt.figure(figsize=(25,10))
sns.barplot(x = 'Country', y = 'Suspected_Cases',
            data = monkeypox_data.nlargest(10, 'Suspected_Cases'))
plt.xticks(rotation = 90)
plt.show()


# # Dataset loaded countrywise updated on 14th june, 2022

# In[32]:


monkeypox_data_cases = pd.read_csv(r'C:\Users\badal\Downloads\monkeypox new\Daily_Country_Wise_Confirmed_Cases.csv')


# In[33]:


monkeypox_data_cases


# In[34]:


monkeypox_data_cases.head(10)


# In[35]:


monkeypox_data_cases.tail(10)


# In[36]:


monkeypox_data_cases.shape


# In[37]:


monkeypox_data_cases.columns


# In[38]:


monkeypox_data_cases.info()


# In[39]:


monkeypox_data_cases.describe()


# In[40]:


monkeypox_data.nunique()


# # Insights showing cases throughout the world as on 2022-06-09.

# In[41]:


monkeypox_data_cases.isnull().sum()


# In[42]:


monkeypox_data_cases.nunique()


# In[43]:


monkeypox_data_cases['2022-06-09'].unique()


# In[44]:


monkeypox_data_cases['2022-06-09'].value_counts()


# In[45]:


plt.figure(figsize=(15,6))
sns.countplot(x = '2022-06-09', data = monkeypox_data_cases)
plt.xticks(rotation = 90)
plt.show()


# In[46]:


plt.figure(figsize=(15,6))
sns.barplot(y = '2022-06-09', x = 'Country', data = monkeypox_data_cases)
plt.xticks(rotation = 90)
plt.show()


# # Insights from daily cases dataset as on 9th June 2022
# England being the leader in number of active cases and the number being 43
# Germany has recorded the second highest number of cases; 30.

# # Some General comparitive insights which we can get from above plots is:
# 1. England having most number of confirmed cases(183), have very less number of suspected cases(5) which is weird as being near to the most contaminated area increases the risk of suspection of the disease, but here there is not more than 5 suspected case. On the other hand Spain being 2nd on the highest number of confirmed cases has the most number of suspected cases recorded(68).
# 
# 2. Also Canada have the second most number of suspected cases i.e. 35, but is on 5th number when it comes to Confirmed cases. So this is probably a good sign as the cases with suspection can take precautions and have a early cure, also it can be said that people there are more aware and are one more positive side of treatment as if they had seen any sign on MonkeyPox they went to the Hospital to report it.
# 
# 3. There is a less need for hospitalization of the MonkeyPox cases in England, the most affected country, as only 5 cases have been hospitalized till now. On the other hand Gremany and Italy are seeing the most number of hospitalized cases as it has 13 and 14 respectively patients in hospital out of 38 and 20 confirmed cases respectively.
# 
# 4. Italy and USA have most number of cases with travel history 9 and 9 each, approximately 50% of cases have travel history in their records and similar number of patients have been hospitalized; Italy, 12 and USA, 10; confirmed cases being 20 in Italy and 19 in USA. So condition in Italy is a bit severe as more than 50% of patients are in hospitals. (12 out of 20).
