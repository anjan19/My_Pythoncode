
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


# In[4]:


type(area_of_rectangle)


# In[17]:


area_of_circle=78.5
area_of_circle=str(area_of_circle)


# In[18]:


area_of_circle_msg="Area of the circle is - " + area_of_circle


# In[19]:


print(area_of_circle_msg)


# In[23]:


n=0
while n > 0:
    print("n is :",n)
   # n=n - 1
print("This is done")    
    


# In[25]:


while True:
    line=input('> ')
    if line =='done':
        break
        print(line)
print('End of loop')


# In[26]:


while True:
    line=input('> ')
    if line=='#':
        continue
    if line=='done':
        break
        print(line)
print('done')


# In[6]:


x=[1,2,3,'anjan','ram']


# In[7]:


type(x)


# In[8]:


x


# In[ ]:


for i in x:
    print(i)


# In[ ]:


numlist=[1,4,56,76,23,52]
l_num=-1
for cn in numlist:
    if cn > l_num:
        l_num=nm
        print('Largest so far: ',l_num)
print('The largest is: ':l_num)

