
# coding: utf-8

# In[1]:


def ordnum(a,b):
    if a >  b:
        return [a,b]
    else:
        return [b,a]


# In[3]:


ordnum(1,5)


# In[4]:


def sq(x): return x*x


# In[8]:


def mymap(a,f):
    r=[]
    for i in a:
        v=f(i)
        r.append(v)
    return r
a=[2,3,4]


# In[10]:


mymap(a,sq)


# In[11]:


mymap([2,3,6,7],lambda x: x*3)


# In[18]:


f=lambda x,y:print('we are x and y',str(x)+str(y))
f(1,2)


# In[32]:


a=[2,3,4]
b='anjan'
#for i in a:
    #print(i)
#for i in range(0,len(b)):
    #print(b[i])
for i in range(len(b)):
    print("Happy Bday to: ",b[i])


# In[39]:


an=dict()
an['anjan']=34
an['sree']=25
an['home']='Chengicherla'
print(an)
d2={'shamp': 23,'brush':26,'surf':56}
print(d2)


# In[42]:


print(an.keys())
print(an.values())


# In[3]:


lst=['anjan','ravi','anjan','sree','anjan','sree','sam']
names=dict()
for name in lst:
   # if name not in lst:
    #    names[name] = 1
   # else:
   #     names[name]=names[name] + 1
    names[name]=names.get(name,0)+1
print(names)
for i in names:
    print(i,names[i])
for key,val in names.items():
    print(key,val)


# In[57]:





# In[16]:


wcline=open('wc.txt')
wcount=dict()
line=wcline.read()
wlist=line.split()
#print(wlist)
for word in wlist:
    wcount[word]=wcount.get(word,0)+1    
bigwrd=None
bigval=None
for key,val in wcount.items():
    if bigval is None or val > bigval:
        bigwrd=key
        bigval=val
print(bigwrd,bigval)


# In[14]:


fhand=open('wc.txt')
#for line in fhand:
    #print(line)
line=fhand.read()
wlst=line.split()
print(wlst)


# In[18]:


max(wcount)


# In[19]:


t=('a','b','c')
print(t)


# In[22]:


for i in t:
    print(i)


# In[24]:


(a,b)=(99,100)
print(b)


# In[42]:


def order(x,y):
    if x > y:
        return (x,y)
    else:
        return (y,x)
(a,b)=order(2,1)
print(a,b)


# In[49]:


file=input('Enter the file name: ')
words={}
lst=[]
fh=open(file)
for line in fh:
    wlist=line.split()
    for word in wlist:
        words[word]=words.get(word,0)+1
#print(words)
for k,v in words.items():
    lst.append((v,k))
lst.sort(reverse=True)
#print(lst)
for v,k in lst[:10]:
    print(k,v)


# In[1]:


d={'anjan':34,'ravi':2}
for i in d:
    print(i)


# In[2]:


(0,1,200000)<(0,3,4)

