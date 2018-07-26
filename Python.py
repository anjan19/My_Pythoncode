
# coding: utf-8

# In[3]:


def add(x,y):
    return x+y


# In[10]:


add(2.4,3)


# In[17]:


def computepay(hour,rate):
    if hour > 40:
        ot=hour-40
        pay=(hour*rate)+(ot*1.5*rate)
        return pay
    else:
        pay=hour*rate
        return pay


# In[19]:


computepay(40,10)


# In[1]:


height=20
width=80
area_of_rectangle=height*width
print(area_of_rectangle)

